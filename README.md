# FL_Benchmark
This repository is a code basis to create and compare different FL approaches.

## Before Installation
Some datasets are downloaded from kaggle, so you need to create a kaggle account and key. After that create a file named `.env` in the root directory with the following content:
```bash
KAGGLE_USERNAME="<username>"
KAGGLE_KEY="<key>"
```

# TODO: docker

## Usage
To run the code, you can use the following commands:
```bash
# download the datasets
python3 Programs/preprocess.py -d all
# divide the datasets
python3 Programs/division.py -d all -n 4
# or from a file
mpirun -n 5 python3 Programs/fl.py --file example.json
# to see the help
python3 Programs/fl.py -h
```
