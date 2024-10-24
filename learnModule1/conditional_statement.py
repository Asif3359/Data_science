# if else check even or odd
print("Ef else : ")
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
print()

age = 60
age_cat = ""
if age >= 70:
    age_cat = "old man"
elif 69 >= age >= 40:
    age_cat = "young man"
else:
    age_cat = "young"
print(age_cat)