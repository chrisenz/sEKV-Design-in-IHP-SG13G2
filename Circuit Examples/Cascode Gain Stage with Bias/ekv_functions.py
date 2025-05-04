#################################################
# Normalized functions for the EKV MOSFET model #
# Christian Enz                                 #
# Version 1                                     #
# 1.3.2025                                      #
#################################################

################################
# Redefine the numpy functions #
################################

import numpy as np
from numpy import pi as pi
from numpy import log as ln
from numpy import log10 as log
from numpy import sqrt as sqrt
from numpy import exp as exp
from numpy import arctan as atan

#####################################
# Large-signal normalized functions #
#####################################

#--------------
# Long-channel
#--------------

# Normalized drain current versus charge (long-channel)
def ic_q(q):
    return q*(q+1)

# Normalized charge versus current (long-channel)
def q_ic(ic):
    return (sqrt(4*ic+1)-1)/2

# Normalized saturation voltage versus normalized charge
def v_q(q):
    return 2*q+ln(q)

# Inverse function giving q(v) corresponding to the inverse function of v(q) using the Lambert W-function
from scipy.special import lambertw
def q_v_lambert(v):
    return np.real(lambertw(2*exp(v))/2)

# Inverse function giving q(v) corresponding to the inverse function of v(q) using the EKV 2.6 approximation
def q_v(v):
    if v <= -15:
        q0=1/(2+exp(v))
    else:
        if v <-0.35:
            z0=1.55+exp(-v)
        else:
            z0=2/(1.3+v-ln(v+1.6))
    z1=(2+z0)/(1+v+ln(z0))
    q0=(1+v+ln(z1))/(2+z1)
    return q0

# Normalized saturation voltage versus inversion coefficient (long-channel)
def vps_ic(ic):
    return ln(sqrt(4*ic+1)-1)+sqrt(4*ic+1)-1-ln(2)

# Inversion coefficient versus normalized saturation voltage (long-chanel)
def ic_vps(vps):
    return ic_q(q_v(vps))

# Drain-to-source saturation voltage versus inversion coefficient
# New vdssat function to avoid problems in the inverse function (CE: 9.3.2022)
def vdssat_ic(ic):
    vdssatwi=4
    return 2*sqrt(ic+vdssatwi)

# Inversion coefficient versus drain-to-source saturation voltage
# New inverse vdssat function to avoid having negative ic for vdssat<4
def ic_vdssat(vdssat):
    vdssatwi=4
    if vdssat<vdssatwi:
        ic=0
    else:
        ic=(vdssat/2)**2-vdssatwi
    return ic

# Slope factor versus inversion coefficient for vs=0
def n_vp(vp,gammab,psi0):
    return 1+gammab/(2*sqrt(psi0+vp))

# Slope factor versus inversion coefficient for vs=0
def n_ic(ic,gammab,psi0):
    vp=vps_ic(ic)
    return n_vp(vp,gammab,psi0)

#---------------
# Short-channel
#---------------

# Normalized charge versus current including VS
def q_ic_short(ic,lc):
    return (sqrt(4*ic+1+(lc*ic)**2)-1)/2

# Normalized current in saturation versus charge including VS
def ic_q_short(qs,lc):
    return (2*(qs**2+qs))/(1+sqrt(1+lc**2*(qs**2+qs)))

# Normalized saturation voltage versus inversion coefficient (including velocity saturation)
def vps_ic_short(ic,lc):
    q=q_ic_short(ic,lc)
    return 2*q+ln(q)

# Inversion coefficient versus normalized saturation voltage (including velocity saturation)
def ic_vps_short(vps,lc):
    return ic_q_short(q_v(vps),lc)

# Inversion coefficient versus normalized saturation voltage (including velocity saturation)
def ic_vps_lambert(vps,lc):
    return ic_q_short(q_v_lambert(vps),lc)

# Normalized charge at drain due to VS
def qdsat_qs(qs,lc):
    num=lc*(qs**2+qs)
    den=1+sqrt(1+lc**2*(qs**2+qs))
    return num/den

# Saturation voltage due to VS
def vdsat_v_q(vp,qdsat):
    return vp-2*qdsat-ln(qdsat)

# Drain charge including VS
def qd_prime_q(vd,vdsat,qd,qdsat):
    if vd<=vdsat:
        qdprime=qd
    else:
        qdprime=qdsat
    return qdprime

def qd_prime_v(vp,vd,vdsat,qdsat):
    if vd<=vdsat:
        qdprime=q_v_lambert(vp-vd)
    else:
        qdprime=qdsat
    return qdprime

#####################################
# Small-signal normalized functions #
#####################################

# Source transconductance versus inversion coefficient (long-channel)
def gms_ic(ic):
    return (sqrt(4*ic+1)-1)/2

