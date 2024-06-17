def main():
    s = input("Input: ")
    print("Output:", shorten(s))

def shorten(word):
    shortened = ""
    for l in word:
        if l not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            shortened += l
    return shortened
        
if __name__ == "__main__":
    main()