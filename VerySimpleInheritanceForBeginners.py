import abc


class Operation(abc):
    def __init__(self):
        self.result = None

    @abc.abstractmethod
    def execute(self, v1, v2):
        pass


class Add(Operation):
    def execute(self, v1, v2):
        self.result = v1 + v2


class Subtract(Operation):
    def execute(self, v1, v2):
        self.result = v1 - v2


class Multiply(Operation):
    def execute(self, v1, v2):
        self.result = v1 * v2


class Divide(Operation):
    def execute(self, v1, v2):
        if v2 == 0:
            self.result = None
            return
        self.result = v1 / v2
