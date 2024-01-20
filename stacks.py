def push():
    doc_ID=int(input("Enter the doctor's ID: "))
    doc_name=input("Enter the doctor's name: ")
    spl=input("Enter the doctor's specialization: ")
    if spl == 'ENT':
        stack.append([doc_ID, doc_name])

def pop():
    if stack==[]:
        print("The stack is empty")
    else:
        print("The deleted element is: ", stack.pop())

def peek():
    if stack==[]:
        print("The stack is empty")
    else:
        top=len(stack)-1
        print("The element at the top of the stack is: ", stack[top])

def disp():
    if stack == []:
        print("The stack is empty")
    else:
        top=len(stack)-1
        for i in range(top, -1, -1):
            print(stack[i])

stack=[]
ch='y'
print("Performing stack operations using list")
while ch=='y':
    print()
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY")
    opt=int(input("Enter your choice: "))
    if opt==1:
        push()
    elif opt==2:
        pop()
    elif opt==3:
        peek()
    elif opt==4:
        disp()
    else:
        print("Invalid choice")
    ch=input("Do you want to perform another operation? (y/n): ")


