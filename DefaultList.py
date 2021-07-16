class DefaultList:

    def __init__(self, list, default_value) -> None:
        self.list = list
        self.default_value = default_value

    def __getitem__(self, index):
        try:
            return self.list[index]
        except IndexError:
            return self.default_value

    def extend(self, list):
        self.list.extend(list)

    def append(self, item):
        self.list.append(item)

    def insert(self, item, index):
        self.list.insert(item, index)

    def remove(self, item):
        self.list.remove(item)

    def pop(self, index):
        self.list.pop(index)
