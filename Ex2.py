from operator import add
from functools import reduce

#Map
def Passar_a_numero(m):
    c = list(map(lambda x:str(x), m))
    d = reduce(lambda x,y:x+y, c)
    print("La llista {} és el número {}".format(m,d))

m = [3, 5, 7,9,1]
Passar_a_numero(m)
