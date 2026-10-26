arr = [64, 34, 25, 12, 22, 11, 90]

def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

selectionSort(arr)
print(arr)