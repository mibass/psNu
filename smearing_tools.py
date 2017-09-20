#!/usr/bin/env python
import numpy as np
from math import *

def smearingA(Ebins, sigma ):
    dim=len(Ebins)-1
    m=np.zeros((dim,dim))

    for i in range(dim):
        e=(Ebins[i]+Ebins[i+1])/2
        x=e+sigma*e*np.random.randn(10000)
        h=np.array(np.histogram(x,bins=Ebins)[0],'d')

        #store in matrix, normalizing each column to 1
        m[:,i]=h/sum(h)

    return m

def smearingB(Ebins, sigma, missing ):
    dim=len(Ebins)-1
    m=np.zeros((dim,dim))

    for i in range(dim):
        e=(Ebins[i]+Ebins[i+1])/2
        x=e+0.05*e*np.random.randn(10000)-missing*2*e*np.random.random(10000)
        h=np.array(np.histogram(x,bins=Ebins)[0],'d')

        #store in matrix, normalizing each row to 1
        m[:,i]=h/sum(h)

    return m

def asmearing(Ebins, sigma, bias):
    dim=len(Ebins)-1
    m=np.zeros((dim,dim))
    for i in range(dim):
        e1=(Ebins[i]+Ebins[i+1])/2
        h=np.zeros(dim)
        for j in range(dim):
            e2=(Ebins[j]+Ebins[j+1])/2
            h[j]=exp(-pow(e2-e1,2)/(2*sigma*sigma*e1*e1))
            if(e2<=e1):
                #h[j]+=e1*bias
                h[j]+=bias*exp(-pow(e2-e1,2)/(2*e1*e1))
        m[:,i]=h/sum(h)
    return m
