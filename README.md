hug_yaml
===================

[![PyPI version](https://badge.fury.io/py/hug_yaml.svg)](http://badge.fury.io/py/hug_yaml)
[![Build Status](https://travis-ci.org/timothycrosley/hug_yaml.svg?branch=master)](https://travis-ci.org/timothycrosley/hug_yaml)
[![Coverage Status](https://coveralls.io/repos/timothycrosley/hug_yaml/badge.svg?branch=master&service=github)](https://coveralls.io/github/timothycrosley/hug_yaml?branch=master)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/hug_yaml/)
[![Join the chat at https://gitter.im/timothycrosley/hug](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/timothycrosley/hug?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

An extension for hug that provides YAML input formats, output formats, and documentation:

```py
import hug
import hug_yaml

hug.API(__name__).extend(hug_yaml.input_format)


@hug.not_found(output=hug_yaml.output)
def documentation(hug_api, hug_api_version):
    return hug_yaml.not_found.documentation(hug_api, hug_api_version)
```

Installing hug_yaml
===================

Installing hug_yaml is as simple as:

```bash
pip3 install hug_yaml --upgrade
```

Ideally, within a virtual environment.


Why hug_yaml?
===================

An extension for hug that provides YAML input formats, output formats, and documentation.

--------------------------------------------

Thanks and I hope you find hug_yaml helpful!

~Timothy Crosley
