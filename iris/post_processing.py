import numpy as np
from pyspark.sql.functions import udf, struct, col
from pyspark.sql.types import *
import pyspark.sql.functions as func

output_schema = StructType([
    StructField("result", IntegerType(), False),
])

def output_fn(X):
    X = {
        "result": 2
    }
    return X