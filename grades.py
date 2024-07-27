try:
    # Vraag de gebruiker om hun cijfer
    grade = float(input("Voer uw cijfer in (tussen 0 en 100): "))
    
    # Controleer of het cijfer binnen het bereik van 0 tot 100 ligt
    if 0 <= grade <= 100:
        if grade >= 55:
            print("Je bent geslaagd!")
        else:
            print("Je bent gezakt.")
    else:
        print("Ongeldig cijfer. Voer een waarde tussen 0 en 100 in.")
except ValueError:
    print("Ongeldige invoer. Voer een getal in.")