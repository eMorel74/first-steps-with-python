# Eric Morel
# Currently taking a Python Certification, started last december 23th 2024
# my first program
#
# check if entered value is not numeric,
# then if condition it's true
# it instructs the user to try again
def check_input_value(val):
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return check_input_value(input("Must be a numeric value. Please try again "))


#ask the user if it continues using the program or not
def action():
    action = input("Would you like to continue calculating? (Y / N) ")

    if action == "Y":
        main()
    elif action == "N":
        return
    else:
        input("Use a valid answer. Try again, would you like to continue calculating? (Y / N) ")


#select between operations
def select_operation(op):
    match op:
        case "D":
            print("\nOperation selected: Division\n")

            x = check_input_value(input("Being x the dividend, what's x? "))
            y = check_input_value(input("Being y the divisor, what's y? "))
            z = x / y

            if z == int(z):
                print(f"\nThe result of divide {x} into {y} is: " + f"{int(z):,}" + "\n")
            else:
                print(f"\nThe result of divide {x} into {y} is: " + f"{z:,.2f}" + "\n")


            action()
        case "M":
            print("\nOperation selected: Multiplication\n")

            x = check_input_value(input("Being x the multiplicand, what's x? "))
            y = check_input_value(input("Being y the multiplier, what's y? "))
            z = x * y

            if z == int(z):
                print(f"\nThe result of multiply {x} by {y} is: " + f"{int(z):,}" + "\n")
            else:
                print(f"\nThe result of multiply {x} by {y} is: " + f"{z:,.2f}" + "\n")


            action()
        case "A":
            print("\nOperation selected: Addition\n")

            x = check_input_value(input("Being x the first addend, what's x? "))
            y = check_input_value(input("Being y the second addend, what's y? "))
            z = x + y

            if z == int(z):
                print(f"\nThe result of adds {x} to {y} is: " + f"{int(z):,}" + "\n")
            else:
                print(f"\nThe result of adds {x} to {y} is: " + f"{z:,.2f}" + "\n")


            action()
        case "S":
            print("\nOperation selected: Substraction\n")

            x = check_input_value(input("Being x the minuend, what's x? "))
            y = check_input_value(input("Being y the subtrahend, what's y? "))
            z = x - y

            if z == int(z):
                print(f"\nThe result of substract {y} from {x} is: " + f"{int(z):,}" + "\n")
            else:
                print(f"\nThe result of substract {y} from {x} is: " + f"{z:,.2f}" + "\n")


            action()
        case "E":
            print("\nOperation selected: Exponentiation\n")

            x = check_input_value(input("Being x the base, what's x? "))
            y = check_input_value(input("Being y the exponent, what's y? "))
            z = pow(x, y)

            if z == int(z):
                print(f"\nThe result of {x} to the power of {y} is: " + f"{int(z):,}" + "\n")
            else:
                print(f"\nThe result of {x} to the power of {y} is: " + f"{z:,.2f}" + "\n")


            action()
        case _:
            return select_operation(input("Select a valid operation. Please try again "))


#starts the program
def main():
    #gives the user the instruction to selects the operation it intends to use
    print("\nPlease select an operation: \nD is for division\nM is for multiplication\nA is for addition\nS is for substraction\nE is for exponentiation\n")

    #ask the user to select whitch operation would like to try
    result = select_operation(input("Whitch operation would you like to try? "))


main()
