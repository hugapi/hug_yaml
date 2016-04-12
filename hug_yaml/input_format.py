import yaml


def _convert_input_format(data, encoding='utf-8', safe=True):
    """Converts the YAML data into a Python Data structure"""
    return (yaml.safe_load if safe else yaml.load)(data.read().decode(encoding))


@hug.default_input_format('text/yaml', apply_globally=True)
def text_yaml(data, encoding='utf-8'):
    """Converts the YAML data into a Python Data structure"""
    return _convert_input_format(data, encoding)


@hug.default_input_format('application/x-yaml', apply_globally=True)
def application_yaml(data, encoding='utf-8'):
    """Converts the YAML data into a Python data structure"""
    return _convert_input_format(data, encoding)
