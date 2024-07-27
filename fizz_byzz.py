# Loop door de getallen van 1 tot en met 100
for i in range(1, 101):
    # Check of het getal een veelvoud is van zowel 3 als 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  # Als dat zo is, print "FizzBuzz"
    # Check of het getal een veelvoud is van 3
    elif i % 3 == 0:
        print("Fizz")  # Als het een veelvoud van 3 is, print "Fizz"
    # Check of het getal een veelvoud is van 5
    elif i % 5 == 0:
        print("Buzz")  # Als het een veelvoud van 5 is, print "Buzz"
    # Als het getal geen veelvoud is van 3 of 5, print het getal zelf
    else:
        print(i)  # Anders print je gewoon het getal






""""Uitleg!:

1. **`for i in range(1, 101):`**
   - **Commentaar:** Dit loopt door de getallen 1 tot en met 100. `range(1, 101)` zorgt daarvoor.

2. **`if i % 3 == 0 and i % 5 == 0:`**
   - **Commentaar:** Checkt of `i` een veelvoud is van zowel 3 als 5. De `%` operator geeft de rest bij deling, dus als de rest 0 is, is het een veelvoud.
   - **Actie:** Print "FizzBuzz" als het getal voldoet aan beide voorwaarden.

3. **`elif i % 3 == 0:`**
   - **Commentaar:** Als het getal alleen een veelvoud van 3 is.
   - **Actie:** Print "Fizz".

4. **`elif i % 5 == 0:`**
   - **Commentaar:** Als het getal alleen een veelvoud van 5 is.
   - **Actie:** Print "Buzz".

5. **`else:`**
   - **Commentaar:** Als het getal geen veelvoud van 3 of 5 is.
   - **Actie:** Print het getal zelf.

Hopelijk maakt dit het duidelijker en makkelijker te volgen!""" 