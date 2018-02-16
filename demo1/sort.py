num_array = [6, 1, 9, 90, 34, 20, 10, 36, 89]
k = num_array.__len__()
print sorted(num_array)
print sorted(num_array,reverse=True)


for j in range(0, k - 1, 1):
    for i in range(j+1, k, 1):
        if num_array[j] < num_array[i]:
            temp = num_array[j]
            num_array[j] = num_array[i]
            num_array[i] = temp
print num_array
print num_array[k-1]
print num_array[0]


