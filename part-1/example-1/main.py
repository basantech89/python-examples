print("=================================")

print(f"--------- Running main.py, module name: {__name__} ------------")

import module1

print(module1)

del globals()["module1"]

# module1.pprint_dict("module.globals", globals())

print("=================================")
