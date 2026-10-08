import common
from common import helpers, models, validators

print("\n\n*********** self ***********")
for k in dict(globals()).keys():
    print(k)

print("\n\n*********** common ***********")
for k in common.__dict__.keys():
    print(k)

print("\n\n*********** models ***********")
for k in models.__dict__.keys():
    print(k)


print("\n\n*********** posts ***********")
for k in models.posts.__dict__.keys():
    print(k)

validators.is_boolean(True)
validators.is_json("{}")
validators.is_date("2020-01-01")

john_post = models.Post()
john_posts = models.Posts()
john = models.User()

print(helpers.say_hello("John"))
print(helpers.factorial(5))
