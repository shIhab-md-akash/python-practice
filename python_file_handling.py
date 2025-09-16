try :
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file was not found.")

finally:
    if 'file' in locals():
        file.close()

# This code attempts to open and read a file named "example.txt".

