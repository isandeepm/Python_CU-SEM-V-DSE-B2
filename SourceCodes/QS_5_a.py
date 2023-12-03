def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left
    if right:
        result += right
    return result

if __name__ == '__main__':
    qarr = [5, 10, 8, 4, 9, 2, 7, 6]
    marr = [6, 2, 5, 10, 9, 4, 3, 8]
    qres = quick_sort(qarr)
    mres = merge_sort(marr)
    print("OUTPUT-1")
    print("Input unsorted list: ", qarr)
    print("Sorted list using quicksort: ", qres)
    print("Input unsorted list: ", marr)
    print("Sorted list using mergesort: ", mres)

    qarr = [5, 10, 8, 4, 9, 2, 7, 6]
    qres = quick_sort(qarr)
    mres = merge_sort(marr)
    print("OUTPUT-2")
    print("Input unsorted list: ", qarr)
    print("Sorted list using quicksort: ", qres)
    print("Input unsorted list: ", marr)
    print("Sorted list using mergesort: ", mres)