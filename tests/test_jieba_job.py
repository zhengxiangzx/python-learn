import unittest

import os
from pyspark import SparkFiles
import pandas as pd
from dependencies.spark import start_spark
from jobs.tokenization_job import load_data, stop_word, remove_stop_word
import jieba


class TestJiebaJob(unittest.TestCase):
    def setUp(self):
        self.config = 'configs/file_list_config.json'
        self.session, *_ = start_spark(app_name='jieba_test')
        self.test_data_path = 'tests/test_data/'

    def tearDown(self):
        """Stop Spark
        """
        self.session.stop()

    # def test_load_data(self):
    #     path = 'E:\\workspaces_learn\\taptap-spider\\app_review_列王纷争.csv'
    #     sentences_list = load_data(self.session, path)
    #     sentences_count = len(sentences_list)
    #     dataframe = self.session.read.csv(path=path, header=True, encoding='utf-8')
    #     contents_count = dataframe.select('contents').count()
    #     self.assertEqual(sentences_count, contents_count)
    #
    # def test_stop_word(self):
    #     print(os.getcwd())
    #     path = './dependencies/stop_word.txt'
    #     with open(path, 'rt', encoding='utf-8')as f:
    #         stop_word_count = len(f.readlines())
    #     count = len(stop_word(path))
    #     self.assertEqual(stop_word_count, count)
    #
    # def test_remove_stop_word(self):
    #     path = './dependencies/stop_word.txt'
    #     pattern = u'[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+'
    #     stop_words = stop_word(path)
    #     words = []
    #     with open(path, 'rt', encoding='utf-8')as f:
    #         for line in f:
    #             words.append(line.strip('\n'))
    #     list_word = remove_stop_word(line.strip('\n'), stop_words, pattern)
    #     self.assertEqual(len(list_word), 0)

    def test_wirte(self):
        dataframe = self.session.read.csv('E:\\workspaces_learn\\taptap-spider\\app_review_列王纷争.csv', header=True,
                                          encoding='utf-8')
        if dataframe:
            for sentence in dataframe.collect():
                print(jieba.lcut(sentence.contents))
        # df = pd.DataFrame(sentences_list, columns=['data'])
        # dfs = self.session.createDataFrame(df)
        # dfs.coalesce(1).write.csv(path='tests/test_data/write_csv', header=True, sep=",", mode='overwrite')

    # # input_files = self.config['file_input']
    # # print(input_files)


if __name__ == '__main__':
    unittest.main()
