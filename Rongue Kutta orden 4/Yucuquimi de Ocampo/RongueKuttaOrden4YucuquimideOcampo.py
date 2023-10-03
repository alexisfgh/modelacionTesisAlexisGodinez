#!/usr/bin/python3

# Alexis Francisco Godínez Hernández
# Rounge Kutta Order Four

from matplotlib.pyplot import *

n1 = 0.20259936876328286
e1 = 0.16945436485754548
k = 14484.277536527565

n2 = 0.9999999999927948
e2 = 0.9469693353747736

l = 0.0030099785819119487

def f1(t,x,y):
    return n1*x*(1-(x+y)/k)-l*x*y-e1*x

def f2(t,x,y):
    return n2*y*(1-(x+y)/k)+l*x*y-e2*y

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

def equi():
    print('X0 = (0,0)')
    print('X1 = (',(k/n1)*(n1-e1),',0)')
    print('X2 = (0,',(k/n2)*(n2-e2),')')
    print('X3 = (',(e2*n1-e1*n2+k*l*(e2-n2))/(l*(k*l+n1-n2)),',',(e1*n2-e2*n1+k*l*(n1-e1))/(l*(k*l+n1-n2)),')')


if __name__=="__main__":
    equi()
    
    x,y=kutta(2020,2120,1000,2086,123)
    plot(x,y)
    
    plot(0,0,'or')  #x0
    plot((k/n1)*(n1-e1),0,'or')  #x1
    plot(0,(k/n2)*(n2-e2),'or')  #x2
    #plot((e2*n1-e1*n2+k*l*(e2-n2))/(l*(k*l+n1-n2)),(e1*n2-e2*n1+k*l*(n1-e1))/(l*(k*l+n1-n2)),'or')  #x3
    
    text(0,0,'$\mathbf{\overline{x}}_0$')
    text((k/n1)*(n1-e1),0,'$\mathbf{\overline{x}}_1$')
    text(0,(k/n2)*(n2-e2),'$\mathbf{\overline{x}}_2$')
    #text((e2*n1-e1*n2+k*l*(e2-n2))/(l*(k*l+n1-n2)),(e1*n2-e2*n1+k*l*(n1-e1))/(l*(k*l+n1-n2)),'$\mathbf{\overline{x}}_3$')
    
    xlabel("Población $x$")
    ylabel("Población $y$")
    
    savefig('simulacionYucuquimi.eps')
    
    show()
    
    
    
    t=np.linspace(2020, 2120, 1000+1)
    plot(t,x)
    plot(t,y,'r:')
    xlabel("Año")
    ylabel("Población")
    legend(['$x$','$y$'])
    savefig('simulacionYucuquimiCondicionInicial.eps')
    show()