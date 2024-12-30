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
endif

touch dummy
$DO_PARALLEL $sander -O < dummy || goto error
../../dacdif  mdout.save mdout

/bin/rm -f mdinfo mdcrd dummy restrt
exit(0)

error:
echo "  ${0}:  Program error"
exit(1)
