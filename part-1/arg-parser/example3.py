import sys

keys = sys.argv[1::2]
values = sys.argv[2::2]

names = {k: v for k, v in zip(keys, values)}

first_name = names.get("--first-name", None)

print(first_name)
