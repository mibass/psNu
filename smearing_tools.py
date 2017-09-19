#!/usr/bin/env python
import numpy as np


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
