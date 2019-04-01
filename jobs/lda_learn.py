# -*- coding: utf-8 -*-

import logging
from pyltp import SentenceSplitter

import jieba
import pandas as pd
import os

from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel

logger = logging.getLogger(__name__)


def participle(sentence_list, stop_words):
    if stop_words:
        split_words_list = []
        if sentence_list:
            for sentence in sentence_list:
                split_words = jieba.lcut(sentence.lower())
                words = list(filter(lambda x: x.strip(), split_words))
                words_list = list(filter(lambda x: x not in stop_words, words))
                split_words_list.append(words_list)
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
            if os.path.exists(file):
                if file.endswith('.txt'):
                    with open(file, 'rt', encoding='GB18030') as f:
                        for word in f:
                            sent_split = SentenceSplitter.split(word.lower().encode('utf-8'))
                            for sent in sent_split:
                                if len(sent) > 3:
                                    sentence_split.append(sent)
            else:
                logger.error('This file %s is not exist.' % file)
        return sentence_split
        # df_train = pd.read_csv(file, encoding='utf-8', engine='python')
        # sentence_list = list(df_train['contents'])
    #             for sentence in sentence_list:
    #                 sent_split = SentenceSplitter.split(sentence.encode('utf-8'))
    #                 for sent in sent_split:
    #                     if len(sent) > 3:
    #                         sentence_split.append(sent)
    #         else:
    #             logger.error('This file %s is not exist.' % file)
    #     return sentence_split
    # else:
    #     logger.error('The data_dir is not exist.')


def load_stop_word(file_path):
    if os.path.exists(file_path):
        stop_words = []
        with open(file_path, 'rt', encoding='utf-8') as f:
            for word in f:
                stop_words.append(word.strip('\n'))
        return stop_words
    else:
        logger.error("file path: %s is not exist" % file_path)


def main():
    sentence_list = load_data('E:\\tmp\\csv_test')
    stop_words = load_stop_word('dependencies/stop_word.txt')
    word_split = participle(sentence_list, stop_words)
    dictionary = Dictionary(word_split)
    corpus = [dictionary.doc2bow(text) for text in word_split]
    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=10)
    print(lda.print_topics(10))
    # load_data('E:\\tmp\\csv_test')


if __name__ == '__main__':
    main()
