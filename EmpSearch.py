import pickle
def searchemployee():
    try:
        with open("employee.pick","rb") as fp:
            empno = int(input("Enter Employee Number To view details: "))
            found = False
            while(True):
                try:
                    record=pickle.load(fp)
                    if(empno==record[0]):
                        found=True
                        emprrec=record
                        break
                except EOFError:
                    break
            if found == True:
                print("=" * 40)
                print("Employee Deatils")
                print("=" * 40)
                print("\tEmployee Number={}".format(record[0]))
                print("\tEmployee Name={}".format(record[1]))
                print("\tEmployee Salary={}".format(record[2]))
                print("\tEmployee Designation={}".format(record[3]))
                print("=" * 40)

    else:
            print("Employee Record Does not Exist")
            except FileNotFoundError:
            print("Employee File Does not Exist:")
    except FileNotFoundError:
        print("File Does not Exist")

