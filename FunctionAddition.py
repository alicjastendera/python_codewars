import functools
from collections import defaultdict

class FuncAdd:
    registered_funcs = defaultdict(list)

    def __init__(self, func):
        functools.update_wrapper(self, func)
        FuncAdd.registered_funcs[func.__name__].append(func)
        self.funcname = func.__name__
        

    def __call__(self, *args, **kwargs):
        results = []
        if not self.funcname in FuncAdd.registered_funcs:
            raise NameError
        for func in FuncAdd.registered_funcs[self.funcname]:
            results.append(func(*args, **kwargs))
        return tuple(results)

    @staticmethod
    def delete(func):
        FuncAdd.registered_funcs.pop(func.__name__)

    @staticmethod
    def clear():
        FuncAdd.registered_funcs.clear()
