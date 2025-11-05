# main.py
def caesar_encrypt(text, shift):
    result = ""
    char = ''
    for i in text:
        if i.isalpha() and i.islower():
            char = chr(range(ord('a'), ord('z') + 1)[(ord(i) - ord('a') + shift) % 26])
        elif i.isalpha() and i.isupper():
            char = chr(range(ord('A'), ord('Z') + 1)[(ord(i) - ord('A') + shift) % 26])
        else:
            char = i
        result += char
    return result

if __name__ == "__main__":
    original_text = "hello world"
    encrypted_text = caesar_encrypt(original_text, 3)
    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}") # Expected: "khoor zruog"