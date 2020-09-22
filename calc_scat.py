import numpy as np
from single_particle import ellipsoid_polz

# read amplitude scattering matrix output file
data = np.genfromtxt('ellipsoid_output/ampl_scatgrid', skip_header=1)
theta = data[:,0]
phi = data[:,1]
s1 = data[:,2]+1j*data[:,3]
s2 = data[:,4]+1j*data[:,5]
s3 = data[:,6]+1j*data[:,7]
s4 = data[:,8]+1j*data[:,9]

# get data at backscatter and forward scatter
bs_ind = (theta==180.)&(phi==0.)
fs_ind = (theta==0.)&(phi==0.)
s1_bs = s1[bs_ind][0]
s2_bs = s2[bs_ind][0]
s3_bs = s3[bs_ind][0]
s4_bs = s4[bs_ind][0]

s1_fs = s1[fs_ind][0]
s2_fs = s2[fs_ind][0]
s3_fs = s3[fs_ind][0]
s4_fs = s4[fs_ind][0]

# convert to radar met. convention (for parallel=h, perpendicular=v)
wavl = 32.1
k = 2.*np.pi/wavl
shh_bs = s2_bs/(-1j*k)
svv_bs = s1_bs/(-1j*k)

shh_fs = s2_fs/(-1j*k)
svv_fs = s1_fs/(-1j*k)

# test zdr
zdr = 10.*np.log10(np.abs(shh_bs)**2./np.abs(svv_bs)**2.)
print(zdr)

# compare to rayleigh
m = 1.78
a = 0.5
phi_ba = 0.5
phi_ca = 0.2
b = a*phi_ba
c = a*phi_ca
alp_a, alp_b, alp_c = ellipsoid_polz(m**2., a, b, c)

shh = k**2./(4.*np.pi)*alp_a
svv = k**2./(4.*np.pi)*alp_c

print(shh, shh_fs)
print(svv, svv_fs)
