def do_sum(a, b):
 return a + b
def do_mul(a, b):
 return a * b
def do_sub(a, b):
    return a - b

def do_gcd(a, b):
    min_num = a if a < b else b
    res = 1
    for i in range(1, min_num + 1):
        if a % i == 0 and b % i == 0:
            res = i
    return res

if __name__ == '__main__':
    x = int(input("Enter num1: "))
    y = int(input("Enter num2: "))
    while True:
        print("\nSum: 1\tProduct: 2\tDifference: 3\tGCD: 4\tExit: 0")
        c = int(input("Enter your choice: "))
        if c == 1:
            print("Sum:", do_sum(x, y))
        elif c == 2:
            print("Product:", do_mul(x, y))
        elif c == 3:
            print("Difference:", do_sub(x, y))
        elif c == 4:
            print("GCD:", do_gcd(x, y))
        elif c == 0:
            break
        else:
            print("Enter valid choice!")
