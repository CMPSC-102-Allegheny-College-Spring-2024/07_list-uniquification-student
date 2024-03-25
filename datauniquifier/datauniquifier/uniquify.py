"""Perform uniquification on the provided input of a list of strings."""

from typing import List

from functools import wraps
from time import time

def timing(function):
    """Define a profiling function for execution time."""
    # Reference:
    # https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
    @wraps(function)
    def wrap(*args, **kw):
        ts = time()
        result = function(*args, **kw)
        te = time()
        print("The function %r took: %2.4f sec" % (function.__name__, te - ts))
        return result

    return wrap


# TODO: Read the reference for a description of the functions:
#
# https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6
#
# Note that this module does not contain all of the functions in the post

# TODO: If you would like to do so, add and then experimentally evaluate more methods

# TODO: Make sure that you understand the purpose of the timing annotation for these functions
# TODO: Add the timing annotation to each of the following functions

@timing
def unique_set(data: List[str]) -> List[str]:
    """Perform uniquification of the input list of strings and return results in a list of strings."""
    # TODO: Add the source code for method f7
    # TODO: You may need to add type hints or statements to support mypy checking

@timing
def unique_listcomprehension(data: List[str]) -> List[str]:
    """Perform uniquification of the input list of strings and return results in a list of strings."""
    # TODO: Add the source code for method f8
    # TODO: You may need to add type hints or statements to support mypy checking

@timing
def unique_dictionary(data: List[str]) -> List[str]:
    """Perform uniquification of the input list of strings and return results in a list of strings."""
    # TODO: Add the source code for method f12
    # TODO: You may need to add type hints or statements to support mypy checking
