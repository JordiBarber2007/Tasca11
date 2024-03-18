def lenp(frase):
    r = frase.split(" ")
    l = list(map(len,r))
    print(l)



frase = input("Introdueix una frase: ")
lenp(frase)