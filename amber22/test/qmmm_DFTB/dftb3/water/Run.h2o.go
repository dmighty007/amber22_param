#!/bin/csh -f
#TEST-PROGRAM sander
#TEST-DESCRIP TO_BE_DEtermined
#TEST-PURPOSE regression, basic
#TEST-STATE   undocumented

set sander = "${AMBERHOME}/bin/sander"
if( $?TESTsander ) then
    set sander = $TESTsander
endif

if( $?DO_PARALLEL ) then
   echo "This test not set up for parallel"
   exit 0
endif

../../../check_slko_files.x DFTB3
if( $status > 0) then
  exit(0)
endif

cat > mdin <<EOF
Geometry optimization with DFTB3
 &cntrl
  imin=1,     ! do a minimization
  ntmin=3,    ! xmin minimizer
  maxcyc=50,  ! max 50 minimization steps
  drms=0.05,  ! RMS gradient convergence criterium 0.5 (kcal/mol)/A = 2.d-4 au
  cut=9999.0, ! non-bonded cutoff (irrelevant for now with pure QM)
  ntb=0,      ! no periodic boundary conditions
  ntc=1,      ! no SHAKE
  ntpr=1,     ! print every minimization step
  ntwx=1,     ! write coordinates each step
  ntwr=50,    ! write restart file each 50 steps
  ioutfm = 1, ! NetCDF MDCRD.
  ntxo   = 1,           !Formatted restart file
  ifqnt=1     ! do QM/MM
 /
 &qmmm
  qmmask    ='@*',
  qmcharge  = 0,
  qm_theory ='DFTB3',
  scfconv = 1.0d-08,
  verbosity = 0,
 /
EOF

set output = h2o.go.out
rm -f $output

touch dummy
$sander -O -p h2o.prmtop -c h2o.inpcrd -o $output < dummy || goto error

../../../dacdif $output.save $output

/bin/rm -f dummy mdin mdinfo mdcrd dummy restrt
exit(0)

error:
echo "  ${0}:  Program error"
exit(1)







