def calculate_bmi(height_cm, mass):
    # Converteer lengte van centimeters naar meters
    height_m = height_cm / 100
    
    # Bereken de BMI met de formule: BMI = mass / (height ** 2)
    bmi = mass / (height_m ** 2)
    return bmi

# Vraag de gebruiker om lengte (in centimeters) en gewicht (in kilogram) in te voeren
while True:
    try:
        height_cm = float(input("Enter your height in centimeters: "))
        mass = float(input("Enter your weight in kilograms: "))
        break
    except ValueError:
        print("Please enter valid numbers for height and weight.")

# Bereken de BMI met behulp van de functie en druk het afgeronde resultaat af
bmi = calculate_bmi(height_cm, mass)
rounded_bmi = round(bmi, 2)  # Rond af tot 2 decimalen
print("Your BMI is:", rounded_bmi)