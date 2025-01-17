import pickle
def saveemprecord():
    with open("employee.pick","ab") as fp:
        while(True):
            try:
                print("="*50)
                empno=int(input("Enter Employee Number: "))
                empname=str(input("Enter Employee Name: "))
                empsal=float(input("Enter Employee Salary: "))
                dsg=str(input("Enter Employee Designation: "))
                print("-"*50)
                lst=[]
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                lst.append(dsg)
                pickle.dump(lst,fp)
                print("-"*50)
                print("Employee Record Saved In File")
                print("-"*50)
                ch=input("Do You Want To Insert Another Record (yes/no): ")
                if (ch.lower()=="no"):
                    print("Thanks For Using This Program..")
                    break
            except ValueError:
                print("Don't Enter alnums, Symbols, str for empno and salary")


saveemprecord()