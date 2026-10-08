import argparse

parser = argparse.ArgumentParser(
    description="Calculates the div a // b and a % b of two integers"
)

parser.add_argument("a", type=int, help="The dividend")
parser.add_argument("b", type=int, help="The divisor")

args = parser.parse_args()
a = args.a
b = args.b

print(f"{a // b = }, {a % b = }")
