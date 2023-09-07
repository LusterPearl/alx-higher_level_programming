#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    all_names = dir(hidden_4)
for names in all_names:
    if name[:2] != '__':
        print(name)
