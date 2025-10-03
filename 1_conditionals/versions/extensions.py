file = input("File name: ").lower().strip()

if file.endswith(".jpg"):
    print("image/jpeg")
elif file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

"""
#Problem 3
def main():
    file_name = input("File name: ").lower().strip()
    print(media_types(file_name))

def media_types(m):
    if m.endswith(".gif"):
        return "image/gif"
    elif m.endswith(".jpg") or m.endswith(".jpeg"):
        return "image/jpeg"
    elif m.endswith(".png"):
        return "image/png"
    elif m.endswith(".pdf"):
        return "application/pdf"
    elif m.endswith(".txt"):
        return "text/plain"
    elif m.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()

# The above code works but the more robust code will be as follows:
def main():
    # 1. Get and clean the user's input
    file_name = input("File name: ").lower().strip()
    # 2. Call the function and print the result
    print(get_media_type(file_name))

def get_media_type(filename):
    # 3. Split the filename and get the last part (the extension)
    parts = filename.split('.')

    # Check if there is an extension
    if len(parts) > 1:
        extension = parts[-1] # Get the last item from the list

        # 4. Check the extension
        if extension == "gif":
            return "image/gif"
        elif extension == "jpg" or extension == "jpeg":
            return "image/jpeg"
        elif extension == "png":
            return "image/png"
        elif extension == "pdf":
            return "application/pdf"
        elif extension == "txt":
            return "text/plain"
        elif extension == "zip":
            return "application/zip"

    # 5. If no extension or no match, return the default
    return "application/octet-stream"

main()
"""
