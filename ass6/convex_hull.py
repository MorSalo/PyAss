import math


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def lowest(p1, p2) -> Point:
    if p1.y == p2.y:
        return min(p1.x, p2.x)
    else:
        return min(p1.y, p2.y)


def findBottomLeft(points: list) -> Point:
    bottom_left = points[0]

    for point in points[1:]:
        if point.y < bottom_left.y or (point.y == bottom_left.y and point.x < bottom_left.x):
            bottom_left = point

    return bottom_left


def sortCCW(points: list):
    pivot = findBottomLeft(points)
    points.sort(key=lambda point: math.degrees(math.atan2(point.y - pivot.y, point.x - pivot.x)))


def isLeftTurn(p1: Point, p2: Point, p3: Point):
    area = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
    # 0 means collinear so what to do?
    if area < 0:
        return False
    elif area > 0:
        return True
    elif area == 0:
        return 0


def grahamScan(points: list):
    n = len(points)

    # Find the pivot point (point with lowest y-coordinate)
    pivot = findBottomLeft(points)

    # Sort the points based on polar angle with respect to the pivot
    sortCCW(points)

    # Initialize the convex hull with the pivot and the first two sorted points
    hull = []
    hull.append(points[0])
    hull.append(points[1])
    hull.append(points[2])
    # Iterate through the sorted points to build the convex hull
    for i in range(2, n):
        while len(hull) > 1 and not isLeftTurn(hull[-2], hull[-1], points[i]):
            hull.pop()
        hull.append(points[i])
    hull.append(hull[0])
    return hull
