def menu():
    opcio=0
    while opcio<1 or opcio >5:
        print("""
            Menu principal:
            1. Programació estructurada
            2. Programació funcional
            3. Programació orientada a  objectes
            4. Acces al fiftxer
            5. Sortir
        """)
        opcio = int(input("Seleccioni l'opcio: "))
        if opcio<1 or opcio >5:
            print("Opcio no valida!")
        else:
            return opcio
    
def programacio_estructurada():
    print("Molt be has entrat a la programacio estructurada!")
def programacio_funcional():
    print("Molt be has entrat a la programacio funcional!")
def  programacio_oo():
    print("Molt be has entrat a la programacio OO!")
def acces_fitxer():
    print("Molt be has entrat a l'acces de fitxers")
#Programa principal
op=1
while op!=5:
    op=menu()
    match(op):
        case 1:
            programacio_estructurada()
        case 2:
            programacio_funcional()
        case 3:
            programacio_oo()
        case 4:
            acces_fitxer()
        case 5:
            print("Gracies per utilitzar aquesta aplicacio, fins un altre!")
        case other:
            print("Opcio no valida! ")