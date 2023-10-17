#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:49:57 2016
@author: <brian> (<kiplangat>)   
"""
from scipy.integrate import odeint
def f(y, t):
    return [ - y[0] + k*np.sin((t+tau)/T) ]
k =.02; tau=1.; T=.05 #parameters for the model
#initial conditions
x_init=[-.5]; xdot_init=[0.]
timepoints=np.linspace(.0,.10,num=10); timepoints
solution=odeint(f,x_init,timepoints)
print solution[:,:]

