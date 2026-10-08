import argparse
import datetime

parser = argparse.ArgumentParser(
    description="Returns a string containing the name and age of the person."
)

# if we've provided both the short(-f) and the long name(--first), argparse will use the long name(first) if both are present
# we can map this name to the variable name we want in the namespace with the dest option
parser.add_argument(
    "-f", "--first", type=str, help="first name", required=False, dest="first_name"
)
parser.add_argument(
    "-l", "--last", type=str, help="last name", required=True, dest="last_name"
)
parser.add_argument(
    "--yob",
    type=int,
    help="year of birth of the person",
    required=True,
    dest="birth_year",
)

args = parser.parse_args()

names = [args.first_name] if args.first_name else []
if args.last_name:
    names.append(args.last_name)

full_name = " ".join(names)

current_year = datetime.datetime.now(tz=datetime.timezone.utc).year
age = current_year - args.birth_year

print(f"{full_name} is {age} years old.")
