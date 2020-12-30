from time import perf_counter

def timer(limit):
    def decorator_timer(func):
        def wrapper_timer(*args, **kwargs):
            tic = perf_counter()
            func(*args, **kwargs)
            toc = perf_counter()
            time_elapsed = toc - tic
            return False if time_elapsed > limit else True                
        return wrapper_timer
    return decorator_timer
