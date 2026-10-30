import sys

sys.path.append("./common.zip")

import common

# from common.models import *
from common import helpers, models, validators

validators.is_boolean("true")
validators.is_json("{}")
validators.is_numeric(10)
validators.is_date("2018-0101")

john_post = models.Post()
john_posts = models.Posts()
john = models.User()


print("\n\n***** self *****")
for k in dict(globals()).keys():
    print(k)


print("\n\n***** common *****")
for k in common.__dict__.keys():
    print(k)

print("\n\n***** models *****")
for k in common.models.__dict__.keys():
    print(k)

print(helpers.say_hello("Python"))
print(helpers.factorial(5))
