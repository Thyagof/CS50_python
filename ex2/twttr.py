def main():
    s = input("Input: ")
    print("Output:", remove_vowel(s))

def remove_vowel(s):
    only_consonants = ""
    for c in s:
        if (c != "a" and c != "A"
            and c != "e" and c != "E" 
            and c != "i" and c != "I" 
            and c != "o" and c != "o" 
            and c != "u" and c != "U"):
            only_consonants += c
    return only_consonants
        
if __name__ == "__main__":
    main()