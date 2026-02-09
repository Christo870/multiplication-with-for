a=int(input("entrer le 1er nombre :"))
b=int(input("entrer le 2eme nombre :"))
operation=input("entrer votre operation : ")
operations=["+","-","/","*"]

if operation not in operations:
    print("entrer un operation arithmetique disponible : ")


def addition(a,b):
    add=a+b
    return add

def sosustraction(a,b):
    sous=a-b
    return sous

def multiplication(a,b):
    multi=a*b
    return multi

def division(a,b):
    if a==0 or b==0:
        return ("division par 0 impossible")
    div=a/b
    return div

if operation=="+":
    print(f"La somme de {a} et {b} est : ",addition(a,b))
elif operation=="-":
    print(f"La difference entre {a} et {b} est : ",sosustraction(a,b))    

elif operation=="*":
    print(f"Le produit entre {a} et {b} est : ",multiplication(a,b))
else:
    print(f"La division entre {a} et {b} est : ",division(a,b))    



