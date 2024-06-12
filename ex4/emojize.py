import emoji

def main():
    text = input("Input: ").strip()
    emojize_text(text)

def emojize_text(t):
    print(emoji.emojize(t, language="alias"))
    

if __name__ == "__main__":
    main()