stack = []

def push(item):
   stack.append(item)

def pop():
   if len(stack) == 0:
       return None
   else:
       return stack.pop()

def display():
   print(stack)

while True:
   print("\n1. Push")
   print("2. Pop")
   print("3. Display")
   print("4. Exit")
   choice = input("Enter your choice: ")

   if choice == "1":
       item = input("Enter the item to push: ")
       push(item)
   elif choice == "2":
       result = pop()
       if result is not None:
           print("Popped item:", result)
       else:
           print("Stack is empty")
   elif choice == "3":
       display()
   elif choice == "4":
       print("Thank you")
       break
   else:
       print("Invalid choice! Please choose a valid option.")