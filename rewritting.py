f1=open("CSlab.txt", 'r')
f2=open("New.txt", 'w')
s=f1.readlines()
for i in s:
    if i[0]=='C' or i[0]=='c':
        f2.write(i)
print("Written successfully")
f1.close()
f2.close()