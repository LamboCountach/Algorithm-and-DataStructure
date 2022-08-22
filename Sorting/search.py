def linear_search(li, val):
    for v in range(len(li)):
        if li[v] == val:
            return v
    else:
        return None

def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

li = [1,2,3,4,5,6,7]
print(binary_search(li,3))
