# -*- coding: utf-8 -*-
import jieba
import os
import logging
import pandas as pd
from gensim.models.doc2vec import TaggedDocument, Doc2Vec, Doc2VecTrainables
import pymysql

# 对评论进行聚类
logger = logging.getLogger(__name__)
jieba.load_userdict('dependencies/user_dict.txt')


def participle(sentence_list, stop_words):
    if stop_words:
        split_words_list = []
        if sentence_list:
            for sentence in sentence_list:
                split_words = jieba.lcut(sentence.lower())
                words = list(filter(lambda x: x.strip(), split_words))
                words_list = list(filter(lambda x: x not in stop_words, words))
                split_words_list.append(' '.join(words_list))
        else:
            logger.error('sentence_list is null')
        return split_words_list
    else:
        logger.error('Stop words are not loaded')


def load_data_mysql(url, username, password, db_name, sql):
    db = pymysql.connect(url, username, password, db_name, charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return list(data)


def load_data(data_dir):
    if data_dir:
        sentence_split = []
        filename = os.listdir(data_dir)
        for name in filename:
            file = data_dir + '/' + name
            if os.path.exists(file):
                df_train = pd.read_csv(file, engine='python')
                sentence_list = list(df_train['contents'])
                for sentence in sentence_list:
                    if len(sentence) > 3:
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


def train_prepare(cut_sentence):
    # documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(cut_sentence)]
    x_train = []
    for i, text in enumerate(cut_sentence):
        word_list = text.split(' ')
        ll = len(word_list)
        word_list[ll - 1] = word_list[ll - 1].strip()
        document = TaggedDocument(word_list, tags=[i])
        x_train.append(document)
    return x_train
    # return documents


def train(x_train, size=300):
    model = Doc2Vec(x_train, min_count=1, window=3, vector_size=size, sample=1e-3, negative=5,
                    workers=1)
    model.train(x_train, total_examples=model.corpus_count, epochs=500)
    model.save('e:/tmp/model_save/doc2vec_test.txt')
    return model


def main():
    sentence_list = load_data('e:/tmp/csv_test')
    stop_words = load_stop_word('dependencies/stop_word.txt')
    split_words_list = participle(sentence_list, stop_words)
    document_train = train_prepare(split_words_list)
    model_dm = train(document_train)
    url = '10.129.129.50'
    username = 'gameprophet'
    password = 'Ch@ngy0u.com'
    db_name = 'gameprophet'
    sql = "SELECT sentence FROM sentence_01 WHERE sentiemnt !=-1 AND sentiemnt !=0 AND target_type !=-1 AND target_type !=0"
    data = load_data_mysql(url, username, password, db_name, sql)
    for (row,) in data:
        test_list = []
        test_list.append(row)
        test_01 = participle(test_list, stop_words)
        for test_02 in test_01:
            test_text = test_02.split(' ')
            print(test_text)
            inferred_vector = model_dm.infer_vector(doc_words=test_text, alpha=0.025, steps=500)
            sims = model_dm.docvecs.most_similar([inferred_vector], topn=10)
            for count, sim in sims:
                print(count, sim)
                sentence = sentence_list[count]
                print(sentence, sim, len(sentence))


if __name__ == '__main__':
    main()
