from collections import deque


# all sub arrays sums
def MyAllSumsDP(arr):
    helper = set()
    stack = deque()
    stack2 = deque()
    for i in range(len(arr) - 1, -1, -1):
        if i == len(arr) - 1:
            helper.add(arr[i])
            stack.append(arr[i])
        else:
            while len(stack) != 0:
                x = stack.pop()
                helper.add(arr[i] + x)
                stack2.append(arr[i] + x)
            helper.add(arr[i])
            stack2.append(arr[i])
            stack.clear()
            stack = deque(stack2)
            stack2.clear()
    return sorted(helper)


# all sums
def allSumsDP(arr):
    helper = set()
    helper.add(0)
    helper.add(arr[len(arr)-1])
    for i in range(len(arr) - 2, -1, -1):
        x = arr[i]
        nw = set(helper)
        for j in nw:
            helper.add(x+j)
        helper.add(x)
    return helper
