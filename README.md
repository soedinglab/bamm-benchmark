# About BaMM benchmark repository

This repository stores the scripts and data for generating the resluts in the W Ge, et al. paper.

### (C) Wanwan Ge, 2020-07

# Installing

## 1. Clone this repository

    git clone https://github.com/soedinglab/BaMM_benchmark
    cd BaMM_benchmark

## 2. (optional) Download the raw data from our cluster

    mkdir -p data/raw
    curl -o data/raw/ENCODE.zip  http://wwwuser.gwdg.de/~compbiol/www/bamm/benchmark/ENCODE.zip
    curl -o data/raw/HTSELEX.zip  http://wwwuser.gwdg.de/~compbiol/www/bamm/benchmark/HTSELEX.zip
    # unzip files
    unzip data/raw/ENCODE.zip -d data/raw/ENCODE/
    unzip data/raw/HTSELEX.zip -d data/raw/HTSELEX/

    # download data for CTCF analysis (data size: 320G)
    curl -o data/processed/CTCF.zip  http://wwwuser.gwdg.de/~compbiol/www/bamm/benchmark/CTCF
    unzip data/processed/CTCF.zip -d data/processed/CTCF/

## 3. Install tools

    # Download the fast seeding tool PEnGmotif, which is used for de novo motif discovery with PWMs






    

