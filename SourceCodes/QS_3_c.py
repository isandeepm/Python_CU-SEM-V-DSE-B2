import re

if __name__ == '__main__':
    # Split the string at each space character
    words = re.split(r'\s+', 'I am a python programmer')
    print("split: ", words)

    # Join the words with a space character
    sentence = " ".join(['I', 'am', 'a', 'python', 'programmer'])
    print("join: ", sentence)

    # Search for the word 'python' in the string
    match = re.search(r'python', 'I am a python programmer')
    if match:
        print("found: ", match.group())
    else:
        print('Not found')

    # Match the start of the string with the word 'I'
    match = re.match('I am a ', 'I am a python programmer')
    if match:
        print("matched: ", match.group())
    else:
        print('Not found')

    # Split the string at each space character
    words = re.split(r'\s+', 'I am a computer science student')
    print("split: ", words)

    # Join the words with a space character
    sentence = " ".join(['I', 'am', 'a', 'computer', 'science', 'student'])
    print("join: ", sentence)

    # Search for the word 'science' in the string
    match = re.search(r'science', 'I am a computer science student')
    if match:
        print("found: ", match.group())
    else:
        print('Not found')

    # Match the start of the string with the word 'I'
    match = re.match('I', 'I am a computer science student')
    if match:
        print("matched: ", match.group())
    else:
        print('Not found')
