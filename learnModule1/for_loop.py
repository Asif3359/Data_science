# from learnModule1.list_matrices_dectonary import fruits

print("For Loop : ")
fruits = ["mango", "apple", "banana", "orange"]
for i in range(len(fruits)):
    print(fruits[i], end=" ")
print()
for fruit in fruits:
    print(fruit, end=" ")
print()
string = "something"
for char in string:
    print(char, " ", end=" ")
print()
for fruit in fruits:
    for ch in fruit:
        print(ch, " ", end=" ")
    print()


# linear search
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 5
for i, x in enumerate(numbers):
    if x == k:
        print(i)
        print("Found")
        break


# Binary search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

index = binary_search(numbers, k)
if index != -1:
    print(index)
else:
    print(-1)
print()



# sum 1 to 10
sum_num = 0
for i in range(1,10+1):
    sum_num += i
    print(i, end=" ")
print()
print(sum_num)