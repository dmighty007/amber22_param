######################################################################################## 
#       Code to format PDB files and add 2 new virtual sites for each selected atom    #
#	   and 1 Rod								       #
#       by Rodrigo Ferreira de Morais                                                  #
#       Date: 04/02/2016                                                               #
# modified by AWG on 3/20/2017
########################################################################################

#!/usr/bin/python

import sys
from numpy import sqrt

###################### Functions #############################################
def CreatPoscar(AtomList,AtomN,Output,dist,AdzIC):
    
    File=open(Output+'.pdb',"w\n")

    count=1
    resd=1

    xmax=0.0
    ymax=0.0
    zmax=0.0
    zmin=1000.0

    for i in range(0,len(AtomList)):
	if  AtomList[i].split()[0]=='ATOM' and AtomList[i].split()[2]==AtomN:
                if zmin>float(AtomList[i].split()[7]):
                        zmin=float(AtomList[i].split()[7])
		if xmax<float(AtomList[i].split()[5]):
			xmax=float(AtomList[i].split()[5])
		if ymax<float(AtomList[i].split()[6]):
                	ymax=float(AtomList[i].split()[6])
		if zmax<float(AtomList[i].split()[7]):
			zmax=float(AtomList[i].split()[7])


    COD = [[ 8.779,   9.753],
[ 8.777,   1.403],
[23.238,   9.805],
[23.235,   1.455],
[23.226,  18.095],
[16.044,   5.546],
[ 1.612,   5.606],
[16.044,  13.834],
[ 1.624,  13.835],
[16.076,  22.163],
[ 1.624,  22.163],
[ 8.768,  18.043]]

   #COD = [[10.702, 9.712]] 

##### Add the oxygen for water

        #if AtomList[i].split()[0]=='ATOM' and AtomList[i].split()[2]=='O':
    for c in range(0,len(COD)):
                File.write("%s %6i %s    %s %6i     %6.3f  %6.3f  %6.3f %5.2f %5.2f          %s\n"%\
                                 ("ATOM",\
                                  count,\
                                  "O",\
                                  "TP3",\
                                  resd,\
                                  float(COD[c][0]),\
                                  float(COD[c][1]),\
                                  float(sys.argv[6])+zmax,\
                                  1.00,\
                                  0.00,\
                                  "O"))
                count=count+1


######  Add the hydrogen for water

                File.write("%s %6i %s   %s %6i     %6.3f  %6.3f  %6.3f %5.2f %5.2f          %s\n"%\
                                 ("ATOM",\
                                  count,\
                                  "H1",\
                                  "TP3",\
                                  resd,\
                                  float(sys.argv[7])+float(COD[c][0]),\
                                  float(sys.argv[8])+float(COD[c][1]),\
                                  float(sys.argv[9])+float(sys.argv[6])+zmax,\
                                  1.00,\
                                  0.00,\
                                  "H1"))
                count=count+1



                File.write("%s %6i %s   %s %6i     %6.3f  %6.3f  %6.3f %5.2f %5.2f          %s\n"%\
                                 ("ATOM",\
                                  count,\
                                  "H2",\
                                  "TP3",\
                                  resd,\
                                  float(sys.argv[10])+float(COD[c][0]),\
                                  float(sys.argv[11])+float(COD[c][1]),\
                                  float(sys.argv[12])+float(sys.argv[6])+zmax,\
                                  1.00,\
                                  0.00,\
                                  "H2"))
                count=count+1
                resd=resd+1

    for i in range(0,len(AtomList)):
#####
##### Add the real sites
#####

	if AtomList[i].split()[0]=='ATOM' and AtomList[i].split()[2]==AtomN:
		File.write("%s %6i %s   %s %6i     %6.3f  %6.3f  %6.3f %5.2f %5.2f          %s\n"%\
				(AtomList[i].split()[0],\
				count,\
				AtomList[i].split()[2],\
				AtomList[i].split()[3],\
				resd,\
				float(AtomList[i].split()[5]),\
				float(AtomList[i].split()[6]),\
				float(AtomList[i].split()[7]),\
				float(AtomList[i].split()[8]),\
				float(AtomList[i].split()[9]),\
				AtomList[i].split()[10]))
		count=count+1
#		resd=resd+1

#####
#####  Add the dummy atoms for the Rod model
#####

