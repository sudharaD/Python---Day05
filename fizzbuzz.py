for number in range(1, 101):
    if number % 3 != 0 and number % 5 != 0:
        print(number)
    # elif number % 3 == 0 and number % 5 == 0:
    #     print("FizzBuzz")
    # elif number % 3 == 0:
    #     print("Fizz")
    # elif number % 5 == 0:
    #     print("Buzz")
    
    else:
        if number % 3 == 0:
            if number % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        else:
            print("Buzz")

    # if number % 3 == 0:
    #     if number % 5 == 0:
    #         print("FizzBuzz")
    #     else:
    #         print("Fizz")
    # elif number % 5 == 0:
    #     print("Buzz")
    # else:
    #     print(number)
    