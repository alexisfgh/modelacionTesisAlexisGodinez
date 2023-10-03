#!/usr/bin/python3

#   Programa para estimar el parámetro l de la función
#
#   Alexis Francisco Godínez Hernández 

from numpy import *

n1 = 0.7844485404243957
e1 = 0.5851467176143677
k = 1001.2528835387923

n2 = 0.1955078516658104
e2 = 0.17457395992594

h=5

x0=351
x1=316
x2=184
x3=309
x4=273
x5=237

y0=458
y1=335
y2=369
y3=146
y4=194
y5=243

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