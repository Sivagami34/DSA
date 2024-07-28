fruits = ["apple", "orange", "banana", "pear", "kiwi"]
fruit = input("Enter a fruit: ")
found = False
for i in range(len(fruits)):
    if fruits[i] == fruit:
        print("found at", i)
        found = True
        break
#else:
    #print("Item not in list")
if found == False:
    print("Item not in list")