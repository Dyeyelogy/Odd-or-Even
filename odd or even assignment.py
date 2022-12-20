number = int(input("Input Number: "))

if number > 0:
    if number%2 == 0:
        print("Number is Positve Even") 
    elif number%3 == 0:
        print("Number is Positive Odd")
elif number < 0:
    if number%2 == 0:
        print("Number is Negative Even") 
    elif number%3 == 0:
        print("Number is Negative Odd")
elif number == 0:
    print("Given is a Null number")
else:
    print("Invalid Number")