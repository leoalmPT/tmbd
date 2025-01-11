import sys
sys.path.append(".")

from dotenv import load_dotenv
load_dotenv()

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# utils
from Utils.DatasetUtils import DatasetUtils
from Utils.MLUtils import MLUtils
from Utils.FLUtils import FLUtils
from Utils.ModelUtils import ModelUtils

# datasets
from Datasets.IOT_DNL import IOT_DNL

# models
from Models.IOT_DNL_M1 import IOT_DNL_M1

# ML
from ML.Tensorflow import Tensorflow as MLtf

# Comm
from Comm.MPI import MPI as CommMPI

# FL
from FL.DecentralizedSync import DecentralizedSync

# update tf logging level
import tensorflow as tf
tf.get_logger().setLevel('WARN')

print("Config loaded\n")


UTILS = {
    'dataset': DatasetUtils,
    'model': ModelUtils,
    'ml': MLUtils,
    'fl': FLUtils,
}

DATASETS = {
    'IOT_DNL': IOT_DNL,
}

MODELS = {
    'IOT_DNL': IOT_DNL_M1,
}

ML = {
    'tf': MLtf
}

COMM = {
    'mpi': CommMPI
}

FL = {
    'ds': DecentralizedSync
}
