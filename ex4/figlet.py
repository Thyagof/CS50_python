import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        render_text()
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font" or invalid_font():
            sys.exit()
        else:
            render_text(sys.argv[2])
    else: 
        sys.exit()
        
def invalid_font():
    fonts = figlet.getFonts()
    return sys.argv[2] not in fonts

def render_text(f = random.choice(figlet.getFonts())):
    text = input("Input: ")
    figlet.setFont(font=f)
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
