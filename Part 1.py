
#derive function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

#loop to iterate through individuals' data
Students = int(input("Enter the number of students: "))
for i in range(3):
    print(f"Students {i+1}:")
    weight = float(input("Enter weight in kg:"))
    height = float(input("Enter weight in m:"))
    bmi = calculate_bmi(weight, height)

#if/elif conditions to determine BMI category
if bmi <18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi <30:
    category = "Overweight"
elif bmi >= 30:
    category = "Obese"
else:
    category = "Invalid BMI"

print(f"BMI: {bmi: .2f}), Category: {category}")

#determine if given BMI number is even or od
bmi_num = float(input("Enter a BMI number: "))
if bmi_num % 2 == 0:
    print("Even")
else:
    print("Odd")