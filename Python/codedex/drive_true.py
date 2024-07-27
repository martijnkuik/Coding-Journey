def get_item(snack):
    if snack == 1:
        return "Minced meat ball sandwich"  # A traditional Dutch sandwich made with minced meat balls.
    elif snack == 2:
        return "Picanto"  # A spicy sausage often served with bread or in a bun.
    elif snack == 3:
        return "Frikandel special"  # A deep-fried, skinless, minced meat sausage, typically served with mayonnaise, curry ketchup, and chopped onions.
    elif snack == 4:
        return "Kroket"  # A deep-fried snack made of a meat ragout (usually beef, veal, or chicken), covered in breadcrumbs.
    elif snack == 5:
        return "Stroopwafel"  # A waffle made from two thin layers of baked dough with a caramel-like syrup filling in the middle.
    else:
        return "Choose the right option"    

def welcome():
    print('Welcome to Dutch snack attack!')
    print('Please choose a snack:')
    print('1. Minced meat ball sandwich')  # A traditional Dutch sandwich made with minced meat balls.
    print('2. Picanto')  # A spicy sausage often served with bread or in a bun.
    print('3. Frikandel special')  # A deep-fried, skinless, minced meat sausage, typically served with mayonnaise, curry ketchup, and chopped onions.
    print('4. Kroket')  # A deep-fried snack made of a meat ragout (usually beef, veal, or chicken), covered in breadcrumbs.
    print('5. Stroopwafel')  # A waffle made from two thin layers of baked dough with a caramel-like syrup filling in the middle.

welcome()

option = int(input('Please choose from the menu? '))
print(get_item(option))
