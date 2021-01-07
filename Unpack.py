from collections.abc import Iterable

def unpack_iter(items):
    result = []
    while len(items) > 0:
        item = items.pop(0)
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            if isinstance(item, dict):
                new_items = []
                for k, v in item.items():
                    new_items.append(k)
                    new_items.append(v)
                new_items.extend(items)
                items = new_items
            else:
                item = list(item)
                item.extend(items)
                items = item
        else:
            result.append(item)
    return result

def unpack(x):
    if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):       
        flat = []
        if isinstance(x, dict):
            for k, v in x.items():
                flat.extend(unpack(k))
                flat.extend(unpack(v))
        else:
            for i in x:
                flat.extend(unpack(i))
        return flat     
    else:
        return [x]
    


if __name__ == "__main__":
    x = ([None, [1, ({2, 3}, {'foo': {4, 5}, "ggg": "uuu"}, 99 ,  {'foo2': 'ba2r'})]])

    print(unpack(x))
    print(unpack_iter(x))
