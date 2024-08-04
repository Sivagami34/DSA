numbers = [8, 9, 4, 5, 7, 2, 1, 6]
for i in range(len(numbers)):
    key = numbers[i]
    j = i-1
    while key < numbers[j] and j >= 0:
        numbers[j+1] = numbers[j]
        j = j-1
    numbers[j+1] = key
    print(numbers)
    print()