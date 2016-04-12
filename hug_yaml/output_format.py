"""hug_yaml/output_format.py.

YAML output formatter for hug

Copyright (C) 2016 Timothy Edmund Crosley

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

"""
import decimal
import types
from collections import OrderedDict

import hug
import yaml
from yaml import MappingNode, SafeDumper, ScalarNode, dump, representer


class SafeDumper(SafeDumper):
    """Handles decimals as strings.
       Handles OrderedDicts as usual dicts, but preserves field order, rather
       than the usual behaviour of sorting the keys.
    """
    def represent_decimal(self, data):
        return self.represent_scalar('tag:yaml.org,2002:str', str(data))

    def represent_mapping(self, tag, mapping, flow_style=None):
        value = []
        node = MappingNode(tag, value, flow_style=flow_style)
        if self.alias_key is not None:
            self.represented_objects[self.alias_key] = node
        best_style = True
        if hasattr(mapping, 'items'):
            mapping = list(mapping.items())
            if not isinstance(mapping, OrderedDict):
                mapping.sort()
        for item_key, item_value in mapping:
            node_key = self.represent_data(item_key)
            node_value = self.represent_data(item_value)
            if not (isinstance(node_key, ScalarNode) and not node_key.style):
                best_style = False
            if not (isinstance(node_value, ScalarNode) and not node_value.style):
                best_style = False
            value.append((node_key, node_value))
        if flow_style is None:
            if self.default_flow_style is not None:
                node.flow_style = self.default_flow_style
            else:
                node.flow_style = best_style
        return node

SafeDumper.add_representer(decimal.Decimal, SafeDumper.represent_decimal)
SafeDumper.add_representer(OrderedDict, representer.SafeRepresenter.represent_dict)
SafeDumper.add_representer(types.GeneratorType, representer.SafeRepresenter.represent_list)


@hug.format.content_type('text/yaml')
def yaml(content, **kwargs):
    """YAML (Yet Another Markup Language - A superset of JSON)"""
    if hasattr(content, 'read'):
        return content

    if isinstance(content, tuple) and getattr(content, '_fields', None):
        content = {field: getattr(content, field) for field in content._fields}

    return dump(content, default_flow_style=False, Dumper=SafeDumper).encode('utf8')
