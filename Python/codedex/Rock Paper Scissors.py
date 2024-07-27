import random

def get_cpu_move():
    moves = ['R', 'P', 'S']
    return random.choice(moves)

print("Rock, Paper, Scissors\n")
print("Please choose (R)ock, (P)aper or (S)cissors\n")

# Asking the player to make a move and upper() lets you use lowercase and uppercase
# The outcome will be the same

player_1 = input("Player one, make your move\n").upper()
player_2 = get_cpu_move()

# Display CPU's move
print(f"CPU made its move: {player_2}")

# All the possible combinations are indicated below
if player_1 == "R":
    if player_2 == "R":
        print("It's a draw!")
    elif player_2 == "S":
        print("Player 1 wins because they used Rock and the CPU used Scissors")
    elif player_2 == "P":
        print("Player 1's Rock loses because the CPU used Paper!")
    else:
        print("Invalid move by the CPU!")
elif player_1 == "P":
    if player_2 == "R":
        print("Player 1 wins because they used Paper and the CPU used Rock!")
    elif player_2 == "S":
        print("Player 1 loses because they used Paper against the CPU's Scissors!")
    elif player_2 == "P":
        print("It's a draw!")
    else:
        print("Invalid move by the CPU!")
elif player_1 == "S":
    if player_2 == "R":
        print("The CPU wins because it used Rock and Player 1 used Scissors")
    elif player_2 == "S":
        print("It's a draw!")
    elif player_2 == "P":
        print("Player 1 wins because they used Scissors against the CPU's Paper!")
    else:
        print("Invalid move by the CPU!")
else:
    print("Invalid move by Player 1!")
