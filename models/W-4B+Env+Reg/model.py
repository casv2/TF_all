import juliaimport
import julip
import os

model_dir = os.path.dirname(os.path.realpath(__file__))
IP = juliaimport.import_IP(model_dir + "/W-PIP-B4+Env+Reg.jld2")

#IP = juliaimport.import_IP(os.path.realpath(__file__)[0:-8] + "Ti_4B_med.json")
ASE_IP = julip.JulipCalculator("IP")

calculator = ASE_IP

no_checkpoint = True

name = 'PIP'
