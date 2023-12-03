import math

if __name__ == '__main__':
    while True:
        print("GCD: 1")
        print("Area & Perimeter of Circle: 2")
        print("Exit: 0")
        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            a = int(input("Enter num 1: "))
            b = int(input("Enter num 2: "))
            print("GCD: ", math.gcd(a, b))
            
        elif ch == 2:
            r = int(input("Enter the radius of the circle: "))
            print("Area: ", math.pi*r*r)
            print("Perimeter: ", math.pi*r*2)
            
        elif ch == 0:
            break
            
        else:
            print("Enter valid choice!")
