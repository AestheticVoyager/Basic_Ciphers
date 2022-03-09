import string

def vigenere_cipher(text, key, decrypt=False):
    if not text.isascii() or not text.isalpha() or not text.isupper():
        raise ValueError("Text must be uppercase ASCII without numbers.")

    uppercase = string.ascii_uppercase
    results = ""

    for i, char in enumerate(text):
        current_key = key[i % len(key)]
        char_index = uppercase.index(char)
        key_index = uppercase.index(current_key)

        if decrypt:
            index = char_index - key_index + 26
        else:
            index = char_index + key_index

        results += uppercase[index % 26]

    return results

if __name__ == "__main__":
    print(vigenere_cipher(text="DOMIRSCIRE", key="MODULO"))
    encrypted = vigenere_cipher(text="DOMIRSCIRE", key="MODULO")
    print(encrypted)
    vigenere_cipher(encrypted, "MODULO", decrypt=True)
