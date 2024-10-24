
print("List : ")
fruits = ["mango", "apple", "banana", "orange"]
print(len(fruits))
print(fruits[0])
print(fruits[len(fruits)-1])
fruits[1] = "jackfruit"
print(fruits)
print()

print("Matrices :")
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"{matrix[i][j]}", end=" ")
    print()
print()


print("2D Pattern : ")
x = 5
for i in range(x):
    for j in range(i+1):
        print("*", end=" ")
    print()
print()


print("Dictionary : ")
resident = {
    "name":"Asif Ahammed",
    "city":"Dhaka",
    "numbers":[10,12,13,14]
}
print(resident)
resident["numbers"][1]=15
for key,value in resident.items():
    print(f"{key} : {value}")
print()