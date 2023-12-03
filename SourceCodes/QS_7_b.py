while True:
    text = input("Enter a sentence: ")
    
    # for word count
    word_counts = {}
    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    print(word_counts)
    
    # for letter count
    letter_counts = {}
    for letter in text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    print(letter_counts)
    
    ch = int(input("Do you want to insert again?[1-yes/0-no]: "))
    if ch == 0:
        break
