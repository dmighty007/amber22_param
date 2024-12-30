#!/bin/csh -f
#TEST-PROGRAM sander
#TEST-DESCRIP TO_BE_DEtermined
#TEST-PURPOSE regression, basic
#TEST-STATE   undocumented

if( ! $?TESTsander ) set TESTsander = "$AMBERHOME/bin/sander"
set DACDIF="$AMBERHOME/test/dacdif -a 0.0002"

if( ! $?DO_PARALLEL ) then
        setenv DO_PARALLEL " "
endif

set FILE = min
set TOP = mol.prmtop
set INCRD = mol.inpcrd

$DO_PARALLEL $TESTsander -O -i ${FILE}.in \
        -o ${FILE}.out \
        -p ${TOP} \
        -c ${INCRD} \
        -r ${FILE}.rst \
        -x ${FILE}.crd \
        -v ${FILE}.vel \
        -e ${FILE}.ene \
        -inf ${FILE}.mdinfo || goto error

$DACDIF ${FILE}.out.save ${FILE}.out
/bin/rm -f ${FILE}.rst ${FILE}.mdinfo ${FILE}.crd  divcon.in divcon.out
exit(0)

error:
echo "  ${0}:  Program error"
exit(1)


