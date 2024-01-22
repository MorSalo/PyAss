from array import array


def dnc(baseFunc, combineFunc):
    def f(arr) -> int:
        if len(arr) == 1:
            return baseFunc(arr[0])
        else:
            mid = len(arr) // 2
            arr1 = arr[:mid]
            arr2 = arr[mid:]
            x = combineFunc(f(arr1), f(arr2))
            return x

    return f


def maxAreaHist(hist):
    if not hist:
        return 0

    return calculate_area(hist, 0, len(hist) - 1)


def calculate_area(hist, start, end):
    if start > end:
        return 0

    min_index = start
    for i in range(start, end + 1):
        if hist[i] < hist[min_index]:
            min_index = i

    return max(
        hist[min_index] * (end - start + 1),
        calculate_area(hist, start, min_index - 1),
        calculate_area(hist, min_index + 1, end)
    )
