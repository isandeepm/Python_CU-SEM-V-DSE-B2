# addition
def do_sum(a, b):
    return a + b

# subtraction
def do_sub(a, b):
    return a - b

# multiplication
def do_mul(a, b):
    return a * b

# division
def do_div(a, b):
    return a / b

# modulus
def do_mod(a, b):
    return a % b

# exponential
def do_expo(a, b):
    return a ** b

if __name__ == '__main__':
    print("Basic Calculator")
    print("----------------")
    x = int(input("Enter num 1: "))
    y = int(input("Enter num 2: "))
    while True:
        print("\nAddition: 1\tSubtraction: 2\tMultiplication: 3\tDivision: 4\tModulus: 5\tExponent: 6\tExit: 0")
        c = int(input("Enter your choice: "))
        if c == 1:
            print("\nAddition:", do_sum(x, y))
        elif c == 2:
            print("\nSubtraction:", do_sub(x, y))
        elif c == 3:
            print("\nMultiplication:", do_mul(x, y))
        elif c == 4:
            print("\nDivision:", do_div(x, y))
        elif c == 5:
            print("\nModulus:", do_mod(x, y))
        elif c == 6:
            print("\nExponent:", do_expo(x, y))
        elif c == 0:
            break
        else:
            print("\nEnter valid choice!")