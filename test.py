#!/usr/bin/python3

import sys

#print(sys.version_info)
#print(sys.version)

#print(sys.platform)

#print('hello')
#print('''multiline test''')

str = "Spam"
#print(str)

a = [1, 2, 3, 4, 5]

squares = [x**2 for x in a]
#print(squares)

# on a deux variables temps et distance
temps=6.896
distance=19.7
vitesse=distance/temps
print("La vitesse est de %2.2f" % vitesse)
print("la vitesse est  = {:.2f} metre par seconde".format(vitesse))

#ints = [1, 2, 3, 4, 5, 6, 7]
ints = [x for x in range(0,4)]
print(ints)
ints = [x for x in range(4,7)]
print(ints)

msg="c'est la formation Devops"
for l in msg:
    print(l)

list = [17, 38, 10, 25, 72]
list.sort()
print(list)
list.append(12)
print(list)
print("l'indice du numero 17 est %d" % list.index(17))
list.pop(list.index(38))
print(list)
print(list[2:])

