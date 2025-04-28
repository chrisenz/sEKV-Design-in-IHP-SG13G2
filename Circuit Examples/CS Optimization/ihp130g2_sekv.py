import numpy as np
from numpy import sqrt as sqrt

################################################
# sEKV parameters for the IHP G2 130nm Process #
#            Long-channel values               #
################################################

######################
# Physical constants #
######################
kB=1.38064852e-23
q=1.60217662e-19
T0=273.15
epsilon0=8.854e-12
epsilonox=3.9
TC=27
T=T0+TC
kT=kB*T
UT=kT/q

######################
# Process parameters #
######################
tox=2.2404e-09
Cox=epsilonox*epsilon0/tox
VDD=1.2
Lmin=130e-9
Wmin=150e-9
z1=340e-9 # used to calculate the drain/source junction perimeter as shown below
z2=389e-9 # used to calculate the drain/source junction perimeter as shown below

#       z1              z2            z1  
#   ----------------------------------------  
#   |          |   |         |   |         |  
#   |    S     | G |   D     | G |    S    |  w/ng, >=0.15u   
#   |          |   |         |   |         |  
#   ----------------------------------------  

###################
# nMOS parameters #
###################
# Channel width and length corrections for current
DLn=58.846e-9
DWn=-20.0e-9
# Channel width and length corrections for intrinsic and overlap capacitances
DLCVn=92.567e-9
DWCVn=-10.0e-9
# Channel width and length corrections for fringing capacitances
DLGCVn=33.721e-9
DWGCVn=10.0e-9
# Long-channel sEKV parameters parameters
n0n=1.22
Ispecsqn=708.3e-9
VT0n=0.246
# Short-channel sEKV parameters parameters
Lsatn=7.1e-9
lambdan=1.4e6
#lambdan=0.85e6
# Flicker noise parameters
AFn=1
KFn=2.208e-24
rhon=KFn/(4*kT*Cox)
# Junction capacitances
CJn=9.764e-04 # Zero-bias bottom junction capacitance per unit area
CJSWSTIn=2.528e-11 # Zero-bias side-wall junction capacitance per unit length along STI edge
CJSWGATn=3.000e-11 # Zero-bias side-wall junction capacitance per unit length along GATE edge
# Overlap capacitances
CGSOn=4.535e-10 # Total gate-to-source overlap capacitance per effective unit width
CGDOn=4.535e-10 # Total gate-to-drain overlap capacitance per effective unit width
CGBOn=4.441e-22 # Gate-to-bulk overlap capacitance per effective unit length
# Fringing capacitances
CGSFn=2.0e-10 # Total gate-to-source extrinsic capacitance per effective unit width
CGDFn=2.0e-10 # Total gate-to-drain extrinsic capacitance per effective unit width

###################
# pMOS parameters #
###################
# Channel width and length corrections for current
DLp=50.508e-9
DWp=30.0e-9
# Channel width and length corrections for intrinsic and overlap capacitances
DLCVp=146.43e-9
DWCVp=15.0e-9
# Channel width and length corrections for fringing capacitances
DLGCVp=95.922e-9
DWGCVp=-15.0e-9
# Long-channel sEKV parameters parameters
n0p=1.23
Ispecsqp=244.6e-9
VT0p=0.365
# Short-channel sEKV parameters parameters
Lsatp=24.9e-9
#lambdap=14.3e6
lambdap=10e6
# Flicker noise parameters
AFp=1
KFp=8.801e-24
rhop=KFp/(4*kT*Cox)
# Junction capacitances
CJp=8.631e-04 # Zero-bias bottom junction capacitance per unit area
CJSWSTIp=3.192e-11 # Zero-bias side-wall junction capacitance per unit length along STI edge
CJSWGATp=2.747e-11 # Zero-bias side-wall junction capacitance per unit length along GATE edge
# Overlap capacitances
CGSOp=4.426e-10 # Total gate-to-source overlap capacitance per effective unit width
CGDOp=4.426e-10 # Total gate-to-drain overlap capacitance per effective unit width
CGBOp=2.186e-11 # Gate-to-bulk overlap capacitance per effective unit length
# Fringing capacitances
CGSFp=1.0e-10 # Total gate-to-source extrinsic capacitance per effective unit width
CGDFp=1.0e-10 # Total gate-to-drain extrinsic capacitance per effective unit width