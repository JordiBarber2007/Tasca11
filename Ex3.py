def filtrar(llista, c):
    f=list(filter(lambda x: x[0]==c.lower() or x[0]==c.upper(), llista))
    print("De la llista{}, les paraules que comencen per {} són {}".format(llista, c, f))

#Programa principal
llista = ["Josep", "Joana", "Jordi", "Maria", "Marc", "Pere", "Paula"]
c = "p"
filtrar(llista,c)