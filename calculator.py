#Basic Calculator by Using Python programming
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
while True:
    print ("please select operation\n"
       "1.Add(+)\n"
       "2.Subtract(-)\n"
       "3.Multiply(*)\n"
       "4.Division(/)")
    select=int(input("Enter operation from 1,2,3,4: "))
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    if select==1:
        print(a,"+",b,"=",add(a,b))
    elif select==2:
        print(a,"-",b,"=",subtract(a,b))
    elif select==3:
        print(a,"*",b,"=",multiply(a,b))
    elif select==4:
        print(a,"/",b,"=",division(a,b))
    c=input("For go to the next calculation..(yes/no):")
    if c=="no":
        break
else:
    print("invalid select operation")
    
