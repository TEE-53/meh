f=open("CSlab.txt", 'r')
content=f.read()
vowels=0
consonants=0
lowercase=0
uppercase=0
for ch in content:
    if ch in 'aeiouAEIOU':
        vowels=vowels+1
    if ch in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        consonants=consonants+1
    if ch.islower():
        lowercase=lowercase+1
    if ch.isupper():
        uppercase=uppercase+1
f.close()
print("The no. of vowels is: ", vowels)
print("The no. of consonants is: ", consonants)
print("The no. of lowercase letters is: ", lowercase)
print("The no. of uppercase letters is: ", uppercase)