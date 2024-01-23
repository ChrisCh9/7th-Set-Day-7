#Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”. 

num = int(input("Please enter a number between 10 and 20 (inclusive): "))

if num <= 20 and num >= 10:
    print("Thank you")

else:
    print("Incorrect answer")