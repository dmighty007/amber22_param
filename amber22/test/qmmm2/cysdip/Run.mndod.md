#!/bin/csh -f
#TEST-PROGRAM sander
#TEST-DESCRIP TO_BE_DEtermined
#TEST-PURPOSE regression, basic
#TEST-STATE   undocumented

set sander = "${AMBERHOME}/bin/sander"
if( $?TESTsander ) then
    set sander = $TESTsander
endif

if( ! $?DO_PARALLEL ) then
    setenv DO_PARALLEL " "
else
    echo "This test not set up for parallel"
    echo "need #nres>#nproc"
    exit 0
endif

touch dummy
set TEST = mndod.md
set MDIN = $TEST.mdin
set MDOUT = $TEST.mdout
set MDCRD = $TEST.mdcrd
$DO_PARALLEL $sander -O -i $MDIN -o $MDOUT -x $MDCRD < dummy || goto error
../../dacdif -r 5.e-4 $MDOUT.save $MDOUT
../../dacdif $MDCRD.save $MDCRD

/bin/rm -f mdin mdinfo dummy restrt
exit(0)

error:
echo "  ${0}:  Program error"
exit(1)









