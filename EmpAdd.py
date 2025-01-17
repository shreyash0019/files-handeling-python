import pickle


def saverecord():
    with open("employee.pick","ab") as fp:
        while(True):
            try:
                print("-"*50)
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
                print("Employee Details Successfully Saved To Record !")
                Print("_"*50)
                ch=input("Do You Want To Add More Details ? (yes/no): ")
                if(ch.lower()=="no"):
                    print("Thanks For Using This Program")
                    break
            except ValueError:
                print("Don't Enter Alnums, Str, Special Symbols for Emp-id and Emp-sal")


