# -*- coding: utf-8 -*-
import math
import re

import jieba
import os
import logging

logger = logging.getLogger(__name__)
jieba.load_userdict('dependencies/user_dict.txt')

# write
pattern = re.compile(u'[^\u4e00-\u9fa5^a-z^A-Z]')
# 后缀名 -- 需要添加获取文件的后缀名
file_suffix = ''


def participle(sentence_list, stop_words):
    if stop_words:
        split_words_list = []
        if sentence_list:
            for sentence in sentence_list:
                sentence = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', sentence, flags=re.MULTILINE)
                sentence = pattern.sub(r'', sentence)
                # print(sentence)
                split_words = jieba.lcut(sentence.lower())
                words = list(filter(lambda x: x.strip(), split_words))
                words_list = list(filter(lambda x: x not in stop_words, words))
                split_words_list.append(' '.join(words_list))
        else:
            logger.error('sentence_list is null')
        return split_words_list
    else:
        logger.error('Stop words are not loaded')


def load_data(data_dir):
    if data_dir:
        sentence_split = []
        filename = os.listdir(data_dir)
        for name in filename:
            file = data_dir + '/' + name
            if file.endswith('.txt'):
                if os.path.exists(file):
                    with open(file, 'rt', encoding='utf-8') as f:
                        for sentence in f:
                            sentence_split.append(sentence)
                else:
                    logger.error('This file %s is not exist.' % file)
        return sentence_split
    else:
        logger.error('The data_dir is not exist.')


def load_stop_word(file_path):
    if os.path.exists(file_path):
        stop_words = []
        with open(file_path, 'rt', encoding='utf-8') as f:
            for word in f:
                stop_words.append(word.strip('\n'))
        return stop_words
    else:
        logger.error("file path: %s is not exist" % file_path)


def write_data(data, file_path_train, file_path_test):
    size = len(data)
    hf_size = math.ceil(size / 2)
    data_train = data[0:hf_size]
    data_test = data[hf_size::]
    with open(file_path_train, 'w', encoding='utf-8') as f:
        for d in data_train:
            f.write(d + "\n")
    with open(file_path_test, 'w', encoding='utf-8') as f:
        for d in data_test:
            f.write(d + "\n")


def main():
    # sentence_list = load_data('e:/tmp/output_one/neg')
    # stop_words = load_stop_word('dependencies/stop_word.txt')
    #
    # split_words_list = participle(sentence_list, stop_words)
    # #write_data(split_words_list, 'e:/tmp/output_one/out_put/neg.txt')
    path = 'e:/tmp/taptap_write/split_word'
    sentence_list = load_data('E:\\tmp\\taptap_write\\sentence')
    stop_words = load_stop_word('dependencies/stop_word.txt')
    split_words_list = participle(sentence_list, stop_words)
    write_data(split_words_list, path + '/taptap.pos', path + '/taptap_test.pos')


if __name__ == '__main__':
    main()
