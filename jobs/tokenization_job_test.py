# -*- coding: utf-8 -*-
import os

import jieba

from dependencies._compat import get_module_res, resolve_filename
from dependencies.spark import start_spark


def main():
    """

    :return:
    """
    user_dict = 'user_dict.txt'
    user_dict_path = resolve_filename(get_module_res(user_dict))
    print(get_module_res(user_dict).name)
    jieba.load_userdict(user_dict_path)
    stop_path = resolve_filename(get_module_res('stop_word.txt'))
    spark_session, log, config = start_spark(app_name='nlp_tokenization',
                                             files=['configs/file_list_config.json'])
    stop_words = stop_word(spark_session, stop_path)
    # input_path=config['file_input'], out_put=config['file_output']
    participle(session=spark_session, stop_words=stop_words)


def participle(session=None, stop_words=[]):
    """

    :param session:
    :param input_path:
    :param stop_words:
    :return:
    """
    path = 'E:\\workspaces_learn\\taptap-spider\\'
    files = os.listdir(path)
    for file in files:
        if file.startswith('app_review'):
            if file.endswith('.csv'):
                data_frame = session.read.csv(path=path + file, header=True,
                                              encoding='utf-8')
                for data in data_frame.collect():
                    split_word = jieba.lcut(data.contents)
                    # words = (item for item in split_word if item not in stop_words)
                    words = list(filter(lambda x: x.strip(), split_word))
                    words = list(filter(lambda x: x not in stop_words, words))
                    # df = pandas_udf(words,)
                    # df = pd.DataFrame(words, columns=['data'])
                    # dfs = session.createDataFrame(df)
                    # dfs.write.csv(path='tests/test_data/write_data', header=True, mode='append')


def stop_word(session, stop_words_file):
    if stop_words_file:
        stop_words = []
        data = session.read.text(stop_words_file)
        for word in data.collect():
            stop_words.append(word[0])
        return stop_words


if __name__ == '__main__':
    main()
