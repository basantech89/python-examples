import argparse

parser = argparse.ArgumentParser(
    description="Prints the squares of a list of numbers, and the cubes of another list of numbers"
)

# nargs means we'll take a variable number values, it can be *(0 or more), or +(1 or more)
# by default, required is False
parser.add_argument("--sq", help="list of numbers to square", nargs="*", type=float)
parser.add_argument(
    "--cu", help="list of numbers to cube", nargs="+", type=float, required=True
)

args = parser.parse_args()

# if sq is not None, and len of sq > 0, equivalent to truthiness of sq
if args.sq:
    print([n**2 for n in args.sq])

cubes = [n**3 for n in args.cu]
print(cubes)
