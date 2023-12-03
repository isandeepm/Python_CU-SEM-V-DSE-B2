if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("OUTPUT-1")
    print("Input list: ", numbers)
    odd_numbers = [x for x in numbers if x % 2 == 1]
    print("Odd numbers in list", odd_numbers)
    numbers_divisible_by_3 = [x for x in numbers if x % 3 == 0]
    print("Numbers divisible by 3 in list", numbers_divisible_by_3)
    print("OUTPUT-2")
    numbers = [5, 6, 10, 2, 12, 9, 4, 21, 7, 1]
    print("Input list: ", numbers)
    odd_numbers = [x for x in numbers if x % 2 == 1]
    print("Odd numbers in list", odd_numbers)
    numbers_divisible_by_3 = [x for x in numbers if x % 3 == 0]
    print("Numbers divisible by 3 in list", numbers_divisible_by_3)
