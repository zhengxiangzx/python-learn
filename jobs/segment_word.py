# -*- coding: utf-8 -*-
import re

import jieba
import os
import logging

from smart_open import smart_open

logger = logging.getLogger(__name__)
jieba.load_userdict('dependencies/user_dict.txt')

# write
pattern = re.compile(u'[^\u4e00-\u9fa5^a-z^A-Z]')


def load_data(uri):
    """
    加载要分词的数据文件 （用的smart_open读文件）
    :param uri: 可以是文件目录地址，可以是url，可以是文件
    :return:
    """
    if os.path.isfile(uri):
        with smart_open(uri, 'rb')as fin:
            for line in fin:
                line = line.strip().decode('utf-8')
                line = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', line, flags=re.MULTILINE)
                line = pattern.sub(r'', line)
                yield line
    elif os.path.isdir(uri):
        files = os.listdir(uri)
        for file in files:
            filename = uri + '/' + file
            with smart_open(filename) as fin:
                for line in fin:
                    line = line.strip().decode('utf-8')
                    line = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', line, flags=re.MULTILINE)
                    line = pattern.sub(r'', line)
                    yield line

    elif os.path.islink(uri):
        pass
    else:
        logger.error('uri 不存在！！')


def participle(sentences, stop_words):
    jieba.cut
    pass
    # if stop_words:
    #     split_words_list = []
    #     if sentence_list:
    #         for sentence in sentence_list:
    #             # sentence = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', sentence, flags=re.MULTILINE)
    #             sentence = pattern.sub(r'', sentence)
    #             split_words = jieba.lcut(sentence.lower())
    #             words = list(filter(lambda x: x.strip(), split_words))
    #             words_list = list(filter(lambda x: x not in stop_words, words))
    #             split_words_list.append(' '.join(words_list))
    #     else:
    #         logger.error('sentence_list is null')
    #     return split_words_list
    # else:
    #     logger.error('Stop words are not loaded')


def load_stop_word(path=None):
    """
    加载停用词
    :param path:停用词的文件地址
    :return:
    """
    stop_words = []
    if path is None:
        path = './dependencies/stop_word.txt'
        with smart_open(path, 'rb', encoding='utf-8') as fin:
            for word in fin:
                stop_words.append(word.strip())
        return stop_words
    else:
        with smart_open(path, 'rb') as fin:
            for word in fin:
                stop_words.append(word.strip().decode('utf-8'))
        return stop_words


def write_data(data, file_path):
    data_size = len(data)

    with open(file_path, 'w', encoding='utf-8') as f:
        for d in data:
            f.write(d + "\n")


def main():
    word = load_stop_word()
    print(word)
    # print(os.path.isfile('./dependencies/stop_word222.txt'))
    # sentence_list = load_data('e:/tmp/output_one/neg')
    # stop_words = load_stop_word('dependencies/stop_word.txt')
    #
    # split_words_list = participle(sentence_list, stop_words)
    # #write_data(split_words_list, 'e:/tmp/output_one/out_put/neg.txt')

    # sentence_list = load_data('E:\\tmp\\taptap_write\\sentence\\taptap.txt')
    # for sentence in sentence_list:
    #     print(sentence)
    # stop_words = load_stop_word('dependencies/stop_word.txt')
    # split_words_list = participle(sentence_list, stop_words)
    # write_data(split_words_list, 'e:/tmp/taptap_write/split_word/taptap.neg')


if __name__ == '__main__':
    main()
