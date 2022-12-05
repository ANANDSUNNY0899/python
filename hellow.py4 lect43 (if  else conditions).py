winning_number = 27
user_input = int(input("enter a number b/w 1 and 100 "))
if winning_number == user_input:
    print("YOU WIN !!!!")
else: #nested if else
    if user_input < winning_number:
       print("too low")
    if user_input >  winning_number:
       print("too high")        
            