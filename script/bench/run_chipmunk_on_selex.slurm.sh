#!/bin/zsh

#SBATCH -J chipmunk
#SBATCH -p fat
#SBATCH -t 480:00
#SBATCH -n 4
#SBATCH -N 1
#SBATCH -o ./jobs/chipmunk_selexl.%J
#SBATCH -C scratch2

source ./paths.cluster.sh

fn=$(sed "${SLURM_ARRAY_TASK_ID}q;d" ${HTSELEXL_FASTA_DIR}/db.index)
bn=$(echo ${fn} | grep -o -P '(?<=TF-).*(?=__cycle)')

seq=${HTSELEXL_FASTA_DIR}/${fn}

result_dir=${RESULT_DIR}/HTSELEX2018long_c4/chipmunk/${bn}
mkdir -p ${result_dir}

#echo "Running ChIPMunk..."
/usr/bin/time -f'urug%e' java -cp ${CHIPMUNK} ru.autosome.ChIPMunk 8 12 yes 1.0 s:${seq} 100 10 1 4 > ${result_dir}/${bn}.out 2>&1
t=$(grep "urug*" ${result_dir}/${bn}.out | sed "s/urug//")
echo "${bn}	$t" > ${result_dir}/${bn}.time

#echo "Transform ChIPMunk output to MEME format..."
python3 ${SCRIPT_DIR}/transform_chipmunk.py ${result_dir}/${bn}.out ${result_dir}/${bn}.meme

#echo "Calculate p-values using FDR for all the PWMs..."
${FDR} ${result_dir}/ ${seq} --PWMFile ${result_dir}/${bn}.meme --maxPWM 3 -m 10 -k 0 --cvFold 1 --basename ${bn}

#echo "Calculate AvRec scores for all the PWMs..."
Rscript ${EVALUATION} ${result_dir}/ ${bn}

$rm -f ${result_dir}/*.stats

