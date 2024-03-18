def diccionari(llista):
    dic = {}
    for i,e in enumerate(llista):
    #L'element té el nombre de la seva posició
        dic[e]= i
    print("De la llista {} hem creat el diccionari \n{}".format(llista, dic))

#Principal
llista = ["Moto", "Casa", "Escola","vaca", "Moix", "Ca", "Jordi"]
diccionari(llista)