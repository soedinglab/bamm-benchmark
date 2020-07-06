#!/bin/zsh

#SBATCH -J chipmunk
#SBATCH -p fat
#SBATCH -t 480:00
#SBATCH -n 4
#SBATCH -N 1
#SBATCH -o ./jobs/chipmunk.%J
#SBATCH -C scratch2

source ./paths.cluster.sh

fn=$(sed "${SLURM_ARRAY_TASK_ID}q;d" ${ENCODE_FASTA_DIR}/db.index)
bn=$(basename ${fn} _summits104_restr5000.fasta)
result_dir=${RESULT_DIR}/ENCODE/chipmunk/${bn}

mkdir -p ${result_dir}
 
echo ${bn}

#echo "Running ChIPMunk..."
/usr/bin/time -f'urug%e' java -cp ${CHIPMUNK} ru.autosome.ChIPMunk 8 12 yes 1.0 s:${ENCODE_FASTA_DIR}/${fn} 100 10 1 4 > ${result_dir}/${bn}.out 2>&1
t=$(grep "urug*" ${result_dir}/${bn}.out | sed "s/urug//")
echo "${bn}	$t" > ${result_dir}/${bn}.time

#echo "Transform ChIPMunk output to MEME format..."
python3 ${SCRIPT_DIR}/transform_chipmunk.py ${result_dir}/${bn}.out ${result_dir}/${bn}.meme

#echo "Calculate p-values using FDR for all the PWMs..."
${FDR} ${result_dir}/ ${ENCODE_FASTA_DIR}/${fn} --PWMFile ${result_dir}/${bn}.meme -m 10 -k 0 --cvFold 1

#echo "Calculate AvRec scores for all the PWMs..."
Rscript ${EVALUATION} ${result_dir}/ ${bn}

#rm -f ${result_dir}/*{stats,out}
