
from EmpMenu import menu
from EmpAdd import saverecord
from EmpSearch import searchemployee
from EmpView import viewallemployees, viewemployee
while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                saveemprecord()
            case 2:
                viewallemployees()
            case 3:
                viewemployee()
            case 4:
                searchemployee()


            case 7:
                print("Thx for this Project")
                break
            case _:
                print("Ur Selection of Operation is wrong-Try again")
    except ValueError:
        print("Don't enter strs, symbols and alnums for choice-try again")