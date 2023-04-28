import random
cnumber= random.randrange(1,101)
userInput= int(input("Enter the Number"))
if userInput>cnumber:
    print("Computer Number",cnumber)
    print("You are guessing high number")
elif cnumber>userInput:
    print("Computer Number",cnumber)
    print("Your guessing low number")
else:
    print("Computer number",cnumber)
    print("Your guess number is correct")
    