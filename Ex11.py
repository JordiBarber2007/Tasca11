"""
def llegir(fitxer):
    a = []
    with open(fitxer,"r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)

#Principal
    
fitxer = "/home/cicles/AO/Tasca 11/Prova/fitxerpy.txt"
llegir(fitxer)
"""

#Variant 

def llegir(fitxer):
    a = []
    with open(fitxer,"r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)

def afegir_fitxer(fitxer,llista):
    with open(fitxer,"a+") as f:
        for e in llista:
            f.write(e+"\n")
    
    
#Programa Principal
    
fitxer = "/home/cicles/AO/Tasca11/Prova/fitxerpy.txt"
llista = ["Jordi", "Ian","Pepe", "Ayoub", "Oscar", "David", "Sergi", "Marc",]
afegir_fitxer(fitxer,llista)
llegir(fitxer)