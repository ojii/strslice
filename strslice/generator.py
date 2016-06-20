import json

import os
from argparse import ArgumentParser

from requests import get
from jinja2 import Template

from . import gen

TEMPLATE = Template('''# Auto-generated file, do not edit manually
# Re-generate using the `strslice-generate` command
# Unicode Version {{ version }}


def get(num):{% for check, result in ranges %}
    {% if check.simple %}if {{ check.low }} == num{% else %}if {{ check.low }} <= num <= {{ check.high }}{% endif %}:
        return {{ result }}{% endfor %}
    return {{ default }}

''')


class Check(object):
    def __init__(self, low, high=None):
        self.low = low
        self.high = high
        self.simple = self.high is None


def range_gen(lines):
    for line in map(str.strip, lines):
        if not line:
            continue
        if line.startswith('#'):
            continue
        if '#' in line:
            line = line[:line.index('#')]
        num, cat = map(str.strip, line.split(';'))
        if '..' in num:
            low, high = num.split('..')
            check = Check('0x' + low, '0x' + high)
        else:
            check = Check('0x' + num)
        yield check, json.dumps(cat)


def generate(url, version, default):
    resp = get(url)
    resp.raise_for_status()
    ranges = range_gen(resp.content.splitlines())
    return TEMPLATE.render(
        version=version,
        ranges=ranges,
        default=json.dumps(default)
    )


def run(url, version, default, output):
    result = generate(url, version, default)
    with open(output, 'w') as fobj:
        fobj.write(result)


def cli():
    gen_dir = os.path.dirname(gen.__file__)
    parser = ArgumentParser()
    parser.add_argument(
        '-v',
        '--unicode-version',
        default='8.0.0'
    )
    parser.add_argument(
        '-u',
        '--url',
        default='http://www.unicode.org/Public/{version}/ucd/auxiliary/GraphemeBreakProperty.txt'
    )
    parser.add_argument(
        '-o',
        '--output',
        default=os.path.join(gen_dir, 'grapheme_break_properties.py')
    )
    parser.add_argument(
        '-d',
        '--default',
        default='Other',
    )
    args = parser.parse_args()
    run(
        args.url.format(version=args.unicode_version),
        args.unicode_version,
        args.default,
        args.output,
    )
