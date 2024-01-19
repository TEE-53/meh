def count():
    f=open("Mytext.txt","r")
    content = f.read()
    v=0
    cons=0
    upperch=0
    lowerch=0
    for ch in content:
        if ch.islower():
            upperch+=1
        elif ch.isupper():
            lowerch+=1
        ch=ch.lower()
        if ch in 'aeiou':
            v+=1
        elif ch in 'bcdfghjklmnpqrstvwxyz':
            cons+=1
    f.close()
    print("Vowels are : ",v)
    print("consonants are : ",cons)
    print("Lower case letters are : ",upperch)
    print("Upper case letters are : ",lowerch)

count()