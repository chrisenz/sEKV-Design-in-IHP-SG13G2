# This includes all the functions used for the EKV MOSFET model
# Redefine the log functions
import numpy as np
from numpy import pi as pi
from numpy import log as ln
from numpy import log10 as log
from numpy import sqrt as sqrt
from numpy import exp as exp
from numpy import arctan as atan

#--------------------------------------------------
# Large-signal normalized functions
#--------------------------------------------------

# Normalized drain current versus charge
def iq(q):
    return q*(q+1)

# Normalized charge versus current
def qi(i):
    return (sqrt(4*i+1)-1)/2

# Normalized saturation voltage vp-v versus the normalized charge
def vq(q):
    return 2*q+ln(q)

def vi(i):
    q=qi(i)
    return 2*q+ln(q)

# Inverse function giving q(v) corresponding to the inverse function of v(q) using the Lambert W-function
from scipy.special import lambertw
def qv(v):
    return np.real(lambertw(2*exp(v))/2)

# Inverse function giving q(v) corresponding to the inverse function of v(q) using the EKV 2.6 approximation
def qvapprox(v):
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

# Normalized saturation voltage vp-vs versus the normalized charge
def vps_ic(ic):
    return ln(sqrt(4*ic+1)-1)+sqrt(4*ic+1)-1-ln(2)

# Inversion coefficient as a function of the normalized saturation voltage vp-vs
def ic_vps(vps):
    return iq(qv(vps))

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

#--------------------------------------------------
# Small-signal normalized functions
#--------------------------------------------------

# Source transconductance versus inversion coefficient (long-channel)
def gms_ic_long(ic):
    return (sqrt(4*ic+1)-1)/2

# Normalized Gm/ID function versus inversion coefficient (long-channel)
def gmsid_ic_long(ic):
    return gms_ic_long(ic)/ic

# Normalized ID/Gm function (long-channel)
def idgms_ic_long(ic):
    return 1/gmsid_ic_long(ic)

# Inverse normalized Gm/ID function (long-channel)
def ic_gmid(gmsid):
    return ((2/gmsid-1)**2-1)/4

# Source transconductance versus inversion coefficient (short-channel)
def gms_ic(ic,lc):
    num=sqrt(4*ic+1+(lc*ic)**2)-1
    den=2+lc**2*ic
    return num/den

# Normalized Gm/ID function versus inversion coefficient (short-channel)
def gmsid_ic(ic,lc):
    return gms_ic(ic,lc)/ic

# Normalized ID/Gm function versus inversion coefficient (short-channel)
def idgms_ic(ic,lc):
    return 1/gmsid_ic(ic,lc)

# Normalized bias current versus IC of CS stage including self-loading
def ib_ic_long(ic,theta):
    IClim=theta*(1+theta)
    if ic<IClim:
        ib=float("nan")
    else:
        gms=gms_ic_long(ic)
        ib=ic/(gms-theta)
    return ib

# Normalized aspect ratio versus IC of CS stage including self-loading
def ar_ic_long(ic,theta):
    IClim=theta*(1+theta)
    if ic<IClim:
        ar=float("nan")
    else:
        gms=gms_ic_long(ic)
        ar=1/(gms-theta)
    return ar

# Thermal noise excess factor (long-channel)
def delta_ic(ic):
    qs=qi(ic)
    return 2/3*(qs+3/4)/(qs+1)

#--------------------------------------------------
# Intrinsic capacitances
#--------------------------------------------------

# Intrinsic GS and GD capacitance (long-channel)
def cc_qs_qd(qs,qd):
    num=2*qs+4*qd+3
    den=(qs+qd+1)**2
    return qs/3*num/den

# Intrinsic GS capacitance in saturation (long-channel)
def cgsi_ic(ic):
    qs=qi(ic)
    qd=0
    return cc_qs_qd(qs,qd)
   
# Intrinsic GB capacitance in saturation (long-channel)
def cgbi_ic(ic,n):
    cgsi=cgsi_ic(ic)
    return (n-1)/n*(1-cgsi)

def cbsi_ic(ic,n):
    cgsi=cgsi_ic(ic)
    return (n-1)*cgsi

#--------------------------------------------------
# NQS time constant
#--------------------------------------------------

# Intrinsic gate transcapacitance (long-channel)
def cm_qs_qd(qs,qd):
    num=(qs-qd)*(4*qs**2+4*q**2+12*qs*qd+10*qs+10*qd+5)
    den=15*(qs+qd+1)**3
    return num/den

# Intrinsic gate transcapacitance in saturation (long-channel)
def cm_ic(ic):
    qs=qi(ic)
    qd=0
    return cm_qs_qd(qs,qd)
