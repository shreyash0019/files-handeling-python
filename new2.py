sno = 10
sname = "Rossum"
marks = 55.55
with open("one.data", "a")as fp:
    fp.write(str(sno) + "\t")
    fp.write(sname + "\t")
    fp.write(str(marks) + "\n")
    print("data written to file..!!!")
