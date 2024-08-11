
def merge(array, start, middle, end):
    c1 = start
    c2 = middle + 1
    result = []
    while c1 <= middle and c2 <= end:
        if array[c1] < array[c2]:
            result.append(array[c1])
            c1 += 1
        else:
            result.append(array[c2])
            c2 += 1
    while c1 <= middle:
        result.append(array[c1])
        c1 += 1
    while c2 <= end:
        result.append(array[c2])
        c2 += 1
    k = 0
    for i in range(start, end+1):
        array[i] = result[k]
        k += 1

def mergesort(array, start, end):
    if start < end:
        middle = (start + end)//2
        mergesort(array, start, middle)
        mergesort(array, middle + 1, end)
        merge(array, start, middle, end)

numbers = [1, 7, 4, 2, 3, 9, 8, 5]
mergesort(numbers, 0, len(numbers)-1)
print(numbers)