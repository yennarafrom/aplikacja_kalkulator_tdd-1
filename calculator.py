number_types = [int, float, complex]


class Calculator:

    @staticmethod
    def validate_args(x, y):
        if type(x) not in number_types and type(y) not in number_types:
            raise ValueError

    def add(self, x, y):
        self.validate_args(x, y)
        return x + y

    def mul(self, x, y):
        self.validate_args(x, y)
        return x*y

    def sub(self, x, y):
        self.validate_args(x, y)
        return x-y

    def div(self, x, y):
        self.validate_args(x, y)
        if y != 0:
            return x/y
        else:
            raise ValueError
