def calculate_bmi(height_m, weight_kg):
    if height_m <= 0:
        raise ValueError("Height must be greater than 0.")

    height_squared = height_m * height_m
    return weight_kg / height_squared


def main():
    name = input("What is your name? ")

    try:
        height_m = float(input("What is your height in meters? "))
        weight_kg = float(input("What is your weight in KG? "))
        bmi = calculate_bmi(height_m, weight_kg)
    except ValueError as error:
        if str(error).startswith("could not convert string to float"):
            print("Height and weight must be numeric values.")
        else:
            print(error)
        return

    print(name, "Your BMI is", f"{bmi:.2f}")


if __name__ == "__main__":
    main()
