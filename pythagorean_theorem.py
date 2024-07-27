def pythagoras(a, b):
    # Bereken het kwadraat van de lengtes van de zijden
    a_squared = a ** 2
    b_squared = b ** 2
    
    # Bereken de som van de kwadraten
    sum_of_squares = a_squared + b_squared
    
    # Neem de wortel om de lengte van de hypotenusa te vinden
    c = sum_of_squares ** 0.5
    
    return c

# Voorbeeldgebruik
a = 3
b = 4
c = pythagoras(a, b)
print("De lengte van de hypotenusa is:", c)