import sys
from pyfiglet import Figlet

def main():

    if len(sys.argv) == 1:
        font_name = None
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font_name = sys.argv[2]
    else:
        print("Invalid usage")
        sys.exit(1)

    figlet = Figlet(font=font_name)

    user_input = input("Input: ")

    output_text = figlet.renderText(user_input)
    print("Output:", output_text)

if __name__ == "__main__":
    main()
