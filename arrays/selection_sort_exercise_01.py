scores = [88, 75, 96, 55, 64, 99, 82]


n = len(scores)
total_swaps = 0


for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if scores[j] < scores[min_index]:
            min_index = j

    print(f"Pass {i+1}: smallest index = {min_index}")

    if min_index != i:
        scores[i], scores[min_index] = scores[min_index], scores[i]
        total_swaps += 1

print("total swaps : ", total_swaps)
print("sorted scores : ", scores)
