# Write code below 💖
# Ask for the amount in Pesos, Soles, and Reals
col_pes = int(input("What do you have left in Peso's? ")) 
per_sol = int(input("What do you have left in Soles? "))   
bra_rea = int(input("What do you have left in Real's? "))  

# Calculate the total amount in euro
euro = (col_pes * 0.00024) + (per_sol * 0.25) + (bra_rea * 0.18)

# Print the total amount rounded to two decimal places with the euro symbol before it
print("You have got €{:.2f}".format(euro))