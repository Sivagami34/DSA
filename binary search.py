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

# using recursion

def binary(array, key, start, end):
    middle = round((start + end)/2)
    print(array[middle])
    if start <= end:
        if array[middle] == key:
            print("found at", middle)
        elif array[middle] < key:
            binary(array, key, middle+1, end)
        elif array[middle] > key:
            binary(array, key, start, middle-1)
    else:
        print("Item not found")
binary(fruits, fruit, 0, len(fruits)-1)
