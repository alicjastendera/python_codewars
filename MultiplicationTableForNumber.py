def multi_table(number):
    return ("".join("{} * {} = {}\n".format(count, number, count*number) for count in range(1, 11))).strip("\n")
