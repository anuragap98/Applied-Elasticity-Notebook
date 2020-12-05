from sympy import *
from IPython.display import Math, Latex

r, theta = symbols('r, theta')

delr_delx = cos(theta)

delr_dely = sin(theta)

deltheta_delx = -sin(theta)/r

deltheta_dely = cos(theta)/r

def del_delx(f):
    return delr_delx*diff(f,r) + deltheta_delx*diff(f,theta)

def del_dely(f):
    return delr_dely*diff(f,r) + deltheta_dely*diff(f,theta)

def del2_delx2(f):
    return del_delx(del_delx(f))

def del2_dely2(f):
    return del_dely(del_dely(f))

def polarLapacian(f):
    return (del2_delx2(f) + del2_dely2(f)).simplify()

def  polarbiharmonic(f):
    return polarLapacian(polarLapacian(f))

def sigma_xx(f):
    return del2_dely2(f)

def sigma_yy(f):
    return del2_delx2(f)

def sigma_xy(f):
    return -del_delx(del_dely(f))

def sigma_rect(f):
    return Matrix([[sigma_xx(f), sigma_xy(f)],[sigma_xy(f), sigma_yy(f)]])

Q = Matrix([[cos(theta), sin(theta)],[-sin(theta), cos(theta)]])

def sigma_polar(f):
    return Q*sigma_rect(f)*(Q.T)

def sigma_rr(f):
    return sigma_polar(f)[0,0].simplify().expand()

def sigma_tt(f):
    return sigma_polar(f)[1,1].simplify()

def sigma_rt(f):
    return sigma_polar(f)[0,1].simplify().expand()

def sigma_tr(f):
    return sigma_polar(f)[1,0].simplify().expand()