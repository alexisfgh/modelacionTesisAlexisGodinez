#!/usr/bin/python3

#   Programa para estimar los parámetros n,k,e, de la función
#   solución de la ecuación diferencial:
#       dz/dt=nz(1-z/k)-ez
#       z(0)=w
#   
#   La función es:
#              (n-e) ( w/ (n-e-wn/k)) e^((n-e)t)
#       z(t)= ----------------------------- 
#              1+n/k ( w/ (n-e-wn/k)) e^((n-e)t)
#
#   Alexis Francisco Godínez Hernández 

import csv
from matplotlib.pyplot import *
from scipy.optimize import leastsq
import scipy as sc
import numpy


#   Capacidad de carga para la agencia de Yucuquimi de Ocampo
w=458
k = 1001.2528835387923



def f(t,n,e):
    return ( (n-e) * ( w / ( n-e-(w*n)/k) ) * np.exp( (n-e)*t ) ) / ( 1 + (n/k) * ( w / ( n-e-(w*n)/k) )*np.exp( (n-e)*t ) )

    

def leer(d):
    a=[]
    b=[]
    with open(d) as File:
        reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            a+=[row[0]]
            b+=[row[1]]
    x=[]
    y=[]    
    for i in a:
        x+=[float(i)]
    for i in b:
        y+=[float(i)]
    
    x=numpy.array(x)
    y=numpy.array(y)
    
    return x,y

if __name__=="__main__":

    i=numpy.array([.335,.331])      # Condición inicial en los parámetros

    #   Datos de la agencia de Tezoatlán de Santa María Tindú
    x,y=leer('SantaMariaTindu.csv')
    
    #   Estimacion de parámetros con condición inicial
    long, _ = sc.optimize.curve_fit(f, x, y, i, bounds=([0.0,0.0],[1.0,1.0]))
    
    #   Estimacion de parámetros sin condición inicial
    #long, _ = sc.optimize.curve_fit(f, x, y)
    
    tt=np.linspace(0, 50, 3000)
    z=f(tt,*long)
    
    n=long[0]
    e=long[1]

    print('n2 = ', n)
    print('e2 = ', e)
    
    datos=open("parámetros.txt","w")
    datos.write("n2 = "+str(n)+"\n")
    datos.write("e2 = "+str(e)+"\n")
    datos.write("k = "+str(k)+"\n")
    datos.close()
    
    plot(x,y,'o')
    plot(tt,z)
    
    ylabel("Población")
    xlabel("Años")

    savefig('EstimacionTindu-n2-e2.eps')
    
    show()