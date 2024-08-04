#numbers = [6, 9, 2, 3, 5, 7]
numbers = ["one", "five", "two", "seven", "three", "four", "six"]
for l in range(len(numbers)):
    print("pass", l+1)
    swap = False
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            t = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = t
            swap = True
    if swap == False:
        break
    print(numbers)