"""hug_yaml/input_format.py.

YAML input formatters for hug to handle both application/x-yaml and text/yaml

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
import hug
import yaml


def convert(data, charset='utf-8', safe=True):
    """Converts the YAML data into a Python Data structure: if safe is set to False YAML object loading is possible"""
    return (yaml.safe_load if safe else yaml.load)(data.read().decode(charset))


@hug.default_input_format('text/yaml')
def text_yaml(data, **kwargs):
    """Converts a `text/yaml` YAML request into a Python Data structure"""
    return convert(data, **kwargs)


@hug.default_input_format('application/x-yaml')
def application_yaml(data, **kwargs):
    """Converts an `application/x-yaml` YAML request into a Python Data structure"""
    return convert(data, **kwargs)
