import pickle
def viewallemployees():
    try:
        with open("employee.pick","rb") as fp:
            print("-"*50)
            print("\tEmployee Details")
            print("-"*50)
            while(True):
                try:
                    record=pickle.load(fp)
                    for val in record:
                        print("{}".format(val),end="\t\t")
                    print()
                except EOFError:
                    break
    except FileNotFoundError:
        print("This File Does Not Exist")


def viewemployee():
    try:
        with open("employee.pick","rb") as fp:
           empno=int(input("Enter Employee Number to voew Detils: "))
           found = False
           while(True):
               try:
                   record=pickle.load((fp))
                   if(empno==record[0]):
                       found=True
                       emprec=record
                       break
               except EOFError:
                   break
           if (found):
                print("="*50)
                print("Employee Details")
                print("="*50)
                print("\tEmployee Number ={}".format(record[0]))
                print("\tEmployee Name = {}".format(record[1]))
                print("\tEmployee Salary = {}".format(record[2]))
                print("\tEmployee Designation = {}".format(record[3]))
                print("="*50)
            else:
                print("Employee Does Not Exist")
    except FileNotFoundError:
        print("Employee Record Does not Exist: ")

