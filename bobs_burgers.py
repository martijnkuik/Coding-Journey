class Restaurant:
  name = ''
  type = ''
  rating = 0.0
  delivery = False





bobs_burgers = Restaurant()
bobs_burgers.name = "Bob\'s Burgers"
bobs_burgers.type = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False


dutch_snack_attack = Restaurant()
dutch_snack_attack.name = "Dutch Snack Attack"
dutch_snack_attack.type = "Fastfood"
dutch_snack_attack.rating = 4.5
dutch_snack_attack.delivery = True    


bottemless_Pit = Restaurant()
bottemless_Pit.name = "Bottemless Pit"
bottemless_Pit.type = "Steakhouse"
bottemless_Pit.rating = 4.9
bottemless_Pit.delivery = True        

print(vars(bobs_burgers and dutch_snack_attack and bottemless_Pit))