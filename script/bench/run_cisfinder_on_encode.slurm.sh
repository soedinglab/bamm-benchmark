#!/bin/zsh

#SBATCH -J cisfinder
#SBATCH -p fat
#SBATCH -t 120:00
#SBATCH -n 4
#SBATCH -N 1
#SBATCH -o ./jobs/cisfinder.%J
#SBATCH -C scratch2

source ./paths.cluster.sh

fn=$(sed "${SLURM_ARRAY_TASK_ID}q;d" ${FASTA_DIR}/db.index)
bn=$(basename ${fn} _summits104_restr5000.fasta)
result_dir=${RESULT_DIR}/cisfinder/${bn}

mkdir -p ${result_dir}

#echo "Running Cisfinder_PatternFind..."
t=$(/usr/bin/time -f'urug%e' ${CISFINDER_PATTERNFIND} -i ${FASTA_DIR}/${fn} -o ${result_dir}/${bn}.find 2>&1 | grep -o "urug.*" | sed "s/urug//")
echo $t >> ${result_dir}/${bn}.single_time

#echo "Running Cisfinder_PatternCluster..."
t=$(/usr/bin/time -f'urug%e' ${CISFINDER_PATTERNCLUSTER} -i ${result_dir}/${bn}.find -o ${result_dir}/${bn}.cluster 2>&1 | grep -o "urug.*" | sed "s/urug//")
echo $t >> ${result_dir}/${bn}.single_time

#echo "Running Cisfinder_PatternTest..."
t=$(/usr/bin/time -f'urug%e' ${CISFINDER_PATTERNTEST} -i ${result_dir}/${bn}.cluster -f ${FASTA_DIR}/${fn} -o ${result_dir}/${bn}.test 2>&1 | grep -o "urug.*" | sed "s/urug//")
echo $t >> ${result_dir}/${bn}.single_time

t=$(awk '{ sum += $1 } END { print sum }' ${result_dir}/${bn}.single_time)
echo "${bn}	$t" > ${result_dir}/${bn}.time

#echo "Transform CisFinder output to MEME format..."
python3 ${SCRIPT_DIR}/transform_cisfinder.py ${result_dir}/${bn}.test ${result_dir}/${bn}.meme

#echo "Calculate p-values using FDR for all the PWMs..."
${FDR} ${result_dir}/ ${FASTA_DIR}/${fn} --PWMFile ${result_dir}/${bn}.meme -m 10 -k 0 --cvFold 1

#echo "Calculate AvRec scores for all the PWMs..."
Rscript ${EVALUATION} ${result_dir}/ ${bn}

rm -f ${result_dir}/*{cluster,find,test,stats,single_time}
