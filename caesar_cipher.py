import string

def caesar_cipher(text, shift, decrypt=False):
    if not text.isascii() or not text.isalpha():
        raise ValueError("Text must be ASCII and contain no numbers.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    result = ""

    if decrypt:
        shift = shift * -1

    for char in text:
        if char.islower():
            index = lowercase.index(char)
            result += lowercase[(index + shift) % 26]
        else:
            index = uppercase.index(char)
            result += uppercase[(index + shift) % 26]

    return result

if __name__ == "__main__":
    print(caesar_cipher("meetMeAtOurHideOutAtTwo", 10))
    print(caesar_cipher("woodWoKdYebRsnoYedKdDgy", 10, decrypt=True))
