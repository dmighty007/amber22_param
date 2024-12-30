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
10 steps NVE pure QM MD (dt=0.5fs, no shake)
 &cntrl
  imin   = 0,           !no minimization
  irest  = 1,           !restart
  ntx    = 5,           !read coordinates and velocities
  cut    = 9999.9       !non-bonded interactions cutoff
  dt     = 0.0005,      !0.5fs time step
  ntb    = 0,           !no periodicity and PME off!
  ntc=1,      ! no SHAKE
  ntpr   = 1,           !print details to log every 10 steps (every 5fs)
  ntwx   = 1,           !write coordinates to mdcrd every 10 steps (every 5fs)
  ntwr   = 10,          !write restart file at last step
  nstlim = 10,          !run for 2 steps (1 fs at dt=0.5fs)
  nscm   = 0,           !No removal of COM motion,
  ioutfm = 1,           !NetCDF MDCRD.
  ntxo   = 1,           !Formatted restart file
  ifqnt  = 1,
 /
 &qmmm
  qmmask    = '@*',
  qmcharge  = 0,
  qm_theory = 'dftb3',
  verbosity = 0,
 /
EOF

set output = h2o.md.out
rm -f $output

touch dummy
$sander -O -p h2o.prmtop -c h2o.inpcrd -o $output < dummy || goto error

../../../dacdif -a 0.0002 $output.save $output

/bin/rm -f dummy mdin mdinfo mdcrd dummy restrt
exit(0)

error:
echo "  ${0}:  Program error"
exit(1)







