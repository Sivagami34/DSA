fruits = ["apple", "banana", "grapes", "kiwi", "lemon"]
fruit = input("Enter a fruit: ")
found = False
start = 0
end = len(fruits) - 1
while start <= end:
    middle = round((start + end)/2)
    print(fruits[middle])
    #// can also be used
    if fruits[middle] == fruit:
        print("found at", middle)
        found = True
        break
    elif fruits[middle] < fruit:
        start = middle + 1
    elif fruits[middle] > fruit:
        end = middle - 1
if found == False:
    print("Item not in list")