#!/usr/bin/env python
# encoding: utf-8


import os
import sys
import platform

import imp


def loadLib(name, so_path):
    if name not in sys.modules:
        featureLib = imp.load_dynamic(name, so_path)
        return featureLib
    return sys.modules[name]


SentenceSplitter = None

try:
    from pyltp import SentenceSplitter
except:
    sysstr = platform.system()
    if (sysstr == "Linux"):
        # 当前工作目录 spark提交任务时使用--files
        path = os.getcwd() + '/pyltp.cpython-36m-x86_64-linux-gnu.so'
        if os.path.exists(path):
            print('Load pyltp module from:', path)
            pyltp = loadLib('pyltp', path)
            SentenceSplitter = pyltp.SentenceSplitter
        else:
            print("Not found ", path)


def split_sentence(lines, logger=None):
    """
    分句
    :param lines:
    :return:
    """
    sentences = []
    if isinstance(lines, str):
        lines = [lines]

    if not SentenceSplitter:
        logger.warn('SentenceSplitter is not import')
        return lines

    for line in lines:
        for subs in SentenceSplitter.split(line):
            if len(subs.strip()) > 1:
                sentences.append(subs.strip())
    return sentences
