from random import choice

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIALS = "€$@%!?<>*"

def generate_password(length, lowerCase, upperCase, numbers, specials):
    characters = ""
    res = ""

    if lowerCase:
        characters += LOWERCASE

    if upperCase:
        characters += UPPERCASE

    if numbers:
        characters += NUMBERS

    if specials:
        characters += SPECIALS

    while length != 0:
        res += choice(characters)
        length -= 1

    return res