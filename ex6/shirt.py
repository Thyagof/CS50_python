import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    overlay_image()

def overlay_image():
    check_command_line_arg()
    try:
        photo = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")
    
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo_resized = ImageOps.fit(photo, size)
    photo_resized.paste(shirt, shirt)
    photo_resized.save(sys.argv[2])

def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    file_input = splitext(sys.argv[1])
    file_output = splitext(sys.argv[2])

    if check_extension(file_input[1]) == False:
        sys.exit("Invalid input") 

    if check_extension(file_output[1]) == False:
        sys.exit("Invalid output")

    if file_input[1].lower() != file_output[1].lower():
        sys.exit("Input and output have different extensions")

def check_extension(file):
    return file in [".jpg", ".jpeg", ".png"]

if __name__ == "__main__":
    main()