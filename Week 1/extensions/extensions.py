def get_media_type(file_name):
    suffix = file_name.lower().split('.')[-1]

    image_suffixes = ['gif', 'jpg', 'jpeg', 'png']
    document_suffixes = ['pdf', 'zip']
    archive_suffixes = ['txt']

    if suffix in image_suffixes:
        return "image/" + suffix
    elif suffix in document_suffixes:
        return "application/" + suffix
    elif suffix in archive_suffixes:
        return "text/" + suffix
    else:
        return "application/octet-stream"

def main():
    file_name = input("File name: ")
    media_type = get_media_type(file_name)
    print(f"{media_type}")

if __name__ == "__main__":
    main()
