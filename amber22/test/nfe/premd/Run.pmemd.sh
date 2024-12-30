#!/bin/bash
#TEST-PROGRAM sander
#TEST-DESCRIP TO_BE_DEtermined
#TEST-PURPOSE regression, basic
#TEST-STATE   undocumented

. ../common.sh

set_SANDER pmemd.MPI
set_SANDER_CMD 4

JUNK="mdout.? restrt.? pmd.?.txt groups prmtop sander.out *.log *.type logfile.*"

#
# remove the junk
#

/bin/rm -rf ${JUNK} junk.*

#
# prepare files
#

cp -p ../prmtop ../groups .

#
# run SANDER
#

${SANDER_CMD} -ng 4 -rem 3 -groupfile groups > sander.out 2>&1
CheckError $?

../../dacdif save/rem.log rem.log

for i in 1 2 3 4; do
    ../../dacdif -t 1 save/pmd.$i.txt.pmemd pmd.$i.txt
    ../../dacdif -t 1 save/mdout.$i.pmemd mdout.$i
done

#
# preserve the junk on failure
#

save_junk_on_failure ${JUNK}

#
# remove the junk
#

/bin/rm -f ${JUNK} profile_mpi
