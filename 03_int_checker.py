
while True:

    error = "Please enter an integer more than 13 or with out a decimal point."

    try:
        my_num = int(input("Enter an integer: "))

        if my_num < 13:
            print(error)

        print("your number is ", my_num)

    except ValueError:
        print(error)