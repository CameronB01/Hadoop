#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
import re

for line in sys.stdin:
    line = line.strip()
    words = re.findall(r'[a-zA-Z]+', line)
    for word in words:
        word = word.lower()
        print('%s\t%s' % (word, 1))

