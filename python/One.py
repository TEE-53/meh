f=open("Vaasavi.txt","r")
content = f.readlines()
for i in content:
    if i[0] in "vV":
        print(i)
f.close()