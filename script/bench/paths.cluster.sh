#!/bin/zsh

# DIRECTORIES
export HM_DIR= # your home folder for the results

export DB_DIR=${HM_DIR}/data/
export ENCODE_FASTA_DIR=${DB_DIR}/ENCODE2018/seq_summits104_restr5000/
export HTSELEXL_FASTA_DIR=${DB_DIR}/HTSELEX2018long/sequence_top5k/

export BM_DIR=../
export OUTPUT_DIR=${BM_DIR}/output/
export RESULT_DIR=${BM_DIR}/result/
export SCRIPT_DIR=${BM_DIR}/script/
export TOOL_DIR=${BM_DIR}/tools/

# PATH to executable binaries or scripts
export FDR=~/opt/BaMM/bin/FDR
export BAMMMOTIF=~/opt/BaMM/bin/BaMMmotif
export BAMMSIMU=~/opt/BaMM/bin/BaMMSimu
export PENGMOTIF=~/opt/PEnG/bin/peng_motif

export BAMMMOTIFV1=${TOOL_DIR}/BaMMmotif1/build/BaMMmotif
export CISFINDER_PATTERNFIND=${TOOL_DIR}/CisFinder/bin/patternFind
export CISFINDER_PATTERNCLUSTER=${TOOL_DIR}/CisFinder/bin/patternCluster
export CISFINDER_PATTERNTEST=${TOOL_DIR}/CisFinder/bin/patternTest
export CHIPMUNK=${TOOL_DIR}/ChIPMunk/chipmunk.jar
export MEME=${TOOL_DIR}/meme-5.1.0/build/bin/meme
export INMODE=${TOOL_DIR}/InMoDeCLI-1.1.jar

# PATH to R and Python scripts
export SHOOT_PENG=~/opt/PEnG/bin/shoot_peng.py
export EVALUATION=~/opt/BaMM/bin/plotPvalStats.R

# make new directory for outputs
mkdir -p ${OUTPUT_DIR}
mkdir -p ${RESULT_DIR}
mkdir -p ${HTSELEXL_DIR}
mkdir -p ${GTRD_DIR}

