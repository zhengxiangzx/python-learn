# -*- coding: utf-8 -*-
import json
import re
from pyltp import SentenceSplitter
import jieba
from pyspark.sql.functions import udf, explode
from pyspark.sql.types import ArrayType, StringType
from smart_open import smart_open
import unittest
from dependencies._compat import get_module_res
from dependencies.spark import start_spark
from jobs.clause_contents import transform_data, load_data


class TestPySparkSegment(unittest.TestCase):
    def setUp(self):
        """
        Start Spark, define config and path to test data
        """
        self.config = json.loads("""{"steps_per_floor": 21}""")
        self.spark, *_ = start_spark(app_name='nlp_clause_test')
        self.test_data_path = 'tests/test_data/segment_test'

    def tearDown(self):
        """
        Stop Spark
        """
        self.spark.stop()

    def test_load_data(self):
        path = self.test_data_path
        df = load_data(self.spark, path)
        print("load_data == ", df.collect())
        return df

    def test_clause(self, sentences):
        # 把传入的数据字母变小写
        sentences = str(sentences).lower().encode('utf-8')
        # 进行分句 哈工大的分句
        sentence = SentenceSplitter.split(sentences)
        # strip()操作
        sentence_list = list(filter(lambda x: x.strip(), sentence))
        print('sentence_list == ', sentence_list)
        return sentence_list

    def test_participle(self, sentence):
        # 加载停用词
        stop_words = self.test_load_stop_word()
        # 去掉url地址
        sentence = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', sentence, flags=re.MULTILINE)
        # 去掉非汉字字母的其他部分（只保留汉字字母）
        sentence = self.pattern.sub(r'', sentence)
        # 调用JieBa进行分词
        split_words = jieba.lcut(sentence.lower())
        # 去空格等符号
        words = list(filter(lambda x: x.strip(), split_words))
        # 去停用词
        words_list = list(filter(lambda x: x not in stop_words, words))
        # 返回分词结果
        print(' '.join(words_list))
        return ' '.join(words_list)

    # def test_load_stop_word(self, path=None):
    #     stop_words = []
    #     if path is None:
    #         path = get_module_res('stop_word.txt')
    #         with smart_open(path, 'rb', encoding='utf-8') as fin:
    #             for word in fin:
    #                 stop_words.append(word.strip())
    #         return stop_words
    #     else:
    #         with smart_open(path, 'rb') as fin:
    #             for word in fin:
    #                 stop_words.append(word.strip().decode('utf-8'))
    #         return stop_words

    def test_transform_data(self):
        data = self.test_load_data()
        df = transform_data(data)
        print(df.collect())

# if __name__ == '__main__':
#     unittest.main()
