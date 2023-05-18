def calculate_bmi(weight, height):
 bmi = weight / (height * height)
 return bmi


def weight_category (weight):
    if weight > 103:
        return ("Obese")
    elif weight >= 76 and weight <= 102:
        return ("Overweight")
    elif weight >= 65 and weight <= 75:
        return ("Normal weight")
    elif weight >= 55 and weight <= 64:
        return ("Underweight")
    else:
        return ("Malnourished")


def height_category (height):
 if height > 6.0:
    return ("Long")
 elif height >= 5.6 and height <= 5.9:
    return ("Tall")
 elif height >= 4.5 and height <= 5.5:
    return ("Medium")
 elif height >= 2.5 and height <= 4.5:
    return ("Short")
 else:
    return ("Dwarf")



#Gather input from user

students = 5
for i in range(students):
    weight = int(input("Enter weight for student in kilogram : "))
    height = int(input("Enter height for student in meter : "))

    print ("bmi =", calculate_bmi(weight, height))
    print ("weight_category =",  weight_category(weight))
    print ("height_type =", height_category(height))

    print("Student {i + 1} - BMI: weight / (height * height), Weight category: {weight_category}, Height category: {height_category}")