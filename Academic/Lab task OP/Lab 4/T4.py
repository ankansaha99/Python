def insert_middle(arr, item):
    mid = len(arr) // 2
    arr.insert(mid, item)

arr = [1, 2, 4, 5]
item_to_insert = 3
insert_middle(arr, item_to_insert)
print("Updated Array:", arr)
