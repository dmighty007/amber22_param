#!/bin/csh -f
#TEST-PROGRAM sander
#TEST-DESCRIP TO_BE_DEtermined
#TEST-PURPOSE regression, basic
#TEST-STATE   undocumented

set sander = "${AMBERHOME}/bin/sander"
if( $?TESTsander ) then
    set sander = $TESTsander
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
  cut    = 8.0,         !non-bonded interactions cutoff
  dt     = 0.0005,      !0.5fs time step
  ntb    = 1,           !PBC
  ntc=1,      ! no SHAKE
  ntpr   = 1,           !print details to log every step
  ntwx   = 1,           !write coordinates to mdcrd every step
  ntwr   = 10,          !write restart file at last step
  nstlim = 10,          !run for 10 steps (5 fs at dt=0.5fs)
  jfastw   = 4,         ! do not use routines for fast triangulated water
  ioutfm = 1,           !NetCDF MDCRD.
  ntxo   = 1,           !Formatted restart file
  ifqnt  = 1,
 /
 &qmmm
  qmmask    = ':1-2',
  qmcharge  = 0,
  qm_theory = 'dftb3',
  verbosity = 0,
 /
EOF

set name = nma-spcfw-15
set prmtop = $name.prmtop
set inpcrd = $name.inpcrd
set output = $name.md.out
rm -f $output

touch dummy
$sander -O -p $prmtop -c $inpcrd -o $output < dummy || goto error

# remove info about number of threads from output as this may vary
grep -v 'num_threads' $output > tmp
mv tmp $output

../../../dacdif -a 0.0002 $output.save $output

/bin/rm -f dummy mdin mdinfo mdcrd dummy restrt
exit(0)

error:
echo "  ${0}:  Program error"
exit(1)







