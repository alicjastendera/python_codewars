import re
def sort_by_binary_ones (num_list): 
    def sorter_fn(item):
        binary = bin(item)
        binary_ones = len(re.findall("[1]", binary))
        binary_len = -len(binary)
        binary_value = -item
        return (binary_ones, binary_len, binary_value)

    return sorted(num_list, key=sorter_fn, reverse=True)