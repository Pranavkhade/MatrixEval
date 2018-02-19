#!/bin/bash
#
#SBATCH  --workdir=/work/LAS/jernigan-lab/sshome/sshome/HpnN/HpnN/production_md/Diploptene/l48f

#SBATCH --nodes=8
#SBATCH --job-name="ihopeitworks"

#SBATCH --time=168:00:00  
#SBATCH --ntasks-per-node=16
#SBATCH --export=ALL
#
#SBATCH -e namd_%N.err.%j 
#SBATCH -o namd_%N.out.%j


# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE
module purge
module load openmpi/2.1.0
module load namd/2.12-ibverbs

cd $SLURM_SUBMIT_DIR
echo "slurm submit dir: $SLURM_SUBMIT_DIR"

# here is bins for namd

                                                                                   
                                                                                                                                       

myNAMD2=$(which namd2)
myWork=/work/LAS/jernigan-lab/sshome/sshome/HpnN/HpnN/production_md/Diploptene/l48f


## allocate 32 processors=2*16, 16 /node.
charmrun +p 128 ++ppn 16   ${myNAMD2}  +setcpuaffinity ${myWork}/min.namd  > min.log

