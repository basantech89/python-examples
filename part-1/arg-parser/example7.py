import argparse

parser = argparse.ArgumentParser(description="Defaults and Flags")

parser.add_argument("-q", "--quiet", action="store_true")

args = parser.parse_args()

print(args)
