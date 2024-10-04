
brailleAlphabeticDict = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......'
}

brailleNumberDict = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',}

brailleDecimalDict = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OO.O',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.O.O.O',
    '>': 'O.O.O.',
    '(': 'O.O..O',
    ')': '.O.OO.',

}


def toBraille(input):

    output = ""
    b,c = 0,0
    for c in input:
        if c.lower() in brailleAlphabeticDict:
            if c.isupper():
                output += ".....O" + brailleAlphabeticDict[c.lower()]
            else:
                output += brailleAlphabeticDict[c]

        if c in brailleNumberDict:
            if b==0:
                output += ".O.OOO" + brailleNumberDict[c]
                b=1
            elif b==1:
                output += brailleNumberDict[c]

        if c in brailleDecimalDict:
            if c == 0:
                output += ".O...O" + brailleDecimalDict[c]
                c=1
            if c == 1:
                output += brailleDecimalDict[c]

    return output

def fromBraille(brailleInput):
    brailleToAlphabeticDict = {v: k for k, v in brailleAlphabeticDict.items()}
    brailleToNumberDict = {v: k for k, v in brailleNumberDict.items()}
    brailleToDecimalDict = {v: k for k, v in brailleDecimalDict.items()}

    output = ""
    i = 0
    is_number_mode = False

    while i < len(brailleInput):
        # Check if the next character is a number indicator
        if brailleInput[i:i+6] == ".O.OOO":
            is_number_mode = True
            i += 6
        elif brailleInput[i:i+6] == ".....O":  # Uppercase indicator
            i += 6
            letter = brailleInput[i:i+6]
            if letter in brailleToAlphabeticDict:
                output += brailleToAlphabeticDict[letter].upper()
            i += 6
        else:
            symbol = brailleInput[i:i+6]
            if is_number_mode and symbol in brailleToNumberDict:
                output += brailleToNumberDict[symbol]
            elif not is_number_mode and symbol in brailleToAlphabeticDict:
                output += brailleToAlphabeticDict[symbol]
            elif symbol in brailleToDecimalDict:
                output += brailleToDecimalDict[symbol]
            i += 6

        # Reset number mode if the next symbol is not a number
        if i < len(brailleInput) and brailleInput[i:i+6] not in brailleToNumberDict:
            is_number_mode = False

    return output


if __name__ == "__main__":
    # toB = " ".join(sys.argv[1:])
    # toB = "42"
    # toB = "Hello world"
    toB = "Abc 123"


    braille_output = fromBraille(toBraille(toB))

    print(braille_output)
    print(toB)


    # Verification for Hello world
    # print(".O.OOOOO.O..O.O...")
    # print(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")
    # print(".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")

    # fromB = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."  # Example
    # braille_input_string = ".O.OOOOO.O..O.O..."  # Example
    # braille_input_string = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."  # Example

    # text_output = toBraille(fromBraille(fromB))
    # print(fromB)
    # print(text_output)


