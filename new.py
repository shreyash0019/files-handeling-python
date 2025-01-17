try:
    with open("one.data", "a") as fp:
        print("-"*50)
        print("file opened successfully ")
        print("-"*50)
        sno = (int(input("Enter Student Number: ")))
        sname = input("Enter Student Name: ")
        smarks = int(input("Enter Student Marks: "))
        fp.write(str(sno)+"\t")
        fp.write((sname)+"\t")
        fp.write(str(smarks)+"\t")
        print("Data written successfully !")
        print("-"*50)
except FileExistsError:
    print("File already exist !")
