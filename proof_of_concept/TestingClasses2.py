import inspect
from proof_of_concept import script

all_functions = inspect.getmembers(script, inspect.isfunction)
for function in all_functions:
    function[1]()