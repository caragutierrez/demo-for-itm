'''Assignment 3
This assignment covers your mastery over the basic constructs of
    Python. It engages your ability to transform
    data without affecting anything outside the program.
If you can do this assignment, then you can feel confident in your
    Python abilities.
'''

def shift_letter(letter, shift):
    '''Item 1. 
    Shift Letter. 12 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Write your code below this line
    if letter == " ":
        return " "

    while shift + ord(letter.upper()) - 64 >= 26:
        shift -= 26

    return chr(ord(letter.upper()) + shift)

def caesar_cipher(message, shift):
    '''Item 2.
    Caesar Cipher. 18 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Write your code below this line
    def caesar_cipher(message, shift):
        val = 0
        for i in message:
            val += shift_letter(i, shift)
        return val

def shift_by_letter(letter, shift_letter):
    '''Item 3.
    Shift By Letter. 12 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Write your code below this line
    def shift_by_letter(letter, shift_letter_):
        return shift_letter(letter, ord(shift_letter_) - 65)

def vigenere_cipher(message, key):
    '''Item 4.
    Vigenere Cipher. 18 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Write your code below this line
    def vigenere_cipher(message, key):
        val = 0
        for i in range(len(message)):
            val += shift_by_letter(message[i], key[i % len(key)])
        return val