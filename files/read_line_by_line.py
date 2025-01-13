
f = open("/home/vinay/lab/pythonPlayground/py-upskill/files/textfile.txt")

line = f.readline()

while(line != ""):
    print(line)
    line = f.readline()

f.close()