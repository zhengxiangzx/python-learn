#!/usr/bin/env python
# -*- coding:utf-8 -*
"""
 数据处理，可以参考《自然语言处理时，通常的文本清理流程是什么？》
 以英文文本处理为例。大致分为以下几个步骤：
    1. Normalization
        标准化：字母小写转换、标点符号处理等，英文里通常只要A-Za-z0-9，根据实际情况确定处理
    2. Tokenization
        Token 是“符号”的高级表达。一般指具有某种意义，无法再分拆的符号。就是将每个句子分拆成一系列词，英文里词之间天然有空格。
    3. Stop words
        Stop Word 是无含义的词，例如'is'/'our'/'the'/'in'/'at'等。它们不会给句子增加太多含义，单停止词是频率非常多的词。 为了减少我们要处理的词汇量，从而降低后续程序的复杂度，需要清除停止词。
    4. Part-of-Speech Tagging   词性标注
    5. Named Entity Recognition 命名实体
    6. Stemming and Lemmatization  将词的不同变化和变形标准化
"""
import os
import sys
import re
import time
import logging

from ._compat import *
from .pyltp import split_sentence

import jieba

logger = logging.getLogger(__name__)

USER_DICT_NAME = "userdict.txt"

# 加载词典
jieba.load_userdict(get_module_res(USER_DICT_NAME))


# 停用词
def _load_stopwords(f):
    f_name = resolve_filename(f)
    stopwords = []
    for lineno, ln in enumerate(f, 1):
        line = ln.strip()
        stopwords.append(line)
    return stopwords


STOPWORDS_NAME = "stopwords.txt"
stopwords = _load_stopwords(get_module_res(STOPWORDS_NAME))


def wordtokenizer(raw_sentences, sentences):
    '''
    预处理文本：标准化，分句，分词，停用词处理
    :param concent_lines:
    :param sentences:
    :return:
    '''
    if not raw_sentences:
        return []
    if isinstance(raw_sentences, str):
        raw_sentences = [raw_sentences]
    for line in raw_sentences:
        try:
            # 1. Normalization   标准化
            line = line.lower()
            # 2. Tokenization
            segs = jieba.lcut(line)
            # segs = [v for v in segs if not str(v).isdigit()]  # 去数字
            segs = list(filter(lambda x: x.strip(), segs))  # 去空格
            # segs = list(filter(lambda x: len(x) > 1, segs))  # 去长度为1的字符
            # 3. Stop words
            segs = list(filter(lambda x: x not in stopwords, segs))  # 去停用词
            sentences.append(' '.join(segs))
        except Exception:
            logger.error(line)
