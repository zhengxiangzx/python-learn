# -*- coding: utf-8 -*-
from gensim.test.utils import get_tmpfile
from gensim.models.doc2vec import Doc2Vec

from jobs.doc2vec_learn import load_data

sentence_list = load_data('e:/tmp/csv_file')
model_dm = Doc2Vec.load('./doc2vec_test.txt')
vector = model_dm.infer_vector(['游戏', '不好玩'], epochs=500)
vector2 = model_dm.infer_vector(['游戏', '不好玩'], epochs=500)
print("2===", vector)
print(vector2)
test_sentence = u'游戏 垃圾'
test_text = test_sentence.split(' ')
inferred_vector = model_dm.infer_vector(doc_words=test_text, alpha=0.025, steps=500)
sims = model_dm.docvecs.most_similar([inferred_vector], topn=10)
for count, sim in sims:
    print(count, sim)
    sentence = sentence_list[count]
    print(sentence, sim, len(sentence))
