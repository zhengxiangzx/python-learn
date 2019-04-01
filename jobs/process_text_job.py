#!/usr/bin/env python
# encoding: utf-8
"""
 数据处理，可以参考《自然语言处理时，通常的文本清理流程是什么？》
 大致分为以下几个步骤：
    1. Normalization
        标准化：字母小写转换、标点符号处理等，英文里通常只要A-Za-z0-9，根据实际情况确定处理
    2. Tokenization
        Token 是“符号”的高级表达。一般指具有某种意义，无法再分拆的符号。就是将每个句子分拆成一系列词，英文里词之间天然有空格。
    3. Stop words
        Stop Word 是无含义的词，例如'is'/'our'/'the'/'in'/'at'等。它们不会给句子增加太多含义，单停止词是频率非常多的词。 为了减少我们要处理的词汇量，从而降低后续程序的复杂度，需要清除停止词。
    4. Part-of-Speech Tagging   词性标注
    5. Named Entity Recognition 命名实体
    6. Stemming and Lemmatization  将词的不同变化和变形标准化
"""

from pyspark.sql import Row
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

from dependencies.spark import start_spark
from dependencies import process_data


def main():
    """Main ETL script definition.

    :return: None
    """
    # start Spark application and get Spark session, logger and config
    spark, log, config = start_spark(
        app_name='process_text_job',
        files=['configs/process_text_config.json'])

    # log that main ETL job is starting
    log.warn('process_text_job is up-and-running')

    # execute ETL pipeline
    data = extract_data(spark, config['input_path'])
    data_transformed = transform_data(data)
    load_data(data_transformed, config['output_path'])

    # log the success and terminate Spark application
    log.info('process_text_job is finished')
    spark.stop()
    return None


def extract_data(spark, input_path):
    """Load data from csv file format.

    :param spark: Spark session object.
    :param input_path: Input files.
    :return: Spark DataFrame.
    """
    df = (
        spark
            .read
            .csv(input_path, header=True))

    return df


def transform_data(df):
    """Transform original dataset.
        SentenceSplitter  Tokenization
        分句 分词

    :param df: Input DataFrame.
    :return: Transformed DataFrame.
    """

    # 返回类型为字符串类型
    udffenci = udf(fenci, StringType())

    df_transformed = (
        df
            .select('contents')
            .withColumn('contents', udffenci(df.contents)))

    return df_transformed


def load_data(df, outpath):
    """Collect data locally and write to CSV.

    :param df: DataFrame to print.
    :return: None
    """
    (df
     # .coalesce(1)
     .write.csv(outpath, mode='overwrite', header=True))
    return None


# 定义一个 udf 函数
def fenci(conetnt):
    sentences = []
    process_data.wordtokenizer(conetnt, sentences)
    return ' '.join(sentences)


# entry point for PySpark ETL application
if __name__ == '__main__':
    main()
