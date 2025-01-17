sno = 11
sname = "WAWSSuUpp"
marks = 69.96
with open ("wap","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written Successfully..!")