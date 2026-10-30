import common
from common import validators

print("\n\n*********** self ***********")
for k in dict(globals()).keys():
    print(k)

print("\n\n*********** common ***********")
for k in common.__dict__.keys():
    print(k)

print("\n\n*********** validators ***********")
for k in validators.__dict__.keys():
    print(k)

print("\n\n*********** numeric ***********")
for k in validators.numeric.__dict__.keys():
    print(k)

print("\n\n*********** boolean ***********")
for k in validators.boolean.__dict__.keys():
    print(k)

print("\n\n*********** dir(common.validators) ***********")
print(validators.__dict__.keys())

validators.is_boolean(True)
validators.is_json("{}")
validators.is_date("2020-01-01")
