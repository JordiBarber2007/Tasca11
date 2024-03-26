def menu():
    op = 0
    while op<1 or op>14:
        print("""
        Programa Principal
        1. Estructures Condicionals, if
        2. Estructures Condicionals, match
        3. Estructures Iteratives, for e in b
        4. Estructures Iteratives, for i in range(x)
        5. Estructures Iteratives, for i,e in enumerate(a)
        6. Funció amb Paràmetres
        7. Funció Lambda
        8. Funció List Comprehension
        9. Funció map
        10. Funció Zip
        11. Funció filter
        12. Classes i Objectes
        13. Fitxers
        14. Sortir
        """)
        op = int(input("Introdueix una Opció: "))
        if op<1 or op>14:
            print("Opció no vàlida \n")
        else:
            return op

def ex1():
    a = int(input("Introdueix el primer numero: "))
    b = int(input("Introdueix el segon numero: "))
    if a>b:
        print("{} és major que {}".format(a,b))
    elif b>a:
        print("{} és major que {}".format(b,a))
    else:
        print("Els dos nombres son iguals")
    
def ex2():
    vocal = input("Introdueix una vocal: ")
    match(vocal):
        case 'a':
            print("La vocal introduida es una a")
        case 'e':
            print("La vocal introduida es una e")
        case 'i':
            print("La vocal introduida es una i")
        case 'o':
            print("La vocal introduida es una o")
        case 'u':
            print("La vocal introduida es una u")
        case Other:
            print("Opció no vàlida")

def ex3():
    a = []
    b = []
    for i in range(3):
        a.append(input("Introdueixi la paraula: "))
    for e in a:
        b.append(len(e))
    print("Les longituds de cada paraula és {}".format(b))

def ex4():
    for i in range(1,10,2):
        print(i)

def ex5():
    llista = [15,32,7,24,2]
    dic = {}
    for i,e in enumerate(llista):
        dic[i] = e
    print(dic)

def ex6(l,c):
    b = []
    for e in l:
        if c in e:
            b.append(e)
    print("{}".format(b))

def ex7():
    l = [2,10,23,9,12]
    x = list(map(lambda x:x+10,l))
    print(x)

def ex8():
    l = [2,4,3,6,5]
    r = [x**2 for x in l if x%2 == 1]
    print(r)

def ex9():
    l = ['hola','si','bones','cara','no']
    x = list(map(lambda x:x[::-1],l))
    print(x)

def ex10():
    l = [2,4,6,9,0]
    m = [0,1,2,3,5]
    x = list(zip(l,m))
    print(x)

def ex11():
    l = [4,2,8,3,9]
    x = list(filter(lambda x:x%2 == 1,l))
    print(x)

def ex12():
    class Ordinador():
        def __init__(self,tipus,pantalla):
            self.tipus = tipus
            self.pantalla = pantalla
        def getTipus(self):
            pass
        def getPantalla(self):
            pass

    class Portàtil(Ordinador):
        def getTipus(self):
            print("Portàtil")
        def getPantalla(self):
            print("15 polzades")

    class Tablet(Ordinador):
        def getTipus(self):
            print("Tablet")
        def getPantalla(self):
            print("9 polzades")

    class Servidor(Ordinador):
        def getTipus(self):
            print("Servidor")
        def getPantalla(self):
            print("21 polzades")

    class PC(Ordinador):
        def getTipus(self):
            print("PC")
        def getPantalla(self):
            print("27 polzades")


    l = [Portàtil("Portàtil","15"),
        Tablet("Tablet","9"),
        Servidor("Servidor","21"),
        PC("PC","27")]
        
    for e in l:
        e.getTipus()
        e.getPantalla()

def ex13():
    with open("/home/cicles/AO/ex20.txt","w") as f:
        for i in range(10):
            f.write(str(i)+"\n")
    with open("/home/cicles/AO/ex20.txt","r") as f:
        for i in f:
            print(i)



# Programa Principal

op = 1
while op!= 14:
    op = menu()
    match(op):
        case 1:
            ex1()
        case 2:
            ex2()