from abc import ABC
from numpy import double
from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def calc(self) -> double:
        pass


# implement the classes here
class Num(Expression):

    def __init__(self, x):
        if isinstance(x, int):
            self.x = int(x)
        else:
            self.x = 0

    def calc(self) -> double:
        return self.x


class BinExp(Expression):

    def __init__(self, r, l):
        if isinstance(r, BinExp):
            self.right = BinExp(r.right, r.left)
        elif isinstance(r, Num):
            self.right = Num(r.x)
        else:
            print("right BinExp init error")
        if isinstance(l, BinExp):
            self.left = BinExp(l.right, l.left)
        elif isinstance(l, Num):
            self.left = Num(l)
        else:
            print("left BinExp init error")

    def calc(self) -> double:
        return 0.0


class Div(BinExp):

    def __init__(self, r, l):
        BinExp.__init__(self, r, l)

    def calc(self) -> double:
        return self.left.calc() / self.right.calc()


class Plus(BinExp):

    def __init__(self, r, l):
        BinExp.__init__(self, r, l)

    def calc(self) -> double:
        lefta = self.left.calc()
        rightb = self.right.calc()
        sum = rightb+lefta
        return sum


class Minus(BinExp):

    def __init__(self, r, l):
        BinExp.__init__(self, r, l)

    def calc(self) -> double:
        return self.left.calc() - self.right.calc()


class Mul(BinExp):

    def __init__(self, r, l):
        BinExp.__init__(self, r, l)

    def calc(self) -> double:
        return self.left.calc() * self.right.calc()


# implement the parser function here
def parser(expression) -> double:
    return 0.0
