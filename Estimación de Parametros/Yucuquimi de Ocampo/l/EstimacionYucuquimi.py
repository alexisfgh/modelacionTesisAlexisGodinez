#!/usr/bin/python3

#   Programa para estimar el parámetro l de la función
#
#   Alexis Francisco Godínez Hernández 

from numpy import *

n1 = 0.20259936876328286
e1 = 0.16945436485754548
k = 14484.277536527565

n2 = 0.9999999999927948
e2 = 0.9469693353747736

h=5

x0=1784
x1=1978
x2=1842
x3=1965
x4=2025
x5=2086

y0=37
y1=18
y2=163
y3=49
y4=86
y5=123

z0=x0*y0
z1=x1*y1
z2=x2*y2
z3=x3*y3
z4=x4*y4
z5=x5*y5

w1=y1-y0
w2=y2-y1
w3=y3-y2
w4=y4-y3
w5=y5-y4

x=array([x1,x2,x3,x4,x5])
y=array([y1,y2,y3,y4,y5])
z=array([z1,z2,z3,z4,z5])
w=array([w1,w2,w3,w4,w5])

b = n1*x*(1-(x+y)/k) + e1*x + (1/h) * w
l=dot(z,b)/dot(z,z)

print('l = ',l)

datos=open("parámetro.txt","w")
datos.write("l = "+str(l)+"\n")
datos.close()