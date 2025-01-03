#!/bin/csh -f
#TEST-PROGRAM sander
#TEST-DESCRIP TO_BE_DEtermined
#TEST-PURPOSE regression, basic
#TEST-STATE   undocumented

# script is supposed to be called from Makefile with: Run.min $(FBLIBS)
if(  "x$1" == "x" ) then
    echo 'Not compiled with Fireball - Skipping Test...'
    exit(0)
endif

# basis must be installed in $AMBERHOME/test/qmmm_EXTERN/QMMM_Fireball/Fdata_HCNOS
set BASIS = '../Fdata_HCNOS'
if ( -d $BASIS ) then
    set found = 'true'
else
    echo 'Fireball Fdata_HCNOS not found - Skipping Test...'
    exit(0)
endif

set sander = "${AMBERHOME}/bin/sander"
if( $?TESTsander ) then
    set sander = $TESTsander
endif

if( ! $?DO_PARALLEL ) then
    setenv DO_PARALLEL " "
endif

cat > mdin <<EOF
QM/MM 
 &cntrl
 ntx = 7, irest = 1, ntrx = 1,
 ntxo = 1, nmropt = 0, ntr = 0,
 ntpr = 1, ntwx = 1,
 ntf = 1,  ntc = 1, ntb = 0, ivcap = 0,
 cut = 10,imin = 0, nstlim = 10, dt = 0.0005,
 ntc = 2, temp0 = 300.0, tempi = 300.0,
 ntt = 2,
 ifqnt = 1
 &end
/
 &qmmm
 qmmask= '@546-569'
 qm_theory='extern'
 qm_ewald= 0,
 qmshake= 0 
 qmcharge= 0,
/
 &fb
 basis= '$BASIS'
/
EOF

touch dummy

$DO_PARALLEL $sander -O -i mdin -p thym_qmmm.prmtop -c thym_qmmm.inpcrd < dummy > fireball.out || goto error

../../../dacdif mdout.save mdout
../../../dacdif restrt.save restrt

/bin/rm -f dummy mdin mdinfo mdout mdcrd restrt fireball.in input.bas param.dat fireball.out CHARGES
exit(0)

error:
echo "  ${0}:  Program error"
exit(1)







