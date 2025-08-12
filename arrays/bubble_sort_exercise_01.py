numbers = [45, 12, 78, 4, 90, 23, 56, 1]


n = len(numbers)


for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if numbers[j] < numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            swapped = True
    if not swapped:
        break


print("numbers in descending order : ", numbers)
