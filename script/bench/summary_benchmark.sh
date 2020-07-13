#!/usr/bin/env bash

for dataset in ENCODE HTSELEX2018long_c4 # change the foldname accordingly
do

	for tool in pengbamm cisfinder meme inmode chipmunk di-chipmunk
	do 
		awk 'FNR==1' ../result/${dataset}/${tool}/*/*.time > ../output/${dataset}/${tool}.time.bench
		for file in ../result/${dataset}/${tool}/*/*.bmscore
		do 
			sort -nrk3,3 ${file} | head -1 | cut -d ' ' -f3
		done > ../output/${dataset}/${tool}.bmscore.bench # get the best score out of all discovered motifs
	done

done 
