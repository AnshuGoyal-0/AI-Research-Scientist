#import layer
#functions layer
def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

#Coding layer



while 1:
    if(choice=="stop"):
        break
    else:
        choice = input("enter her digit you want to perform:- \n1.add\n2.sub\n3.mul\n4.div\n5.stop\n")
        num1 = input("enter you first digit : ")
        num2 = input("enter you second digit : ")
        switch(choice):
            case "add":
                add(num1,num2)
            case "sub":
                sub(num1,num2)
            case "mul":
                mul(num1,num2)
            case "div":
                div(num1,num2)
            default:
                continue


