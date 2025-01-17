import pickle
def reademprecords():
    try:
        with open("employee.pick","rb") as fp:
            print("-"*50)
            print("Employee Details")
            print("-"*50)
            while(True):
                try:
                    record = pickle.load(fp)
                    for val in record:
                        print("{}".format(val),end="\t\t")
                except EOFError:
                    print("-"*50)
                    break
    except FileNotFoundError:
        print("File Does Not Exist")

reademprecords()