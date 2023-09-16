def starts_with_two_letters(s):
    return s[:2].isalpha()

def meets_length_requirements(s):
    return 2 <= len(s) <= 6

def ends_with_number(s):
    if s[-1].isdigit():
        return not any(char.isdigit() for char in s[:-1])
    return False

def first_number_not_zero(s):
    return not s[0].isdigit() or s[0] == '0'

def contains_no_punctuation(s):
    return s.isalnum()

def is_valid(s):
    return (
        starts_with_two_letters(s) and
        meets_length_requirements(s) and
        ends_with_number(s) and
        first_number_not_zero(s) and
        contains_no_punctuation(s)
    )

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
