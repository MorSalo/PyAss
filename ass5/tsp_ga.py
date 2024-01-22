import random
import sys
import math


def dist(p1, p2):
    return float(math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2))


def fitness(points):
    sum = 0
    if isinstance(points, list):
        for i in range(1, len(points)):
            sum += dist(points[i - 1], points[i])

    return sum


def solve(points):
    mn = sys.maxsize
    for i in range(len(points) * 4):
        ps = points.copy()
        random.shuffle(ps)
        f = fitness(ps)
        if f < mn:
            mn = f
            best = ps
    return best
