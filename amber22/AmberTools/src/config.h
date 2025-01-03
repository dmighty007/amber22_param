
# Compatibility config.h generated by the CMake build system

###############################################################################

# (1)  Location of the installation

BASEDIR=/home/suman/Dibyendu/Soft/amber22_src/amber22_src/build
AMBER_PREFIX=/home/suman/Dibyendu/Soft/amber22_src/amber22//
BINDIR=$(AMBER_PREFIX)/bin
LIBDIR=$(AMBER_PREFIX)/lib
INCDIR=$(AMBER_PREFIX)/include
DATDIR=$(AMBER_PREFIX)/dat
LOGDIR=$(AMBER_PREFIX)/logs
AMBER_SOURCE=$(AMBERHOME)

###############################################################################

FLIBS=-L/home/suman/Dibyendu/Soft/amber22_src/amber22_src/build/AmberTools/src/xblas/build -L/usr/lib64 -L/home/apps/spack/opt/spack/linux-almalinux8-cascadelake/gcc-12.2.0/miniconda3-24.3.0-253ehl37flystewbyl6ye5bputnscfhw/lib -lz -lm -lnetcdf -lblas -lxblas-amb -lblas -llapack -lxblas-amb -lblas -llapack -lblas -larpack -lm -lpthread -lm -lfftw3 -lblas -lxblas-amb -lblas -llapack -lxblas-amb -lblas -llapack -lblas -larpack -lm -lz -lm -lnetcdf -lnetcdff -lz -lm -lnetcdf -lamber_common -lxblas-amb -lrism -lsff -lpthread -lm -lfftw3 -lblas -lxblas-amb -lblas -llapack -lxblas-amb -lblas -llapack -lblas -larpack -lm -lz -lm -lnetcdf -lnetcdff -lz -lm -lnetcdf -lamber_common -lz -lm -lnetcdf -lnetcdff -lz -lm -lnetcdf -lpbsa -lpthread -lm -lfftw3 -lblas -lxblas-amb -lblas -llapack -lxblas-amb -lblas -llapack -lblas -larpack -lm -lz -lm -lnetcdf -lnetcdff -lz -lm -lnetcdf -lamber_common -lxblas-amb -lrism -lfftw3 -lblas -lxblas-amb -lblas -llapack -lxblas-amb -lblas -llapack -lblas -larpack -lm -lz -lm -lnetcdf
FLIBSF=-L/usr/lib64 -L/home/suman/Dibyendu/Soft/amber22_src/amber22_src/build/AmberTools/src/xblas/build -lblas -lxblas-amb -lblas -llapack -lxblas-amb -lblas -llapack -lblas -larpack -lm -lxblas-amb
FLIBS_MPI=-L/home/apps/spack/opt/spack/linux-almalinux8-cascadelake/gcc-13.2.0/intel-oneapi-mpi-2021.13.0-vufnfy5m34auafv54sqkf4d6iza6ohhc/mpi/2021.13/lib -L/home/suman/Dibyendu/Soft/amber22_src/amber22_src/build/AmberTools/src/xblas/build -L/usr/lib64 -L/home/apps/spack/opt/spack/linux-almalinux8-cascadelake/gcc-12.2.0/miniconda3-24.3.0-253ehl37flystewbyl6ye5bputnscfhw/lib -lz -lm -lnetcdf -lblas -lxblas-amb -lblas -llapack -lxblas-amb -lblas -llapack -lblas -larpack -lm -Xlinker --enable-new-dtags -Xlinker -lmpi -lrt -lpthread -ldl -Xlinker --enable-new-dtags -Xlinker -lmpifort -lmpi -lrt -lpthread -ldl -lpthread -lm -lfftw3 -lblas -lxblas-amb -lblas -llapack -lxblas-amb -lblas -llapack -lblas -larpack -lm -lz -lm -lnetcdf -lnetcdff -lz -lm -lnetcdf -lamber_common -lxblas-amb -Xlinker --enable-new-dtags -Xlinker -lmpifort -lmpi -lrt -lpthread -ldl -lpthread -lm -lfftw3 -Xlinker --enable-new-dtags -Xlinker -lmpi -lrt -lpthread -ldl -lfftw_mpi -lrism_mpi -lsff_mpi -lpbsa_mpi -lpthread -lm -lfftw3 -lblas -lxblas-amb -lblas -llapack -lxblas-amb -lblas -llapack -lblas -larpack -lm -lz -lm -lnetcdf -lnetcdff -lz -lm -lnetcdf -lamber_common -lxblas-amb -Xlinker --enable-new-dtags -Xlinker -lmpifort -lmpi -lrt -lpthread -ldl -lpthread -lm -lfftw3 -Xlinker --enable-new-dtags -Xlinker -lmpi -lrt -lpthread -ldl -lfftw_mpi -lrism_mpi -lfftw3_mpi -lfftw3 -lblas -lxblas-amb -lblas -llapack -lxblas-amb -lblas -llapack -lblas -larpack -lm -lz -lm -lnetcdf

###############################################################################

BUILDAMBER=amber
SHELL=/usr/bin/bash

CC=/usr/bin/gcc
CFLAGS= -Wall -Wno-unused-function -Wno-unknown-pragmas -Wno-unused-variable -Wno-unused-but-set-variable
CNOOPTFLAGS=
COPTFLAGS=-O3 -mtune=native

CXX=/usr/bin/g++
CXXFLAGS= -Wall -Wno-unused-function -Wno-unknown-pragmas -Wno-unused-local-typedefs -Wno-unused-variable -Wno-unused-but-set-variable
CXXNOOPTFLAGS=
CXXOPTFLAGS=-O3 -mtune=native

MV=mv
RM=rm
CP=cp

FC=/usr/bin/gfortran
FFLAGS= -Wall -Wno-tabs -Wno-unused-function -ffree-line-length-none -Wno-unused-dummy-argument -Wno-unused-variable
FNOOPTFLAGS=
FOPTFLAGS=-O3 -mtune=native

# pmemd.gem is always enabled in NetCDF builds
PMEMD_GEM=yes

#QUICK
QUICK=no

#TCPB
TCPB=no

# reaxff-puremd
REAXFF_PUREMD=no

LDFLAGS=

# NetCDF is always enabled in CMake builds
NETCDF=yes

EMIL=EMIL

FEP_MODE=gti

COMPILER=GNU
MKL=

PYTHON=/home/suman/.conda/envs/amber/bin/python
SKIP_PYTHON=no

# OS-specific rules for making shared objects
SHARED_SUFFIX=.so

# used by tests
INSTALLTYPE=parallel
TESTRISMSFF=testrism
FEP_MODE=gti
