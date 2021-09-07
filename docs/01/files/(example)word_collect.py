#! /opt/anaconda3/bin/python
# -*- encoding: utf-8 -*-

import re

target_part = re.compile(r'통합\\(.+)\.log')


with open('input.txt', encoding='utf8') as inf:
    with open('output.txt', 'w') as of:
        for line in inf:
            _line = line.rstrip()
            print(_line)
            match = target_part.findall(_line)

            if match:
                of.write(match[0]+'\n')