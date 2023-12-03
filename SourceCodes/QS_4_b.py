def gaussian_addition(numbers):
    n = len(numbers)
    result = 0
    for i in range(0, n, 2):
        partial_sum = numbers[i] + numbers[n-i-1]
        print(f"{numbers[i]} + {numbers[n-i-1]}")
        result += partial_sum
    return result
if __name__ == '__main__':
 # Test the function with an even-length list
 print("OUTPUT-1")
 print("for even number of numbers: ")
 print(gaussian_addition([1, 2, 3, 4, 5, 6]))
 print("\n")
 # Test the function with an odd-length list
 print("OUTPUT-2")
 print("for odd number of numbers: ")
 print(gaussian_addition([1, 2, 3, 4, 5]))