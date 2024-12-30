#!/bin/bash

# AWG 3/20/2017
#
# TIP3P coordinates of water taken from
# $AMBERHOME/dat/leap/lib/solvents.lib, !entry.TP3.unit.positions
#
# CreatVirtualSites.py script by Rodrigo Ferreira de Morais, modified
# to add only virtual sites, not rod particles
#
python CreatVirtualSites.py \
       Pt111_6l_6R3x9_H2O.pdb Pt PythonPDB \
       2.77483 0.7 2.0 .9572 0.0 0.0 -0.239988 -.926627 0.0

tleap -f leap.inp
