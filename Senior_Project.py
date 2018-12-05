# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:22:03 2018

@author: bradl
"""
import numpy as numpy
import timeit

def function_1(t,x):
        return (x * (1-numpy.e**t)/((numpy.e**t)+1))
def function1_answer(t):
    return 12*(numpy.e**t)/(((numpy.e**t)+1)**2)


def rk4(M,h,t,x,f):
    knots=[t]
    values=[x]
    fcncalls=M*10
    for k in range(M):
        F1=h*f(t,x)
        F2=h*f(t+h/2,x+F1/2)
        F3=h*f(t+h/2,x+F2/2)
        F4=h*f(t+h,x+F3)
        x=x+(F1+2*F2+2*F3+F4)/6    
        t=t+h
        knots.append(t)
        values.append(x)
    data1={'t':knots,'x':values, 'Calls':fcncalls}
    return(data1) 
    
    
def Euler(M,h,t,x,f):  
    interval=[t]
    X=[x]
    fcncalls=M*2
    for k in range(M):
        x=x+h*f(t,x)
        t=t+h
        interval.append(t)
        X.append(x)
    data2={'t':interval,'x':X, 'Calls':fcncalls}
    return (data2)


def compare(M,h,t,x,f,true_answer):
    fmt='{}, {}, {}\n'
    fmt2='{},{}, {}\n'
    Runge=rk4(M,h,t,x,f)
    eulerMeth=Euler(M,h,t,x,f)
    T=Runge['t']
    rk4X=Runge['x']
    EMX=eulerMeth['x']
    RKCost=Runge['Calls']
    EMCost=eulerMeth['Calls']
    mfile=open('FinalProject.csv','wt')
    mfile.write('t,'+\
    'Runge Kutta,'+\
    'Euler,\n')
    for i in range(M+1):
        line=fmt.format(T[i],rk4X[i]-true_answer(T[i]),EMX[i]-true_answer(T[i]))
        mfile.write(line)
    line2=fmt2.format('Calls',RKCost, EMCost)
    mfile.write(line2)
    mfile.close()
    return None