def calcluse():
    try:
        firstNumber = float(input("first number is:"))
        symbol = input("symbol is:")
        secondNumber = float(input("the second number is:"))

        def summation():
            result = firstNumber + secondNumber
            if result.is_integer():
                print("The result of the summation is:", int(result))
            else:
                print("The result of the summation is:", result)
            calcluse()

        def multiply():
            result = firstNumber * secondNumber
            if result.is_integer():
                print("The result of the multiplication is:", int(result))
            else:
                print("The result of the multiplication is:", result)
            calcluse()

        def division():
            result = firstNumber / secondNumber
            if result.is_integer():
                print("The result of the division is:", int(result))
            else:
                print("The result of the division is:", result)
            calcluse()

        def subtraction():
            result = firstNumber - secondNumber
            if result.is_integer():
                print("The result of the subtraction is:", int(result))
            else:
                print("The result of the subtraction is:", result)
            calcluse()

        if symbol == "*":
            multiply()
        elif symbol == "+":
            summation()
        elif symbol == "-":
            subtraction()
        elif symbol == "/":
            division()
        else:
            print("please insert a valid symbol!")
            calcluse()

    except (ValueError, TypeError):
        print("please check your numbers")
        calcluse()


calcluse()
