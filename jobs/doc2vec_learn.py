# -*- coding: utf-8 -*-
import jieba
import os
import logging
import pandas as pd
from pyltp import Segmentor
from pyltp import SentenceSplitter

from gensim.models.doc2vec import TaggedDocument, Doc2Vec, Doc2VecTrainables

# doc2vec测试
logger = logging.getLogger(__name__)
jieba.load_userdict('dependencies/user_dict.txt')
LTP_DATA_DIR = 'E:\\pyltp_modle\\ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
segmentor = Segmentor()
segmentor.load_with_lexicon(cws_model_path, 'E:\\pyltp_modle\\ltp_data_v3.4.0\\lexicon\\user_dict.txt')


def main():
    sentence_list = load_data('e:/tmp/csv_file')
    stop_words = load_stop_word('dependencies/stop_word.txt')
    # split_words_list = participle(sentence_list, stop_words)
    print(sentence_list)
    # document_train = train_prepare(split_words_list)
    # model_dm = train(document_train)
    # test_sentence = u'这个 游戏 垃圾'
    # test_text = test_sentence.split(' ')
    # inferred_vector = model_dm.infer_vector(doc_words=test_text, alpha=0.025, steps=500)
    # sims = model_dm.docvecs.most_similar([inferred_vector], topn=10)
    # for count, sim in sims:
    #     print(count, sim)
    #     sentence = sentence_list[count]
    #     print(sentence, sim, len(sentence))


# def participle(sentence_list, stop_words):
#     if stop_words:
#         split_words_list = []
#         if sentence_list:
#             for sentence in sentence_list:
#                 split_words = list(segmentor.segment(sentence))
#                 words = list(filter(lambda x: x.strip(), split_words))
#                 words_list = list(filter(lambda x: x not in stop_words, words))
#                 split_words_list.append(' '.join(words_list))
#             segmentor.release()
#         else:
#             logger.error('sentence_list is null')
#         return split_words_list
#     else:
#         logger.error('Stop words are not loaded')


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


def load_data(data_dir):
    if data_dir:
        sentence_split = []
        filename = os.listdir(data_dir)
        for name in filename:
            file = data_dir + '/' + name
            if os.path.exists(file):
                df_train = pd.read_csv(file, encoding='utf-8', engine='python')
                sentence_list = list(df_train['contents'])
                for sentence in sentence_list:
                    sent_split = SentenceSplitter.split(sentence.encode('utf-8'))
                    for sent in sent_split:
                        if len(sent) > 3:
                            sentence_split.append(sent)
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
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(cut_sentence)]
    # for i, text in enumerate(cut_sentence):
    #     word_list = text.split(' ')
    #     ll = len(word_list)
    #     word_list[ll - 1] = word_list[ll - 1].strip()
    #     document = TaggedDocument(word_list, tags=[i])
    #     x_train.append(document)
    print("documents===========", documents)
    return documents


def train(x_train, size=300):
    model = Doc2Vec(x_train, min_count=1, window=3, vector_size=size, sample=1e-3, negative=5,
                    workers=1)
    model.train(x_train, total_examples=model.corpus_count, epochs=100)
    model.save('./doc2vec_test.txt')
    return model


if __name__ == '__main__':
    main()
