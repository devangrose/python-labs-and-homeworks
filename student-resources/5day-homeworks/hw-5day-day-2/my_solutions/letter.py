def letter_counter(string):
    to_return = {}
    for letter in string: 
        if letter in to_return:
            to_return[letter] += 1
        else:
            to_return[letter] = 1
    return to_return

print(letter_counter('banana'))
