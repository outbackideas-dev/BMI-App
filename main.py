name = input("What is your name? ")
height = float(input("What is your height in meters? "))
weight = int(input("What is your weight in KG? "))

KG = weight
M = height * height

total_BMI = KG / M

print(name, "Your BMI is", total_BMI)
