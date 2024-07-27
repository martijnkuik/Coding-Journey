height = int(input("Whats your height "))
credits = int(input("Please pay "))

if height >= 137 and credits != 10:
  print("Enjoy the ride")

elif height <= 137 and credits !=10:
  print("Your not tall enough to ride")
elif height >= 137 and credits <= 10:
  print("You dont have enough credits")
else:
    print("you are to short and haven't have enough credits")
