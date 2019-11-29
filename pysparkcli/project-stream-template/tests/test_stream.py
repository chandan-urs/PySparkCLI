import unittest
from pyspark.sql import SparkSession
import transform
import json


class SparkStreamTest(unittest.TestCase):

    def setUp(self):
        spark = SparkSession.builder.getOrCreate()
        self.dataRDD = spark.read.json('./test-data/inputs/data.json').rdd

    def test_transform_data(self):
        result = transform.transformfunc(self.dataRDD)
        print(result)


if __name__ == '__main__':
    unittest.main()
