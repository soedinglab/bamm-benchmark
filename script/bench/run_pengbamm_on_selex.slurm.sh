#!/bin/zsh

#SBATCH -J pengbamm_selex
#SBATCH -p fat
#SBATCH -t 120:00
#SBATCH -n 4
#SBATCH -N 1
#SBATCH -o ./jobs/pengbamm_selex.%J
#SBATCH -C scratch2
#SBATCH -A all

source ./paths.cluster.sh

fn=$(sed "${SLURM_ARRAY_TASK_ID}q;d" ${HTSELEXL_FASTA_DIR}/db.index)
bn=$(echo ${fn} | grep -o -P '(?<=TF-).*(?=__cycle)')

seq=${HTSELEXL_FASTA_DIR}/${fn}

result_dir=${RESULT_DIR}/HTSELEX2018long_c4/pengbamm/${bn}
mkdir -p ${result_dir}

peng=${result_dir}/${bn}.meme

#echo "Running PEnG!motif..."
/usr/bin/time -f 'urug%e' ${SHOOT_PENG} ${seq} -o ${peng} --optimization_score MUTUAL_INFO -w 8 --threads 4 --silent > ${result_dir}/${bn}.logg 2>&1

t=$(grep "urug*" ${result_dir}/${bn}.logg | sed "s/urug//")
echo "${bn}     $t" > ${result_dir}/${bn}.time
peng_time=${t}

#echo "Calculate p-values using FDR for the top 1 PWM..."
${FDR} ${result_dir}/ ${seq} --PWMFile ${peng} -m 10 -k 0 --cvFold 1 --maxPWM 5 --basename ${bn}

#echo "Calculate AvRec scores for all the PWMs..."
${EVALUATION} ${result_dir}/ ${bn}

#rm -f ${result_dir}/*stats

for k in {0,1,2,5}
do
        result_dir=${RESULT_DIR}/HTSELEX2018long_c4/bamm_k${k}_mask/${bn}
        mkdir -p ${result_dir}
	/usr/bin/time -f 'urug%e' ${BAMMMOTIF} ${result_dir} ${seq} --PWMFile ${peng} --maxPWM 1 --EM -k ${k} --extend 2 2 --basename ${bn} --advanceEM > ${result_dir}/${bn}.logg 2>&1
	t=$(grep "urug*" ${result_dir}/${bn}.logg | sed "s/urug//")
	total_time=$(awk "BEGIN {print $peng_time+$t; exit}")
	echo "${bn}     ${total_time}" > ${result_dir}/${bn}.time
	echo "${bn}     ${t}" > ${result_dir}/${bn}.time

	${FDR} ${result_dir} ${seq} --BaMMFile ${result_dir}/${bn}*.ihbcp --bgModelFile ${result_dir}/${bn}*.hbcp -k ${k} -m 10 --cvFold 1 --basename ${bn}

	#echo "Calculate AvRec scores for all the PWMs..."	
	${EVALUATION} ${result_dir} ${bn}
	
	#rm -fr ${result_dir}/*.stats
done

for k in {0,1,2,5}
do
        result_dir=${RESULT_DIR}/HTSELEX2018long_c4/bamm_k${k}_full/${bn}
        mkdir -p ${result_dir}
	/usr/bin/time -f 'urug%e' ${BAMMMOTIF} ${result_dir} ${seq} --PWMFile ${peng} --maxPWM 1 --EM -k ${k} --extend 2 2 --basename ${bn} > ${result_dir}/${bn}.logg 2>&1
	t=$(grep "urug*" ${result_dir}/${bn}.logg | sed "s/urug//")
	total_time=$(awk "BEGIN {print $peng_time+$t; exit}")
	echo "${bn}     ${total_time}" > ${result_dir}/${bn}.time
	echo "${bn}     ${t}" > ${result_dir}/${bn}.time

	${FDR} ${result_dir} ${seq} --BaMMFile ${result_dir}/${bn}*.ihbcp --bgModelFile ${result_dir}/${bn}*.hbcp -k ${k} -m 10 --cvFold 1 --basename ${bn}

	#echo "Calculate AvRec scores for all the PWMs..."	
	${EVALUATION} ${result_dir} ${bn}
	
	#rm -fr ${result_dir}/*.stats
done
