# FL_Benchmark
This repository is a code basis to create and compare different FL approaches.

## Before Installation
Some datasets are downloaded from kaggle, so you need to create a kaggle account and key. After that create a file named `.env` in the root directory with the following content:
```bash
KAGGLE_USERNAME="<username>"
KAGGLE_KEY="<key>"
```

## Container
To run the code in a docker container, you can use the following commands:
```bash
# create the docker image (it may take a while)
docker build -t fl_benchmark .
# create the docker container
docker run -d --name fl_benchmark fl_benchmark
# start the container if it is not running
docker start fl_benchmark
# go to the container
docker exec -it fl_benchmark bash
```

## Usage
To run the code, you can use the following commands:
```bash
# download the datasets
python3 Programs/preprocess.py -d IOT_DNL
# divide the datasets
python3 Programs/division.py -d IOT_DNL -n 2
# or from a file
mpirun -n 3 python3 Programs/fl.py --file example.json 2>/dev/null
# to see the help
python3 Programs/fl.py -h
```
