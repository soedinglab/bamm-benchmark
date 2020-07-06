#!/bin/zsh

#SBATCH -J bammv1
#SBATCH -p fat
#SBATCH -t 240:00
#SBATCH -n 4
#SBATCH -N 1
#SBATCH -o ./jobs/bammv1.%J
#SBATCH -C scratch2
#SBATCH -A all

source ./paths.cluster.sh

fn=$(sed "${SLURM_ARRAY_TASK_ID}q;d" ${ENCODE_FASTA_DIR}/db.index)
seq=${ENCODE_FASTA_DIR}/${fn}
bn=$(basename ${fn} _summits104_restr5000.fasta)

for k in {0,1,2,5}
do 

	result_dir=${RESULT_DIR}/ENCODE/bammmotifv1_k${k}/${bn}
	mkdir -p ${result_dir}

	#echo "Running BaMMmotif with EM..."
	/usr/bin/time -f 'urug%e' ${BAMMMOTIFV1} ${result_dir} ${seq} --reverseComp --XX-localization --XX-localizationRanking --XX-K 2 --maxPValue 0.05 --maxPWMs 3 --extend 2 2  --saveBaMMs > ${result_dir}/${bn}.logg 2>&1

        t=$(grep "urug*" ${result_dir}/${bn}.logg | sed "s/urug//")
        echo "${bn}	$t" > ${result_dir}/${bn}.time

	# change the suffix of file
	cp ${result_dir}/${bn}_summits104_restr5000.conds ${result_dir}/${bn}.ihbcp
	cp ${result_dir}/${bn}_summits104_restr5000-1.conds ${result_dir}/${bn}-1.ihbcp
	cp ${result_dir}/${bn}_summits104_restr5000-2.conds ${result_dir}/${bn}-2.ihbcp

	# add meta data to the previous hbcp file
	rm -f ${result_dir}/${bn}.hbcp
	echo "# K = 2" >> ${result_dir}/${bn}.hbcp
	echo "# A = 1 10 10" >> ${result_dir}/${bn}.hbcp
	less ${result_dir}/${bn}_summits104_restr5000.condsBg >> ${result_dir}/${bn}.hbcp
	
	# evaluate 
	${FDR} ${result_dir} ${seq} --BaMMFile ${result_dir}/${bn}.ihbcp --bgModelFile ${result_dir}/${bn}.hbcp -k ${k} -m 10 --cvFold 1
        ${FDR} ${result_dir} ${seq} --BaMMFile ${result_dir}/${bn}-1.ihbcp --bgModelFile ${result_dir}/${bn}.hbcp -k ${k} -m 10 --cvFold 1
	${FDR} ${result_dir} ${seq} --BaMMFile ${result_dir}/${bn}-2.ihbcp --bgModelFile ${result_dir}/${bn}.hbcp -k ${k} -m 10 --cvFold 1

        ${EVALUATION} ${result_dir} ${bn}
        #rm -fr ${result_dir}/*.stats
	# shorten filenames to keep consistence	
	mv ${result_dir}/${bn}_summits104_restr5000.bmscore ${result_dir}/${bn}.bmscore
done
