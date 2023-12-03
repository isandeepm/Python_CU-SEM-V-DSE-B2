if __name__ == '__main__':
    while True:
        str1 = input("Enter the 1st string: ")
        str2 = input("Enter the 2nd string: ")
        print("\n", str1 * 2)
        print("\n", str2 * 3)
        ch = int(input("Do you want to insert again?[1-yes/0-no]: "))
        if ch == 0:
            break
