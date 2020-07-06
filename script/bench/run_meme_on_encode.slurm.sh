#!/bin/zsh

#SBATCH -J meme_encode
#SBATCH -p fat
#SBATCH -t 240:00
#SBATCH -n 4
#SBATCH -N 1
#SBATCH -o ./jobs/meme_encode.%J
#SBATCH -C scratch2
#SBATCH -A all

source ./paths.cluster.sh
##SLURM_ARRAY_TASK_ID=1

fn=$(sed "${SLURM_ARRAY_TASK_ID}q;d" ${ENCODE_FASTA_DIR}/db.index)
bn=$(basename ${fn} _summits104_restr5000.fasta)
result_dir=${RESULT_DIR}/ENCODE/meme/${bn}
mkdir -p ${result_dir}
echo ${bn}

seq=${ENCODE_FASTA_DIR}/${fn}

#echo "Running MEME..."
t=$(/usr/bin/time -f 'urug%e' ${MEME} ${seq} -dna -mod zoops -oc ${result_dir} -nmotifs 3 -revcomp -p 4 -V 2>&1 | grep -o "urug.*" | sed "s/urug//")
echo "${bn}	$t" > ${result_dir}/${bn}.time

# transform new MEME text format to MEMEv4
python3 ${SCRIPT_DIR}/transform_meme.py ${result_dir}/meme.txt --prefix ${bn}

#echo "Calculate p-values using FDR for all the PWMs..."
${FDR} ${result_dir}/ ${seq} --PWMFile ${result_dir}/${bn}.meme -m 10 -k 0 --cvFold 1

#echo "Calculate AvRec scores for all the PWMs..."
Rscript ${EVALUATION} ${result_dir}/ ${bn}

#rm -f ${result_dir}/*{html,txt,xml,stats}
