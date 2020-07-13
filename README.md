# About BaMM benchmark repository

This repository stores the scripts and data for generating the results in the W Ge, et al. paper (DOI: https://doi.org/10.1101/2020.07.12.197053).

# Installing

## 1. Clone this repository

    git clone https://github.com/soedinglab/BaMM_benchmark
    cd BaMM_benchmark

## 2. (optional) Download the pre-processed data from our cluster

  Bash scripts:

    mkdir -p data/raw
    curl -o data/raw/ENCODE.zip  http://wwwuser.gwdg.de/~compbiol/bamm/benchmark/ENCODE.zip
    curl -o data/raw/HTSELEX.zip  http://wwwuser.gwdg.de/~compbiol/bamm/benchmark/HTSELEX.zip
    # unzip files
    unzip data/raw/ENCODE.zip -d data/raw/ENCODE/
    unzip data/raw/HTSELEX.zip -d data/raw/HTSELEX/

    # download data for CTCF analysis (data size: 320G)
    curl -o data/processed/CTCF.zip  http://wwwuser.gwdg.de/~compbiol/bamm/benchmark/CTCF/
    unzip data/processed/CTCF.zip -d data/processed/CTCF/

## 3. Prerequisites for installing BaMMmotif2

  To compile from source code, you need:
  * [GCC](https://gcc.gnu.org/) compiler 4.7 or later (we suggest GCC-5.x)
  * [CMake](http://cmake.org/) 2.8.11 or later

  C++ packages
  * [Boost](http://www.boost.org/)

  R and several R packages
  * [R](https://cran.r-project.org/) 2.14.1 or later

  Download R packages by running:

    Rscript ./script/install_packages.R


## 4. Install tools

#### I. Install the fast seeding program PEnGmotif

  [PEnG-motif](https://github.com/soedinglab/PEnG-motif)

#### II. Install the refinement program BaMMmotif2

  [BaMMmotif2](https://github.com/soedinglab/BaMMmotif2)

#### III. Other tools that are included in this benchmark:
  * [MEME](http://meme-suite.org/doc/download.html), version 5.1.1
  * [CisFinder](https://lgsun.grc.nia.nih.gov/CisFinder/download.html)
  * [ChIPMunk](http://autosome.ru/ChIPMunk/), version 8
  * [di-ChIPMunk](http://autosome.ru/ChIPMunk/), version 8
  * [InMoDe](http://www.jstacs.de/index.php/InMoDe)


## 5. Edit paths

   Edit paths in this path file `./script/bench/paths.cluster.sh`

## 6. Submit jobs to the cluster
    
    ./script/bench/start_benchmark.slurm.sh

## 7. Summarize the motif evaluations to get runtime and AvRec score

    ./script/bench/summary_benchmark.sh






    

