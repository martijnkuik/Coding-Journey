
# the print function prints out the text given between the  parentheses
print("This is the first build in function")

#The input function takes input from the user. Whatever you enter as input, the input function converts it into a string
dry = input("what does D.R.Y mean\n").capitalize()
if dry == "Dont repeat yourself":
    print("Thats correct")
else:
    print("thats not the anwser I was looking for")

#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
for i in range(6):
    print(i)

#The int function returns the type of data stored in the objects or variables in the program
name=12345
print(type(name))

# the complex() function creates a complex number, which has both a real part and an imaginary part.The j comes behind the imaginary part
x = complex(3, 5)
print(x)