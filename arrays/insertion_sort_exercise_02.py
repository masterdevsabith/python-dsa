arr = [42, 5, 42, 19, 0, 27, 27, 15, 100, 3, 100, 8]


n = len(arr)

for i in range(1, n):
    insert_index = i
    current_value = arr[i]
    for j in range(i-1, -1, -1):
        if arr[j] < current_value:
            arr[j+1] = arr[j]
            insert_index = j
        else:
            break

    arr[insert_index] = current_value


print(
    f'sorted array is {arr}'
)
