def addition(x,y):
    print(x+y)
def subtraction(x,y):
    print(x-y)
def multiplication(x,y):
    print(x*y)
def division(x,y):
    print(x/y)

while True:
    x=int(input("Enter the first number:"))
    y=int(input("Enter the second number:"))
    print("1.addition\n2.Subtraction\n3.multiplication\n4.division\n")
    op=int(input("enter your choice:"))
    if op==1:
       print(x+y)
    elif op==2:
       print(x-y)
    elif op==3:
       print(x*y)
    elif op==4:
       print(x/y)
    else:
       print("Ivalid choice")
        
    
