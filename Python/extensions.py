#!/usr/bin/env python3
"""
Function takes a file name as input and returns the media type for that file based on its file extension
"""

def extension(file_name):
    name_and_ext = file_name.strip().lower().split(".")

    if len(name_and_ext) == 1:
        return "application/octet-stream"
    elif name_and_ext[-1] == "bin":
        return "application/octet-stream"
    elif name_and_ext[-1] == "gif":
        return "image/gif"
    elif name_and_ext[-1] == "jpg":
        return "image/jpg"
    elif name_and_ext[-1] == "jpeg":
        return "image/jpeg"
    elif name_and_ext[-1] == "png":
        return "image/png"
    elif name_and_ext[-1] == "pdf":
        return "application/pdf"
    elif name_and_ext[-1] == "txt":
        return "text/plain"
    elif name_and_ext[-1] == "zip":
        return "application/zip"


if __name__ == '__main__':
    for i in range(8):
        file_name = input("File mane: ")
        print(extension(file_name))
