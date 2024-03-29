# ADDA tutorial code

# Run scripts
- [run_ellipsoid](run_ellipsoid): simple script to run ADDA with mpi for an ellipsoid.
- [run_fromfile](run_fromfile): script to run ADDA with mpi for a pregenerated [shape file](../data/crystal_0000_3.0.txt).

# Python utilities
- [calc_scat.py](calc_scat.py): script to calculate radar scattering properties from ADDA output of scattering amplitude matrices.
- [make_crystal_dda.py](make_crystal_dda.py): script to generate an ADDA-formated input branched-planar crystal shape file. Requires the [crystal_dda](https://github.com/rskschrom/crystal_dda) package.
- [single_particle.py](single_particle.py): module containing functions to compute polarizabilities of ellipsoids with the Rayleigh approximation. Useful to compare with ADDA results.
