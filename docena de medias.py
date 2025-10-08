Cont=0
C=str(input("usted quiere comprar (si o no)"))
if C=="si":
    print("usted si quiere comprar")
    def menu():
        print("menu de opciones")
        print("1) usted quiere comprar 2 docenas de pares de media")
        print("2) usted quiere comprar 4 docenas de pares de media")
        print("3) usted quiere comprar 6 docenas de pares de media")
        print("4) gracias por comprar")
    def main():
        menu()
        op=int(input("ingrese algo en el menu de opciones"))
        if op==1:
            print("usted quiere comprar 2 pares, gracias por su compra")
        if op==2:
            print("usted quiere comprar en gran cantidad, gracias por su compra")
        elif op==3:
            print("usted quiere comprar una cantidad ya mayor a la deseada, gracias por su compra")
        else:
            print("gracias por comprar")
            while op not in [1,2,3]:
                main() 
    main()          
if C=="no":
    print("usted no quiere comprar")