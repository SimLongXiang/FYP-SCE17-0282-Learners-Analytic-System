import math
 
number_list = [10,-5,1.2,'apple']
 
for number in number_list:
    try:
        number_factorial = math.factorial(number)
    except TypeError:
        print("Factorial is not supported for given input type.")
    except ValueError:
        print("Factorial only accepts positive integer values.", number," is not a positive integer.")
    else:
        print("The factorial of",number,"is", number_factorial)
    finally:
        print("Release any resources in use.")
