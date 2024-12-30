# amber22_param

After cloning this repo, 
do a Git-lfs fetch and pulling; since large files are compressed and needed to be pulled(Github way of dealing large files)
In paramrudra terminal, 
```
spack load miniconda3@24.3.0
conda create -n git 
conda activate git
conda install git-lfs
```
This will install git-lfs. 
Now git clone this repo, 
```
git clone https://github.com/dmighty007/amber22_param.git
cd amber22_param
git-lfs install
git-lfs fetch --all
git-lfs pull
```
This should pull the whole directory with large file.
```
# Now cd into the bin folder
cd amber22_param/amber22/bin
ln -s pmemd.cuda_SPFP pmemd.cuda
ln -s pmemd.cuda_SPFP.MPI pmemd.cuda.MPI
```
That should be enough to install amber22 in the user directory.
