import os.path
import sys
import types


def import_(module_name: str, module_file: str, module_path: str):
    if module_name in sys.modules:
        return sys.modules[module_name]

    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    # read source code from the file
    with open(module_rel_file_path, "r") as code_file:
        source_code = code_file.read()

    # create a module object
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    # set a ref in sys.modules
    sys.modules[module_name] = mod

    # compile the source code
    code = compile(source_code, filename=module_abs_file_path, mode="exec")

    # execute the compiled code
    # all the things created in mod will be available in mod.__dict__
    exec(code, mod.__dict__)

    return sys.modules[module_name]
