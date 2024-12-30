#!/bin/csh -f

echo "*** NMA Dihedral Linear Algorithm Perfect Fit ***"


$AMBERHOME/bin/paramfit -i Job_Control.in -p NMA.prmtop -c mdcrd -q amber_energy --random-seed 5000 > prog_out.txt

# Diff only the second energy column of the generated energy data file.
awk 'BEGIN{FS="\t"}{print $3}' < energy.dat > energy.out
../../dacdif saved_output/energy.out.saved energy.out
../../dacdif saved_output/frcmod.saved frcmod
/bin/rm -f energy.dat prog_out.txt

exit(0)

error:
echo "  ${0}: Program error"
exit(1)

