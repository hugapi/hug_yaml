"""Example showing how to set YAML as default CLI output format

This example illustrates two different methods of changing the default CLI
output format.

"""

import hug
import hug.interface
import hug_yaml
from hug.routing import CLIRouter


API = hug.API(__name__)


class YamlCli(CLIRouter):
    def __call__(self, api_function):
        """Enable exposing a Hug compatible function as a CLI

        This overridden implementation uses YAML as the default output format.

        This is method #1 for overriding the default output format.

        """
        cli = hug.interface.CLI(self.route, api_function)
        cli.outputs = hug_yaml.output
        return api_function


def yaml_cli(*args, **kwargs):
    """CLI decorator which sets YAML as the default output format

    This is method #2 for overriding the default output format.

    """
    def wrapper(func):
        return hug.cli(*args, output=hug_yaml.output, **kwargs)(func)
    return wrapper


@YamlCli()  # method #1
def hello():
    return {'name': 'hug_yaml',
            'author': 'Timothy Crosley'}


@yaml_cli()  # method #2
def goodbye():
    return {'name': 'hug_yaml',
            'author': 'Timothy Crosley'}


if __name__ == '__main__':
    API.cli()