#AWG DO NOT ADD ROD PARTICLES
#AWG
#AWG		if float(AtomList[i].split()[7])==zmax:
#AWG			zIC=float(AtomList[i].split()[7])-AdzIC
#AWG		else:
#AWG			zIC=float(AtomList[i].split()[7])+AdzIC	
#AWG
#AWG                File.write("%s %6i %s   %s %6i     %6.3f  %6.3f  %6.3f %5.2f %5.2f          %s\n"%\
#AWG				 (AtomList[i].split()[0],\
#AWG				  count,\
#AWG				  " H",\
#AWG				  AtomList[i].split()[3],\
#AWG				  resd,\
#AWG				  float(AtomList[i].split()[5]),\
#AWG				  float(AtomList[i].split()[6]),\
#AWG				  zIC,\
#AWG				  float(AtomList[i].split()[8]),\
#AWG				  float(AtomList[i].split()[9]),\
#AWG				  AtomList[i].split()[10]))
#AWG                count=count+1
		resd=resd+1

		File.write("TER\n")

#####
##### Add the virtual sites only if it is inside the box
#####
    for i in range(0,len(AtomList)):

	if AtomList[i].split()[0]=='ATOM' and AtomList[i].split()[2]==AtomN:


		newyVS1 = float(AtomList[i].split()[6]) + dist/2
		newxVS1 = float(AtomList[i].split()[5]) + (dist*sqrt(3))/6
                newxVS2 = float(AtomList[i].split()[5]) + (dist*sqrt(3))/3

		if float(AtomList[i].split()[7])==zmax or float(AtomList[i].split()[7])==zmin:
#			if ymax>newyVS1 and xmax>newxVS1:

				File.write("%s %6i %s   %s %6i     %6.3f  %6.3f  %6.3f %5.2f %5.2f          %s\n"%\
					  	(AtomList[i].split()[0],\
						count,\
						'VS',\
						"MVS",\
						resd,\
						newxVS1,\
						newyVS1,\
						float(AtomList[i].split()[7]),\
						float(AtomList[i].split()[8]),\
						float(AtomList[i].split()[9]),\
						AtomList[i].split()[10]))

				count=count+1
				resd=resd+1

#			if xmax>newxVS2:

				File.write("%s %6i %s   %s %6i     %6.3f  %6.3f  %6.3f %5.2f %5.2f          %s\n"%\
						 (AtomList[i].split()[0],\
						  count,\
						  'VS',\
						  "MVS",\
					 	  resd,\
						  newxVS2,\
						  float(AtomList[i].split()[6]),\
						  float(AtomList[i].split()[7]),\
						  float(AtomList[i].split()[8]),\
						  float(AtomList[i].split()[9]),\
						  AtomList[i].split()[10]))

				count=count+1
				resd=resd+1

#    if len(sys.argv)>6:
#		File.write("%s %6i %s   %s %6i     %6.3f  %6.3f  %6.3f %5.2f %5.2f          %s\n"%\
#                                                ("ATOM",\
#                                                 count,\
#                                                 'qT',\
#                                                 "QTS",\
#                                                 resd,\
#                                                 xmax/2,\
#                                                 ymax/2,\
#                                                 float(sys.argv[6])+zmax,\
#                                                 1.00,\
#                                                 1.00,\
#                                                 "qT"))
#
#    		count=count+1
#		resd=resd+1




    File.close()
    
    return
    


#----------------------------------------------------------------------------
#
########################### Main code #######################################

#---Definition of variables---
AtomCoord=[]
vect=[]
i=0 

# ---Definition of code inicialiazation---
try:
   type=sys.argv[1] # Name of the PDB file to read
   type=sys.argv[2] # Name of the atom type to creat the virtual sites 
   type=sys.argv[3] # Name of the output file
   type=sys.argv[4] # Atom-Atom bond distance
   type=sys.argv[5] # Bond of the dummy atoms and Real sites 
   type=sys.argv[6] # O distance to the surface
   type=sys.argv[7] # x dist H1
   type=sys.argv[8] # y dist H1
   type=sys.argv[9] # z dist H1
   type=sys.argv[10] # x dist H2
   type=sys.argv[11] # y dist H2
   type=sys.argv[12] # z dist H2 
except:
    print '----------------------------------------------------------------------'
    print 'The correct use of this script is:    '
    print 'python code.py Name_PDB_input Name_atom_for_V.S. Name_PDB_output Atom-Atom_bond_distance bond_dymmy_at_to_RealSites Odist X_h1 Y_h1 Z_h1 X_h2 Y_h2 Z_h2'
    print '----------------------------------------------------------------------'
    sys.exit(2)


# ----------- Read POSCAR_low
file=open(sys.argv[1],"r")

linhas=file.readlines()

file.close()

CreatPoscar(linhas,sys.argv[2],sys.argv[3],float(sys.argv[4]),float(sys.argv[5]))
#----------------------------------------------------------------------------
