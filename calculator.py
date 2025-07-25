def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def divide(x,y):
    if(y == 0):
        return "error! denominator cannot be zero."
    return x/y

while True:
    print("\n simple calculator")   
    print("1. add")   
    print("2. substract")   
    print("3. multiplication")   
    print("4. divide")    
    print("5. exit")

    choice = input("enter choice (1,2,3,4,5): ")

    if choice == '5':
        print("exiting the calculator. goodbye!") 
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("enter first number: "))
            num2 = float(input("enter second number: "))     
        except: ValueError
        print("invalid input! please enter numbers only.")     

    if choice == '1':
        print("result: ", add(num1,num2))
    elif choice == '2':
        print("result: ", substract(num1,num2))   
    elif choice == '3':
        print("result: ", multiplication(num1,num2))    
    elif choice == '4':
        print("result: ", divide(num1,num2))  
    else:         
        print("invalid choice! please enter a valid option") 
