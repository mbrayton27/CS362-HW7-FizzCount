def print_count():
    stri = ""
    for x in range(1,101):
        if ((x % 3) == 0) and ((x%5) == 0):
            print ("FizzBuzz", end = '')
            stri += "FizzBuzz"
        elif x % 5 == 0:
            print ("Buzz", end = "")
            stri += "Fizz"
        elif x % 3 == 0:
            print ("Fizz", end = "")
            stri += "Buzz"
        else:
            print (x, end = "")
            stri += str(x)
    return stri
