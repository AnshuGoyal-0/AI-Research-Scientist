#import layer
#functions layer
def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def mul(a,b):
    return (a*b)

def div(a,b):
    return (a/b)

#Coding layer
choice = ""l
while True:
    choice = input("enter the name of operation you want to perform:- \n1.add\n2.sub\n3.mul\n4.div\n5.stop\n\n").lower()
    if(choice=="stop"):
        break
    else:
        num1 = int(input("enter you first digit : "))
        num2 = int(input("enter you second digit : "))

        if(choice in ["add","sum","plus","+"]):
            print(add(num1,num2))
            
        elif(choice in ["minus","sub","subtract","-"]):
            print(sub(num1,num2))
            
        elif(choice in ["into","mul","guda","*"]):
            print(mul(num1,num2))
            
        elif(choice in ["divison","div","bhag","/"]):
            if(num2=="0"):
                print("division error")
            else:
                print(div(num1,num2))
            
        else:
            print("operation not found try again")
            choice = ""
            continue
        choice = ""
        continue
            
            


