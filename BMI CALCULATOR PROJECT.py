# Define function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Initialize variables
total_bmi = 0

# Loop to iterate through users' data
for i in range(2):
    print(f"Student {i+1}:")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in m: "))
    bmi = calculate_bmi(weight, height)
    total_bmi += bmi

    # If/elif conditions to determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif bmi >= 30:
        category = "Obese"
    else:
        category = "Invalid BMI"

    print(f"BMI: {bmi:.2f}, Category: {category}\n")

# Print the sum of BMIs for the two users
print(f"Sum of BMIs: {total_bmi:.2f}")

# Subtract function to calculate the difference between two BMIs
def subtract_bmi(bmi1, bmi2):
    difference = bmi1 - bmi2
    return difference

# Get the BMIs for subtraction
bmi1 = float(input("Enter the first BMI number: "))
bmi2 = float(input("Enter the second BMI number: "))

# Calculate the difference between the BMIs
subtraction_result = subtract_bmi(bmi1, bmi2)

print(f"Difference between BMIs: {subtraction_result:.2f}")

# Determine if a given BMI number is even or odd
bmi_num = float(input("Enter a BMI number: "))
if bmi_num % 2 == 0:
    print("Even")
else:
    print("Odd")