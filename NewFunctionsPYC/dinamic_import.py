import sys
from contextlib import contextmanager
from importlib.util import spec_from_file_location, module_from_spec
from os.path import dirname


@contextmanager
def correctionPath(p: str):

    old_path = sys.path
    sys.path = sys.path[:]
    sys.path.insert(0, p)

    try:
        yield
    finally:
        sys.path = old_path

def dinamic_import(path: str):
    """Import a python file dynamically

    Args:
    ------
        path (str): Path of file 
    """

    with correctionPath(dirname(path)):
        spec = spec_from_file_location(path, path)
        if spec is not None:
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            return module