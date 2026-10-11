def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


my_list = [1, 4, 7, 2, 9, 3, 6]
find = 4

result = linear_search(my_list, find)

if result != -1:
    print(f"Element {find} found at index {result}.")
else:
    print(f"Element {find} not found in the list.")
