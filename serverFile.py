dictFile={}
f=open("C:/Users/Asus/Documents/GitHub/pycharmDemo1/etc/server.cfg",'r')
lines=f.readlines()
for line in lines:
    print(line.split(" "))
    lineFile=line.split(" ")
    lineFile[0].rstrip()
    lineFile[1].rstrip()
    print(lineFile[0])
    print(lineFile[1])
    dictFile[lineFile[0]]=lineFile[1]


print("print Key and Values  of Dict")
for key,value in dictFile.items():
    print(key)
    print(value)