def omit_vowels(text):
    vowels = "AEIOUaeiou"
    text_without_vowels = ""

    for char in text:
        if char not in vowels:
            text_without_vowels += char

    return text_without_vowels

def main():
    user_input = input("Input: ")
    text_without_vowels = omit_vowels(user_input)
    print("Output:", text_without_vowels)

if __name__ == "__main__":
    main()