# Source transconductance versus inversion coefficient (including velocity saturation)
def gms_q_short(q,lc):
    return q/sqrt(1+lc**2*(q**2+q))

# Source transconductance versus inversion coefficient (including velocity saturation)
def gms_ic_short(ic,lc):
    num=sqrt(4*ic+1+(lc*ic)**2)-1
    den=2+lc**2*ic
    return num/den

# Inversion coefficient versus normalized transconductance (long-channel)
def ic_gms(gms):
    return gms*(gms+1)

# Inversion coefficient versus normalized transconductance (including velocity saturation)
def ic_gms_short(gms,lc):
    if lc<=0:
        ic=gms*(gms+1)
    else:
        ic=(2-gms*lc**2*(1+2*gms)-sqrt(4-(gms*lc)**2*(4-lc**2)))/(lc**2*((gms*lc)**2-1))
    return ic

# Normalized Gm/ID function versus inversion coefficient (long-channel)
def gmsid_ic(ic):
    return gms_ic(ic)/ic

# Normalized Gm/ID function versus inversion coefficient (including velocity saturation)
def gmsid_ic_short(ic,lc):
    return gms_ic_short(ic,lc)/ic

# Inverse normalized Gm/ID function (long-channel)
def ic_gmsid(gmsid):
    return (1-gmsid)/gmsid**2

######################################
# Thermal noise normalized functions #
######################################

#--------------
# Long-channel
#--------------

# Thermal noise conductance (long-channel)
def gn_qs_qd(qs,qd):
    return 1/6*(4*qs**2+3*qs+4*qs*qd+3*qd+4*qd**2)/(qs+qd+1)

# Thermal noise conductance in strong inversion (long-channel)
def gn_qs_qd_si(qs,qd):
    return 2/3*(qs**2+qs*qd+qd**2)/(qs+qd)

# Thermal noise parameter in strong inversion (long-channel)
def deltan_qs_qd_si(qs,qd):
    gn=gn_qs_qd_si(qs,qd)
    gdso=qs
    return gn/gdso

# Thermal noise parameter (long-channel)
def deltan_qs_qd(qs,qd):
    gn=gn_qs_qd(qs,qd)
    gdso=qs
    return gn/gdso

# Thermal noise parameter (long-channel)
def deltan_ic(ic):
    qs=q_ic(ic)
    return 2/3*(qs+3/4)/(qs+1)

# Thermal noise excess factor (long-channel)
def gamman_ic(ic,n):
    return n*deltan_ic(ic)

# Fano suppression factor (long-channel)
def fano_ic(ic):
    return 2*deltan_ic(ic)*gmsid_ic(ic)

#---------------
# Short-channel
#---------------

# Thermal noise conductance (short-channel)
def gnsat_qs(qs,lc):
    qdsat=qdsat_qs(qs,lc)
    num=4*(qs**2+qs*qdsat+qdsat**2)+3*qs
    den=6*(qs+qdsat+1)
    return num/den

# Thermal noise parameter (short-channel)
def deltansat_qs(qs,lc):
    gnsat=gnsat_qs(qs,lc)
    gdso=qs
    return gnsat/gdso

# Thermal noise excess factor including short-channel effects
def gamman_ic_short(ic,n,lc):
    return gamman_ic(ic,n)*(1+3/4*lc**2*ic)

# Thermal noise excess factor including short-channel effects
def gammansat_qs(qs,n,lc):
    gnsat=gnsat_qs(qs,lc)
    gm=gms_q_short(qs,lc)/n
    return gnsat/gm

# Input-referred thermal noise resistance including short-channel effects
def rnsat_ic(ic,n,lc):
    gammansat=gamman_ic_short(ic,n,lc)
    gm=gms_ic_short(ic,lc)/n
    return gammansat/gm

# Fano suppression factor including short-channel effects
def fano_ic_short(ic,n,lc):
    return 2*gamman_ic_short(ic,n,lc)/n*gmsid_ic_short(ic,lc)

##########################
# Intrinsic capacitances #
##########################

# Intrinsic GS and GD capacitance (long-channel)
def cc_qs_qd(qs,qd):
    num=2*qs+4*qd+3
    den=(qs+qd+1)**2
    return qs/3*num/den

# Intrinsic GS capacitance in saturation (long-channel)
def cgsi_ic(ic):
    qs=q_ic(ic)
    qd=0
    return cc_qs_qd(qs,qd)
   
# Intrinsic GB capacitance in saturation (long-channel)
def cgbi_ic(ic,n):
    cgsi=cgsi_ic(ic)
    return (n-1)/n*(1-cgsi)

def cbsi_ic(ic,n):
    cgsi=cgsi_ic(ic)
    return (n-1)*cgsi