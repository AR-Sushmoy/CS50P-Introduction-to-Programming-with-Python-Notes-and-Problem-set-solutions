def main():
    file_type = input("File name: ").lower().strip()

    if file_type[-4: ] == ".gif":
        print("image/gif")
    elif file_type[-5: ] == ".jpeg" or file_type[-4: ] == ".jpg":
        print("image/jpg")
    elif file_type[-4: ] == ".png":
        print("image/png")
    elif file_type[-4: ] == ".pdf":
        print("application/pdf")
    elif file_type[-4: ] == ".txt":
        print("document/txt")
 
main()