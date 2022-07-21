import numpy as np
from pyspark.sql.functions import udf, struct, col
from pyspark.sql.types import *
import pyspark.sql.functions as func

input_schema = StructType([
    StructField("0", DoubleType(), False),
    StructField("1", DoubleType(), False),
    StructField("2", DoubleType(), False),
    StructField("3", DoubleType(), False)
])

def input_fn(X):
    X = {
        "0":1.3,
        "1":1.3,
        "2":1.3,
        "3":1.3
    }
    return X