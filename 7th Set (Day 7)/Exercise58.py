#Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is between 10 and 20, display “Correct”, otherwise display “Too high”. 

num = int(input("Please enter a number between 10 and 20 (inclusive): "))

if num <= 20 and num >= 10:
    print("Correct")

elif num < 10:
    print("Too low")

else:
    print("Too high")