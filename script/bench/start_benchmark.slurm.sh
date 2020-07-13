#!/usr/bin/env bash
module load gcc/6.3.0
module load python/3.6.3
module load JAVA/jdk1.8.0_31
source ./paths.cluster.sh

## FOR ENCODE datasets
sbatch --array=1-435 run_pengbamm_on_encode.slurm.sh
sbatch --array=1-435 run_BaMMmotifv1_on_encode.slurm.sh
sbatch --array=1-435 run_cisfinder_on_encode.slurm.sh
sbatch --array=1-435 run_chipmunk_on_encode.slurm.sh
sbatch --array=1-435 run_di-chipmunk_on_encode.slurm.sh
sbatch --array=1-435 run_meme_on_encode.slurm.sh
sbatch --array=1-435 run_inmode_on_encode.slurm.sh

## FOR HT-SELEX datasets
sbatch --array=1-170 run_pengbamm_on_selex.slurm.sh
sbatch --array=1-170 run_cisfinder_on_selex.slurm.sh
sbatch --array=1-170 run_chipmunk_on_selex.slurm.sh
sbatch --array=1-170 run_di-chipmunk_on_selex.slurm.sh
sbatch --array=1-170 run_meme_on_selex.slurm.sh
sbatch --array=1-170 run_inmode_on_selex.slurm.sh

