height= int(input("Enter your height in meters:"))
weight= int(input("Enter your weight in kilogram:"))

BMI=weight/(height*height)
print("BMI is:" , BMI)

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your Weight in Kilogram: "))

BMI = weight / (height * height)
print("BMI is: " , BMI)


if (BMI > 40):
    print("You are obese")
elif BMI >= 32 and BMI <= 39:
    print("You are overweight")
elif BMI >= 29 and BMI <= 31:
    print(" You have a normal weight")
elif BMI >= 18 and BMI <= 28:
    print("You are underweight")
elif BMI < 17:
    print("You are malnourished")


