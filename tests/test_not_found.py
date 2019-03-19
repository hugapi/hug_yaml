"""Tests hug_yaml's YAML formatted documentation support"""
import hug

from hug_yaml import not_found, output_format

api = hug.API(__name__)
api.extend(not_found)


@hug.get()
def hello():
    return


@hug.not_found(output=output_format.yaml)
def documentation(hug_api, hug_api_version):
    return not_found.documentation(hug_api, hug_api_version)


def test_not_found():
    """Test to ensure hug_yaml is able to override hug's defualt documentation format"""
    print(hug.test.get(api, '/documentation').data)
    assert hug.test.get(api, '/documentation').data == \
           ("handlers:\n"
            "  /hello:\n"
            "    GET:\n"
            "      examples:\n"
            "      - /hello\n"
            "      outputs:\n"
            "        content_type: application/json; charset=utf-8\n"
            "        format: JSON (Javascript Serialized Object Notation)\n"
            "overview: Tests hug_yaml's YAML formatted documentation support\n")
