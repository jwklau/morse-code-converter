# 1. TODO - Create Morse code dictionary
MORSE_CODE_DICT = {
    "A": "·-", "B": "-···", "C": "-·-·", "D": "-··", "E": "·", "F": "··-·", "G": "--·", "H": "····", "I": "··",
    "J": "·---", "K": "-·-", "L": "·-··", "M": "--", "N": "-·", "O": "---", "P": "·--·", "Q": "--·-", "R": "·-·",
    "S": "···", "T": "-", "U": "··-", "V": "···-", "W": "·--", "X": "-··-", "Y": "-·--", "Z": "--··",
    "0": "-----", "1": ".----", "2": "··---", "3": "···--", "4": "····-", "5": "·····", "6": "-····", "7": "--···",
    "8": "---··", "9": "----·",
    ".": "·-·-·-", ",": "--··--", "?": "··--··", "'": "·----·", "!": "-·-·--", "/": "-··-·", "(": "-·--·",
    ")": "-.--.-", ":": "---···", ";": "-·-·-·", "=": "-···-", "--": "-··-·", "-": "-····-", "+": "·-·-·",
    "_": "··--·-", '"': '·-··-·', "@": "·--·-·", "&": "·-···", "$": "···-··-",
}


# 4. TODO - Encrypt string to Morse code and return
def morse_converter(message):
    """' This function takes a message (string) to convert and returns a Morse code message' """
    converted_message = ""
    for char in message:
        if char != " ":
            # look up character in dictionary
            e_char = MORSE_CODE_DICT[char]
            # add space between each character
            converted_message += e_char + " "
        else:
            # 1 space indicates different characters
            # 2 spaces indicates different words
            converted_message += "  "
    return converted_message


# Morse code converter

should_continue = True

print("Welcome to the Text to Morse code converter! \n"
      "You can convert any message including numbers (0-9), and the following symbols: \n"
      '. (full stop), , (comma), ?, !, /, (, ), ", :, ;, +, -, =, --, _ (underscore), @, &, $')
while should_continue:
    # 2. TODO - User input for string to convert
    # 3. TODO - Convert string to UPPERCASE
    message = input("What message would you like to convert to Morse code?: \n").upper()

    morse_message = morse_converter(message)
    print(f"Here's your converted message: {morse_message} ")

    convert_again = input("Would you like to convert another message? Type 'yes' to continue or 'no' to exit: ").lower()

    if convert_again == "no":
        should_continue = False
        print("You got it, Handkerchief. Smell ya later.")

# 6. TODO - CHALLENGE - add audio return for encrypt function
