from array import array
# variable int
print("Integer : ")
x_int = 10
y_int = 20
sum_int = x_int + y_int
print(x_int , " + " ,y_int ," = ", sum_int,"\n")


# variable float
print("Floating : ")
x_float = 10.5
y_float = 20.5
sum_float = x_float + y_float
print(x_float, " + ",y_float, " = ", sum_float, "\n")


# variable string
print("String : ")
x_string = "Hello to the world of data science"
print(x_string,"\n")


# variable int array, float array
print("Array : ")
x_array = [1, 2, 3, 4, 5]
y_array = [1.2, 2.5, 6.8, 8.99]
sum_array = x_array + y_array
sum_array2 = []
for x in x_array:
    print(x)
for i in range(min(len(x_array),len(y_array))) :
    sum_array2.append(x_array[i] + y_array[i])
print(sum_array)
print(sum_array2,"\n")


# variable list which can include different type of data type
print("List : ")
x_list = [1, 2.5, True, "Asif Ahamed"]
for x in x_list:
    print(x)
print(x_list,"\n")