try:
    filename = input("Enter Any File: ")
    nl=0
    nw=0
    nc=0
    with open ("wap","r")as fp:
        filedata = fp.readlines()
        for line in filedata:
            nl=nl+1
            nw=nw+len(line.split())
            nc=nc+len(line)
        else:
            print("-"*50)
            print("Number of lines = {}".format(nl))
            print("Number of words = {}".format(nw))
            print("Number of chars = {}".format(nc))
            print("-"*50)
except FileNotFoundError:
    print("File Does Not Exist")