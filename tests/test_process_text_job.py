"""
test_process_text_job.py
~~~~~~~~~~~~~~~

This module contains unit tests for the transformation steps of the ETL
job defined in process_text_job.py. It makes use of a local version of PySpark
that is bundled with the PySpark package.
"""
import unittest

import os
import sys
import json

from pyspark import SparkFiles

from dependencies.spark import start_spark
from jobs.process_text_job import transform_data

from dependencies.process_data import split_sentence, wordtokenizer


class SparkETLTests(unittest.TestCase):
    """Test suite for transformation in etl_job.py
    """

    def setUp(self):
        """Start Spark, define config and path to test data
        """
        self.config = json.loads("""{"steps_per_floor": 21}""")
        self.spark, *_ = start_spark()
        self.test_data_path = 'tests/test_data/'

    def tearDown(self):
        """Stop Spark
        """
        self.spark.stop()

    def test_transform_data(self):
        """Test data transformer.

        Using small chunks of input data and expected output data, we
        test the transformation step to make sure it's working as
        expected.
        """

        # assemble
        input_data = (
            self.spark
                .read
                .csv(self.test_data_path + 'taptap_review', header=True))
        print('sys.path 2'.center(50, '-'), sys.path)

        # acttransform_data
        data_transformed = transform_data(input_data)

        print(data_transformed.show(10))

        # assert
        # self.assertEqual(expected_cols, cols)


if __name__ == '__main__':
    unittest.main()
