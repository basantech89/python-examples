"""
Times how long a snippet of code takes to run over multiple iterations.
"""

import argparse
from time import perf_counter
from typing import NamedTuple


class Timing(NamedTuple):
    repeats: int
    elapsed: float
    average: float


def timeit(code: str, repeats: int = 10):
    compiled_code = compile(code, filename="<string>", mode="exec")

    start = perf_counter()

    for _ in range(repeats):
        exec(compiled_code)

    end = perf_counter()

    elapsed = end - start
    average = elapsed / repeats

    return Timing(repeats, elapsed, average)


if __name__ == "__main__":
    # grab the module docstring added above and use it when user runs the script with a -h or --help flag
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("code", type=str, help="The python code snippet to time.")
    parser.add_argument(
        "-r",
        "--repeats",
        default=10,
        type=int,
        help="The number of times to repeat the code snippet.",
    )

    args = parser.parse_args()
    print(f"timing: {args.code}...")

    result = timeit(code=str(args.code), repeats=args.repeats)
    print(result)
