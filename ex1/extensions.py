def main():
    file_name = input("File name: ").strip().lower()
    print(define_media(file_name))

def define_media(file):
    if "." in file:
        extension = file.split(".")[-1]
    else:
        return "application/octet-stream"

    match extension:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

if __name__ == "__main__":
    main()
