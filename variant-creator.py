
print('Name Variant Creator')


def variant_creator(name):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v'
        , 'w', 'x', 'y', 'z']

    variations = []

    # Replaced all instances of a letter with another in the alphabet.
    replaced_letter = []
    for character in name:
        for letter in alphabet:
            replaced_letter.append(name.replace(character, letter))
            variations.append(name.replace(character, letter))

    # Remove one character from name iteratively.
    removedLetter = []
    fromLeftRL = -1
    fromRightRL = 0
    for character in name:
        fromLeftRL = fromLeftRL + 1
        fromRightRL = fromRightRL + 1
        removedLetter.append(name[:fromLeftRL] + name[fromRightRL:])
        variations.append(name[:fromLeftRL] + name[fromRightRL:])

    # Add one character to name iteratively.
    addedLetter = []
    fromLeftAL = -1
    fromRightAL = -1
    for character in name:
        fromLeftAL = fromLeftAL + 1
        fromRightAL = fromRightAL + 1
        for letter in alphabet:
            addedLetter.append(name[:fromLeftAL] + letter + name[fromRightAL:])
            variations.append(name[:fromLeftAL] + letter + name[fromRightAL:])
            # to include a letter at the end of the name
            addedLetter.append(name + letter)
            variations.append(name + letter)

    # Substitute one character to name iteratively.
    substituteLetter = []
    fromLeftSL = -1
    fromRightSL = 0
    for character in name:
        fromLeftSL = fromLeftSL + 1
        fromRightSL = fromRightSL + 1
        for letter in alphabet:
            substituteLetter.append(name[:fromLeftSL] + letter + name[fromRightSL:])
            variations.append(name[:fromLeftSL] + letter + name[fromRightSL:])

    # Swap adjacent characters iteratively.
    swapped_letters = []
    from_left_sl = -1
    from_right_sl = 1
    next_character = 0
    for character in name:
        if next_character < len(name)-1:
            next_character = next_character + 1
            character_b = name[next_character]
            from_left_sl = from_left_sl + 1
            if from_left_sl == 0:
                from_right_sl = 2
                swapped_letters.append(character_b + character + name[from_right_sl:])
                variations.append(character_b + character + name[from_right_sl:])
            else:
                from_right_sl = from_right_sl + 1
                swapped_letters.append(name[:from_left_sl] + character_b + character + name[from_right_sl:])
                variations.append(name[:from_left_sl] + character_b + character + name[from_right_sl:])

    return variations

if __name__ == '__main__':

    print('Type in a screen name to create name variants. Press enter twice when finished.')
    while True:
        rawInput = input()
        if rawInput == '':
            break
        name = rawInput

    variations = variant_creator(name)

    countOfVariations = 0
    # from https://www.w3schools.com/python/python_howto_remove_duplicates.asp to remove duplicates efficiently
    variations = list(dict.fromkeys(variations))
    for word in variations:
        countOfVariations = countOfVariations + 1
        print(word)
    print(countOfVariations)


