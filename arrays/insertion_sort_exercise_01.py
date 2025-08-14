arr = [15, 3, 27, 8, 19, 42, 5]


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
    print(f'array at pass {i} is {arr}')


print(f'final sorted array is : {arr}')
