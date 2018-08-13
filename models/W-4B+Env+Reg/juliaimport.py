
# coding: utf-8

# In[2]:

import numpy as np
from ase.calculators.calculator import Calculator

import os
from julia import Julia



if not os.environ.has_key('JL_RUNTIME_PATH'):
    julia = Julia()
else:
    # "/Users/ortner/gits/julia6bp/usr/bin/julia"
    julia = Julia(jl_runtime_path=os.environ['JL_RUNTIME_PATH'])

julia.using("NBodyIPs")

def import_IP(potname):
    #julia.eval("IP = load_ip(\"" + potname + "\")")
    julia.eval("IP = load_ip(\""+ potname + "\")")
    julia.eval("IPf = fast(IP)")
    IP = julia.eval("IPf")
    return IP
