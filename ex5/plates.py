def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s): 
    if (
            check_start_letters(s) and
            check_len(s) and 
            check_punctuation(s) and 
            check_number_ending(s)
        ):
        return True
    else: 
        return False

def check_start_letters(s):
    return s[0:2].isalpha()

def check_len(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else: 
        return True

def check_punctuation(s):
    for c in s:
        match c: 
            case "!" | "." | "," | " " | "-" | ":":
                return False
    return True

def check_number_ending(s):
    first_number = False
    for c in s:
        if c.isnumeric() and int(c) == 0 and first_number == False:
            return False
        elif c.isnumeric() and int(c) != 0 and first_number == False:
            first_number = True
        elif first_number == True and c.isnumeric() == False:
            return False
    return True

if __name__ == "__main__":
    main()