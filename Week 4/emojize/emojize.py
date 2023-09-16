import emoji

def main():
    user_input = input("Input: ")
    emojized_text = emojize_text(user_input)
    print("Output:", emojized_text)

def emojize_text(text):
    return emoji.emojize(text, language='alias')

if __name__ == "__main__":
    main()
