name = input("What is your name? ")
height_m = float(input("What is your height in meters? "))
weight_kg = float(input("What is your weight in KG? "))

height_squared = height_m * height_m
bmi = weight_kg / height_squared

print(name, "Your BMI is", f"{bmi:.2f}")
