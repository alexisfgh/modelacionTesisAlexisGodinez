#!/usr/bin/python3

#   Programa para ver si los parámetros son correctos para el teorema de nuestro modelo
#
#   Alexis Francisco Godínez Hernández 


n1 = 0.7844485404243957
#e1 = 0.5851467176143677
k = 1001.2528835387923

n2 = 0.1955078516658104
#e2 = 0.17457395992594

#l = 0.0033189503462847485

l = 0.00033189503462847485

e1 = 0.3146342
e2 = 0.155049


e1umbral = n1 - ((n2-e2)*(n1+k*l))/n2

lumbral = ( (n1-e1)*n2 )/ ( k*(n2-e2) ) - n1/k

e2umbral = n2 - ( (n1-e1)/(n1+k*l) )*n2

print(n1,'>', e1)
if n1 > e1:
    print('Sí')
    print()
else:
    print('no')
    print()

print(n1,'>', e1)
if n2 > e2:
    print('Sí')
    print()
else:
    print('no')
    print()

print(n2/l, '<', k)
if n2/l < k:
    print('Sí')
    print()
else:
    print('no')
    print()

print((n2-e2)/n2, '<', (n1-e1)/(n1+k*l))
if (n2-e2)/n2 < (n1-e1)/(n1+k*l):
    print('Sí')
    print()
else:
    print('no')
    print()

x = (e2*n1 - e1*n2 + k*l*(e2-n2)) / (l*(k*l+n1-n2))
y = (e1*n2 - e2*n1 + k*l*(n1-e1)) / (l*(k*l+n1-n2))

print()
print('x3 = ', x)
print('y3 = ', y)
print()

print(e1umbral)
print(lumbral)
print(e2umbral)