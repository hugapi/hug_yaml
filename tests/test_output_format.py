"""tests/test_output_format.py.

Tests outputting Python data structures to YAML

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
from collections import namedtuple
from io import BytesIO

from hug_yaml import output_format
from decimal import Decimal

name = namedtuple('Name', ('name', ))


def test_yaml():
    """Test to ensure yaml output_format works as expected"""
    assert output_format.yaml({'hi': 'there'}) == b'hi: there\n'
    assert output_format.yaml(name('tim')) == b'name: tim\n'
    assert output_format.yaml({'one': Decimal(1)}) == b"one: '1'\n"

    stream = BytesIO(b'hi: there\n')
    assert output_format.yaml(stream) == stream
