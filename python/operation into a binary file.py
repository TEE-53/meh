import pickle

def create():

    f = open("shoes.dat", 'ab')
    opt = 'y'
    while opt == 'y':
        s_id = input("What is the s_id of the shoe: ")
        name = input("What is the name of the shoe: ")
        brand = input("What is the brand  of the shoe: ")
        type = input("What is the type  of the shoe: ")
        price = input("What is the price of the shoes: ")
        l = [s_id, name, brand, type, price]

        pickle.dump(l, f)
        opt = input("Do you want to add another Shoe detail [y/n]: ")
    f.close()

def disp():
    f = open("shoes.dat", 'rb')
    try:
        while True:
            s = pickle.load(f)
            print(s)
    except:
        f.close()




def search():
    f = open("shoes.dat", 'rb')
    s_id = input("What is the s_id of the shoe you want to search: ")
    found = 0
    try:
        while True:
            s = pickle.load(f)
            if s[0] == s_id:
                print("The searched s_id is found and Details are:", s)
                found = 1
                break
    except:
        f.close()

    if found == 0:
        print("The searched s_id is not found")

while True:
    print('''
To Add a record, please press 1 
To Display the Records, please press 2
To Search the Records, please press 3
To Exit, please press 4''')

    choice = int(input("\nOption: "))

    if choice == 1:
        create()
    elif choice == 2:
        disp()
    elif choice == 3:
        search()
    elif choice == 4:
        print("Thank you")
        break

