# -*- coding: utf-8 -*-
from pyspark import SparkFiles
from pyspark.sql import SparkSession
import os
from os import environ, listdir, path, getcwd
import jieba


# def create_spark_session(app_name="SparkApplication", master='local[*]', files=[], spark_config={}, jar_packages=[]):
#     spark_session = SparkSession.builder \
#         .appName(app_name) \
#         .master(master)
#
#     spark_session.config('file_path', files)
#     # spark_session.config('jar_packages', jar_packages)
#     # for key, value in spark_config.items():
#     #     spark_session.config(key=key, value=value)
#     spark_session = spark_session.getOrCreate()
#     spark_session.sparkContext.setLogLevel("WARN")
#     return spark_session


def main():
    route = {}
    N = 10
    route[N] = (0, 0)
    print(route)
    # file_path = 'E:\\workspaces_learn\\taptap-spider'
    # file_list = []
    # for file in os.listdir(file_path):
    #     if file.startswith('app_review'):
    #         if file.endswith('.csv'):
    #             file_list.append(file)
    #
    # session = create_spark_session(app_name='jieba', files=['configs/file_list_config.json'])
    # monthlySales = session.read.csv('E:\\workspaces_learn\\taptap-spider\\app_review_*.csv', header=True,
    #                                 encoding='utf-8')
    # monthlySales.select('contents').show()
    # spark_files_dir = SparkFiles.getRootDirectory()
    # print("spark_files_dir=", spark_files_dir)
    # config_files = [filename
    #                 for filename in listdir(spark_files_dir)
    #                 if filename.endswith('config.json')]
    # print('config_files=', config_files)
    # list_list = []
    # data = monthlySales.collect()
    # for i in data:
    #     list_list.append(jieba.lcut(i.contents))
    # print(list_list)


if __name__ == '__main__':
    main()
