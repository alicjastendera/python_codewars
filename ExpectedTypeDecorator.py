class UnexpectedTypeException(Exception):
    pass

def expected_type(return_types):
    def expected_type_decorator(func):
        def func_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not any([isinstance(result, exp_type) for exp_type in return_types]):
                raise UnexpectedTypeException
            return result
        return func_wrapper
    return expected_type_decorator
