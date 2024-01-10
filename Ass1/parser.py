from abc import ABC
from numpy import double
from abc import ABC, abstractmethod
from collections import deque
import queue as q


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

    def __init__(self, left, right):
        if isinstance(left, BinExp):
            self.left = left
        elif isinstance(left, Num):
            self.left = Num(left.x)

        if isinstance(right, BinExp):
            self.right = right
        elif isinstance(right, Num):
            self.right = Num(right.x)

    def calc(self) -> double:
        return 0.0


class Div(BinExp):

    def __init__(self, left, right):
        BinExp.__init__(self, left, right)

    def calc(self) -> double:
        return self.left.calc() / self.right.calc()


class Plus(BinExp):

    def __init__(self, left, right):
        BinExp.__init__(self, left, right)

    def calc(self) -> double:
        lefta = self.left.calc()
        rightb = self.right.calc()
        sum = lefta + rightb
        return sum
        # return self.left.calc() + self.right.calc()


class Minus(BinExp):

    def __init__(self, left, right):
        BinExp.__init__(self, left, right)

    def calc(self) -> double:
        lefta = self.left.calc()
        rightb = self.right.calc()
        sum = lefta - rightb
        return sum
        # return self.left.calc() - self.right.calc()


class Mul(BinExp):

    def __init__(self, left, right):
        BinExp.__init__(self, left, right)

    def calc(self) -> double:
        return self.left.calc() * self.right.calc()


# implement the parser function here
def isOperator(c):
    if c == '+' or c == '-' or c == '*' or c == '/':
        return 1
    else:
        return 0


def isNumber(c):
    try:
        int(c)
        return True
    except Exception:
        return False


def isLeftParen(c):
    return c == '('


def isRightParen(c):
    return c == ')'


def notEmpty(s):
    s = deque(s)
    try:
        return s[0]
    except Exception:
        return 0


# 0- do not change
# 1- change!
def precedence(c, x):
    if isOperator(c):
        if c == '*' or c == '/':
            return 0
        if (c == '+' and x == '-') or (c == '-' and x == '+'):
            return 1
        if (c == '+' or c == '-') and (x == '*' or x == '/'):
            return 1
    else:
        return 0


def isMinus(c):
    return c == "-"


def shuntingYard(expression) -> list:
    queue = []
    stack = deque()
    i = 0

    while i < len(expression):
        c = expression[i]
        if isNumber(c):
            num = c
            j = i + 1
            while isNumber(expression[j]):
                num += expression[j]
                j += 1
            queue.append(num)
            i = j - 1
        elif isOperator(c):
            while notEmpty(stack) and precedence(c, stack[-1]):
                queue.append(stack.pop())
            stack.append(c)
        elif isLeftParen(c):
            if expression[i + 1] == "-":
                num = expression[i + 1]
                j = i + 2
                while isNumber(expression[j]):
                    num += expression[j]
                    j += 1
                queue.append(num)
                i = j
            else:
                stack.append(c)
        elif isRightParen(c):
            while notEmpty(stack) and not isLeftParen(stack[-1]):
                queue.append(stack.pop())
            if notEmpty(stack):
                stack.pop()


        i += 1

    while notEmpty(stack):
        queue.append(stack.pop())

    return queue


def parser(expression) -> double:
    if isinstance(expression, str):
        expression = str(expression)

    queue = shuntingYard(expression)
    helper = deque()
    i = 0
    for my in queue:
        if isNumber(my):
            helper.append(Num(int(my)))
        if isOperator(my):

            if notEmpty(helper):
                right = helper.pop()
                if notEmpty(helper):
                    left = helper.pop()
                else:
                    continue
            else:
                continue

            exp = 0
            if my == "+":
                exp = Plus(left, right)
            elif my == "-":
                exp = Minus(left, right)
            elif my == "*":
                exp = Mul(left, right)
            elif my == "/":
                exp = Div(left, right)

            # match my:
            #     case "+":
            #         exp = Plus(left, right)
            #     case "-":
            #         exp = Minus(left, right)
            #     case "*":
            #         exp = Mul(left, right)
            #     case "/":
            #         exp = Div(left, right)

            helper.append(exp)

        i += 1

    return helper.pop().calc()
