#!/usr/bin/python3

# Alexis Francisco Godínez Hernández
# Programa que simula Rounge Kutta Order Four y varia los parámetros e1 y e2

from matplotlib.pyplot import *
from numpy import *

n1=.81
n2=.802
k=15000
l=.0001
e1=.8002
e2=.800101

def f1(t,x,y):
    return n1*x*(1-(x+y)/k)-l*x*y-e1*x

def f2(t,x,y):
    return n2*y*(1-(x+y)/k)+l*x*y-e2*y

def x1(ee1,ee2):
	return (k/n1)*(n1-ee1)

def y2(ee1,ee2):
	return (k/n2)*(n2-ee2)

def x3(ee1,ee2):
	return (ee2*n1-ee1*n2+k*l*(ee2-n2))/(l*(k*l+n1-n2))

def y3(ee1,ee2):
	return (ee1*n2-ee2*n1+k*l*(n1-ee1))/(l*(k*l+n1-n2))

def kutta(a,b,N,q1,q2):
    x=[]
    y=[]
    
    h=(b-a)/N
    t=a
    
    w1=q1
    w2=q2
    
    x+=[w1]
    y+=[w2]
    
    for i in range(1,N+1):
        k11=h*f1(t,w1,w2)
        k12=h*f2(t,w1,w2)
        
        k21=h*f1(t+h/2,w1+k11/2,w2+k12/2)
        k22=h*f2(t+h/2,w1+k11/2,w2+k12/2)
        
        k31=h*f1(t+h/2,w1+k21/2,w2+k22/2)
        k32=h*f2(t+h/2,w1+k21/2,w2+k22/2)
        
        k41=h*f1(t+h,w1+k31,w2+k32)
        k42=h*f2(t+h,w1+k31,w2+k32)
        
        w1=w1+(k11+ 2*k21 + 2*k31 + k41)/6
        w2=w2+(k12+ 2*k22 + 2*k32 + k42)/6
        
        t=a+i*h
        
        x+=[w1]
        y+=[w2]
    
    return x,y



if __name__=="__main__":
    x,y=kutta(0,3000,1000,15,3)
    plot(x,y)
    
    x,y=kutta(0,3000,1000,180,10)
    plot(x,y)
    
    x,y=kutta(0,3000,1000,2,55)
    plot(x,y)
    
    x,y=kutta(0,3000,1000,72,13)
    plot(x,y)
    
    x,y=kutta(0,3000,1000,250,100)
    plot(x,y)
    
    x,y=kutta(0,3000,1000,6,10)
    plot(x,y)
    
    plot(0,0,'or')  #x0
    plot((k/n1)*(n1-e1),0,'or')  #x1
    plot(0,(k/n2)*(n2-e2),'or')  #x2
    plot((e2*n1-e1*n2+k*l*(e2-n2))/(l*(k*l+n1-n2)),(e1*n2-e2*n1+k*l*(n1-e1))/(l*(k*l+n1-n2)),'or')  #x3
    
    text(5,0,'$\mathbf{\overline{x}}_0$')
    text((k/n1)*(n1-e1)+5,0,'$\mathbf{\overline{x}}_1$')
    text(5,(k/n2)*(n2-e2),'$\mathbf{\overline{x}}_2$')
    text((e2*n1-e1*n2+k*l*(e2-n2))/(l*(k*l+n1-n2))+5,(e1*n2-e2*n1+k*l*(n1-e1))/(l*(k*l+n1-n2)),'$\mathbf{\overline{x}}_3$')
    
    xlabel("Población $x$")
    ylabel("Población $y$")
    
    savefig('simulacion.eps')
    
    show()
    
    
    # Se e2 y se varía e1
    w=np.linspace(e1, .1, 10)

    plot(w,x3(w,e2),'bo')
    plot(w,y3(w,e2),'ro')

    xlabel("$e_1$")
    ylabel("$Población$")
    legend(['$x$','$y$'])

    savefig('e1.eps')

    show()
    
    # Se e1 y se varía e2
    w2=np.linspace(e2, .7993, 10)

    plot(w2,x3(e1,w2), 'bo')
    plot(w2,y3(e1,w2), 'ro')

    xlabel("$e_2$")
    ylabel("$Población$")
    legend(['$x$','$y$'])

    savefig('e2.eps')

    show()