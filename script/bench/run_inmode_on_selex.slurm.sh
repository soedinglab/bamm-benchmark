#!/bin/zsh

#SBATCH -J InMoDe
#SBATCH -p fat
#SBATCH -t 480:00
#SBATCH -n 4
#SBATCH -N 1
#SBATCH -o ./jobs/inmode_selexl.%J
#SBATCH -C scratch2
#SBATCH -A all

source ./paths.cluster.sh

fn=$(sed "${SLURM_ARRAY_TASK_ID}q;d" ${HTSELEXL_FASTA_DIR}/db.index)
bn=$(echo ${fn} | grep -o -P '(?<=TF-).*(?=__cycle)')

seq=${HTSELEXL_FASTA_DIR}/${fn}

result_dir=${RESULT_DIR}/HTSELEX2018long_c4/inmode/${bn}
mkdir -p ${result_dir}

#echo "Running InMoDe..."
/usr/bin/time -f'urug%e' java -jar ${INMODE} flexible i=${seq} outdir=${result_dir} Name=${bn} m=8 > ${result_dir}/${bn}.out 2>&1
t=$(grep "urug*" ${result_dir}/${bn}.out | sed "s/urug//")
echo "${bn}	$t" > ${result_dir}/${bn}.time

#echo "Transform InMoDe output to BaMM format..."
python3 ${SCRIPT_DIR}/transform_inmode.py ${result_dir}/Learned_${bn}_motif_component_0/Parameters_of_${bn}_motif_component_0.txt -odir ${result_dir}/ -basename ${bn}_motif_1
python3 ${SCRIPT_DIR}/transform_inmode.py ${result_dir}/Learned_${bn}_motif_component_1/Parameters_of_${bn}_motif_component_1.txt -odir ${result_dir}/ -basename ${bn}_motif_2

#echo "Calculate p-values using FDR for all the PWMs..."
${FDR} ${result_dir}/ ${seq} --BaMMFile ${result_dir}/${bn}_motif_1.ihbcp -m 10 -k 2 --cvFold 1 --basename ${bn}_motif_1
${FDR} ${result_dir}/ ${seq} --BaMMFile ${result_dir}/${bn}_motif_2.ihbcp -m 10 -k 2 --cvFold 1 --basename ${bn}_motif_2

# score bindingsites file
${FDR} ${result_dir}/ ${seq} --bindingSiteFile ${result_dir}/Learned_${bn}_motif_component_0/Binding_sites_of_${bn}_motif_component_0.txt -m 10 -k 0 --cvFold 1 --basename ${bn}_motif_3
${FDR} ${result_dir}/ ${seq} --bindingSiteFile ${result_dir}/Learned_${bn}_motif_component_1/Binding_sites_of_${bn}_motif_component_1.txt -m 10 -k 0 --cvFold 1 --basename ${bn}_motif_4

#echo "Calculate AvRec scores for all the PWMs..."
Rscript ${EVALUATION} ${result_dir}/ ${bn}

#rm -f ${result_dir}/*.{stats,txt}

