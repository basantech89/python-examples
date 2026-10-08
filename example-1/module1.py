print(f"--------- Running {__name__} ------------")

from typing import Any


def pprint_dict(header: str, d: dict[str, Any]):
    print("\n\n----------------------------")
    print(f"****** {header} ******")
    for k, v in d.items():
        print(f"{k}: {v}")
    print("----------------------------\n\n")


pprint_dict("module.globals", globals())

print(f"------------------- End of {__name__} -------------------")
