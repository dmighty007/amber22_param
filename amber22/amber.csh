# Source this script to define the environment variables necessary to use Amber.
# This script must be located in the Amber root folder!

# Amber was configured on 2024-12-30 at 19:29:09

set myname = 'amber.csh'

# Incomplete path coverage, but may catch novice user attempts:
if ( "$0" == "$myname" || "$0" == ./"$myname" ) then
        echo "Warning:  $myname is not a script; it should be sourced not executed!"
        echo "          Use it like this:  source $myname"
endif

if ( "$0" !~ '*csh' ) then
        echo "Warning:  $myname is a C shell source file!"
        echo "          Your shell does not appear to be a C shell:  $0"
endif

# Get path used for this source file (credit scott brozell).
set invocationpath = `echo $_ | cut -d' ' -f2- | sed "s@$myname.*@@"`
if ( "$invocationpath" == '' ) then
        set invocationpath = '.'
endif

setenv AMBERHOME `cd "$invocationpath" >&! /dev/null; pwd`
setenv PATH "$AMBERHOME/bin:$PATH"

# Add Amber lib folder to LD_LIBRARY_PATH (if platform supports it).  Note that
# LD_LIBRARY_PATH is necessary for nab and mpinab; it may help Amber's Python
# programs find their dynamic libraries, and it may be useful if Amber has been
# moved from where it was installed.
if ( 1 == 1 ) then
	if ( $?LD_LIBRARY_PATH ) then
		setenv LD_LIBRARY_PATH "$AMBERHOME/lib:$LD_LIBRARY_PATH"
	else
		setenv LD_LIBRARY_PATH "$AMBERHOME/lib"
	endif
endif

# Add location of Amber Perl modules to default Perl search path
# (if platform supports it).
if ( 1 == 1 ) then
	if ( $?PERL5LIB ) then
		setenv PERL5LIB "$AMBERHOME/lib/perl:$PERL5LIB"
	else
		setenv PERL5LIB "$AMBERHOME/lib/perl"
	endif
endif

# Add location of Amber Python modules to default Python search path
# (if platform supports it).
if ( $?PYTHONPATH ) then
	setenv PYTHONPATH "$AMBERHOME/lib/python3.10/site-packages:$PYTHONPATH"
else
	setenv PYTHONPATH "$AMBERHOME/lib/python3.10/site-packages"
endif

# Tell QUICK where to find its data files
if ( 0 == 1 ) then
	setenv QUICK_BASIS "$AMBERHOME/AmberTools/src/quick/basis"
endif
