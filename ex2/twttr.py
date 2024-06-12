def main():
    s = input("Input: ")
    print("Output:", shorten(s))

def shorten(word):
    shortened = ""
    for l in word:
        if (l != "a" and l != "A"
            and l != "e" and l != "E" 
            and l != "i" and l != "I" 
            and l != "o" and l != "O" 
            and l != "u" and l != "U"):
            shortened += l
    return shortened
        
if __name__ == "__main__":
    main()