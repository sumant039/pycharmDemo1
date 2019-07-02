dictFile={}
f=open("C:/Users/Asus/Documents/GitHub/pycharmDemo1/etc/server.cfg",'r')
lines=f.readlines()
for line in lines:
    print(line.split(" "))
    lineFile=line.split(" ")
    print(lineFile[0])
    print(lineFile[1])
    dictfile[lineFile[0]]=lineFile[1]



for key,value in dictFile.items():
    print(key)
    print(value)