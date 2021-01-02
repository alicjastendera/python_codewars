import json

def jsonattr(filepath):
    def decorator_jsonattr(func):
        with open(filepath, "r") as f:
            data = json.load(f)
        for name, value in data.items():            
            setattr(func, name, value)
        return func
    return decorator_jsonattr