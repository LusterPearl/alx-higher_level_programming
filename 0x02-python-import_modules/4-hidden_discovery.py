#!/usr/bin/python3
import hidden_4
all_names = dir(hidden_4)
for names in all_names:
    if name[:2] != '__':
        print(name)
