# recursive 이분탐색


def binary_search(array, target, lower, upper):
    if lower > upper:
        return None
    mid = (lower + upper )//2

    if array[mid] == target :
        return mid
    elif array[mid] > target:
        return binary_search(array, target, mid-1, upper)
    else:
        return binary_search(array, target, mid+1, upper)
n, target = list(map(int, input().split()))


array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result ==None:
    print("원소가 존재하지 않음.")
else:
    print(result +1)