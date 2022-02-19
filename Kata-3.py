print("Se van a comparar la magnitud de tres numeros. Dependiendo de la condicion, se mostrara en texto que se cumplio.")
A=input("¿Que valor quiere darle a A? ")
B=input("¿Que valor quiere darle a B? ")
C=input("¿Que valor quiere darle a C? ")
if A>B:
    if B>C:
        print("A es mayor que B y C")
    else: 
        print("A es mayor que B y menor que C")  

elif A==B:
    print("A es igual que B")
else:
    print("A es menor que B")