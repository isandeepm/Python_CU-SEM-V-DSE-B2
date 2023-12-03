def odd_even_strings(words):
    odd_string = ' '.join(words[1::2])
    even_string = ' '.join(words[::2])
    return (odd_string, even_string)

if __name__ == '__main__':
    print("OUTPUT-1")
    words = ['I', 'am', 'a', 'python', 'programmer']
    oddeven = odd_even_strings(words)
    print("Input list: ", words)
    print("Output tuple", oddeven)
    print("OUTPUT-2")
    words = ['I', 'am', 'a', 'computer', 'science', 'student']
    oddeven = odd_even_strings(words)
    print("Input list: ", words)
    print("Output tuple", oddeven)
