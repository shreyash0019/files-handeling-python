try:
    filename = input("Enter file name to view its content: ")
    with open("one.data", "r") as fp:
        filedata = fp.read()
        print("-"*50)
        print("Content of File : ")
        print(filedata)
        print("-"*50)
except FileNotFoundError:
    print("File Does not Exist !! ")
