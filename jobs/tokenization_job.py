# -*- coding: utf-8 -*-
import os
import re

import jieba
import pandas as pd
from dependencies.spark import start_spark


def main():
    """

    :return:
    """
    pattern = u'[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+'
    stop_words_file = './dependencies/stop_word.txt'
    user_dict = './dependencies/user_dict.txt'
    stop_words = stop_word(stop_words_file)
    file_path = 'E:\\workspaces_learn\\taptap-spider'
    spark_session, log, config = start_spark(app_name='nlp_tokenization',
                                             files=['./configs/file_list_config.json'])
    file_list = os.listdir(file_path)
    for file in file_list:
        if file.startswith('app_review'):
            if file.endswith('.csv'):
                file_split = file.split('.')[0]
                file = file_path + '/' + file
                sentences_list = load_data(spark_session, file)
                word_split(sentences_list=sentences_list, stop_words=stop_words, user_dict=user_dict, pattern=pattern,
                           session=spark_session, file=file_split)


def load_data(session, input_path):
    """
    用spark加载hdfs上的数据
    :param session: 创建的pyspark的SparkSession实例
    :param input_path: 要读取的文件的hdfs地址目录
    :return: 返回每个文件读取的每条评论内容数据的一个list
    """
    if input_path:
        print("input===", input_path)
        dataframe = session.read.csv(path=input_path, header=True, encoding='utf-8')
        sentences_list = []
        if dataframe:
            for sentence in dataframe.collect():
                sentences_list.append(sentence.contents)
        return sentences_list


def word_split(sentences_list=[], stop_words=[], user_dict=None,
               pattern=None, session=None, file=None):
    """

    :param sentences_list:
    :param stop_words:
    :param user_dict:
    :param pattern:
    :param session:
    :param file:
    :return:
    """
    if user_dict is None:
        user_dict = './dependencies/user_dict.txt'
    jieba.load_userdict(user_dict)
    for sentences in sentences_list:
        participle = jieba.lcut(sentences)
        word_list = remove_stop_word(participle, stop_words, pattern)
        write_csv(word_list, session, file)


def add_words(words):
    if words:
        for word in words:
            jieba.add_word(word)
    else:
        jieba.add_word('')


def stop_word(stop_words_file):
    if stop_words_file:
        stop_words = []
        with open(stop_words_file, 'rt', encoding='utf-8') as f:
            for word in f:
                stop_words.append(word.strip('\n'))
        return stop_words


def remove_stop_word(participle, stop_words, pattern):
    if participle:
        word_list = []
        for word in participle:
            if word:
                if word not in stop_words:
                    word_re = re.sub(pattern, '', word)
                    # word_re = pattern.sub(r'', word)
                    if word_re != '':
                        word_list.append(word)
        return word_list


def write_csv(word_list, session, file):
    if word_list:
        df = pd.DataFrame(word_list, columns=['data'])
        dfs = session.createDataFrame(df)
        dfs.coalesce(1).write.csv(path='data/test_write/' + file, header=True, mode='append')
        # dfs.write.text(path='data/test_write')


if __name__ == '__main__':
    main()
