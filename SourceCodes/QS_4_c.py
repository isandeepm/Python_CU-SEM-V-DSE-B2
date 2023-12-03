if __name__ == '__main__':
    print("OUTPUT-1")
    numbers = [1, 2, 3, 4]
    words = ['pineapple', 'banana', 'orange', 'mango']
    print("List of input words:", words)
    print("Input number list: ", numbers)
    # Without the key function
    print("Without key function:")
    print("Sum", sum(numbers))
    print("Minimum", min(words))
    print("Maximum", max(words))
    print("Sorted list", sorted(words))
    # With the key function
    print("With key function:")
    print("Sum", sum(numbers, key=lambda x: x**2))
    print("Minimum", min(words, key=lambda x: len(x)))
    print("Maximum", max(words, key=lambda x: len(x)))
    print("Sorted list", sorted(words, key=lambda x: len(x)))
    print("OUTPUT-2")
    numbers = [5, 7, 2, 4]
    words = ['litchi', 'apple', 'cucumber', 'date']
    print("List of input words:", words)
    print("Input number list: ", numbers)
    # Without the key function
    print("Without key function:")
    print("Sum", sum(numbers))
    print("Minimum", min(words))
    print("Maximum", max(words))
    print("Sorted list", sorted(words))
    # With the key function
    print("With key function:")
    print("Sum", sum(numbers, key=lambda x: x**2))
    print("Minimum", min(words, key=lambda x: len(x)))
    print("Maximum", max(words, key=lambda x: len(x)))
    print("Sorted list", sorted(words, key=lambda x: len(x)))