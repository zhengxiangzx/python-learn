# -*- coding: utf-8 -*-
"""
训练词向量前处理，对所有的评论分句分词处理
基于pyspark的分句分词
"""
import re
from pyltp import SentenceSplitter

import jieba
from pyspark.sql.functions import udf, explode
from pyspark.sql.types import StringType, ArrayType
from smart_open import smart_open

from dependencies._compat import get_module_res
from dependencies.spark import start_spark
import logging

logger = logging.getLogger(__name__)
# 加载自定义词典
jieba.load_userdict(get_module_res('user_dict.txt'))
# 句子过滤条件
pattern = re.compile(u'[^\u4e00-\u9fa5^a-z^A-Z]')


def load_data(session, input_file):
    """
    加载评论语料，基于pyspark读取hdfs上的数据
    :param session: 创建的spark会话
    :param input_file: 读取的文件的hdfs地址
    :return: 返回的是 dataframe（只选择了contents字段）训练词向量用
    """
    # 配置文件 只读取csv的文件
    file_path = input_file + '/*.csv'
    # 使用spark对取csv文件
    dfs = session.read.csv(file_path, header=True, encoding='utf-8')
    # 选择要使用的字段内容（评论的内容）
    df = dfs.select('contents')
    return df


def transform_data(df):
    """
    数据处理，定义自定义函数来分句分词（基于spark的dataframe）
    :param df: 读取的语料dataframe格式的
    :return: 返回处理完的语料dataframe格式的
    """
    # 定义分句的udf函数（返回每个评论分完句子的一个list（每个评论都返回一个list））
    sentence_split = udf(clause, ArrayType(StringType()))
    # 定义分词的udf函数（返回每个句子分完词的一个string串（每个句子返回一个串））
    word_segment = udf(participle, StringType())
    # 使用分句的udf函数（返回的结果拼接到被分句的后面一个字段内）
    dfs = df.withColumn('sentences', sentence_split(df.contents))
    # 把分完句子的字段一行拆分成多行数据(分完句的是一个list放到一个字段内 需要一行拆成多行)
    data_frame = dfs.select(explode(dfs.sentences).alias("sentence"))
    # 使用分词的udf函数 进行分词
    df_word = data_frame.withColumn('sentence_word', word_segment(data_frame.sentence))
    # 把分完词的 字段筛选出来返回（写入输出文件）selectExpr(也是查询，可以起别名 可以做一些运算 可以用一些函数)
    df_ret = df_word.selectExpr('sentence_word as sentence')
    return df_ret


def clause(sentences):
    """
    分句, 用pyltp的SentenceSplitter分的句子，基于标点符号
    :param sentences:传入的评论句段
    :return:返回一个list 分完的句子
    """
    # 把传入的数据字母变小写
    sentences = str(sentences).lower().encode('utf-8')
    # 进行分句 哈工大的分句
    sentence = SentenceSplitter.split(sentences)
    # strip()操作
    sentence_list = list(filter(lambda x: x.strip(), sentence))
    return sentence_list


def participle(sentence):
    """
    分词
    :param sentence: 句子
    :return:
    """
    # 加载停用词
    stop_words = load_stop_word()
    # 去掉url地址
    sentence = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', sentence, flags=re.MULTILINE)
    # 去掉非汉字字母的其他部分（只保留汉字字母）
    sentence = pattern.sub(r'', sentence)
    # 调用JieBa进行分词
    split_words = jieba.lcut(sentence.lower())
    # 去空格等符号
    words = list(filter(lambda x: x.strip(), split_words))
    # 去停用词
    words_list = list(filter(lambda x: x not in stop_words, words))
    # 返回分词结果
    return ' '.join(words_list)


def load_stop_word(path=None):
    """
    加载停用词
    :param path:停用词的文件地址
    :return: 返回停用词一个list列表
    """
    stop_words = []
    if path is None:
        path = get_module_res('stop_word.txt')
        with smart_open(path, 'rb', encoding='utf-8') as fin:
            for word in fin:
                stop_words.append(word.strip())
        return stop_words
    else:
        with smart_open(path, 'rb') as fin:
            for word in fin:
                stop_words.append(word.strip().decode('utf-8'))
        return stop_words


def writer_csv(data_frame, output_file):
    """
    处理完的语料写入到hdfs文件
    :param data_frame: 处理完分词返回的分词结果数据
    :param output_file: 保存数据的地址
    :return: '数据保存完成'
    """
    # 分完的词写入csv文件保存 （sep 分隔符）
    data_frame.write.csv(output_file, mode='overwrite', sep='\01', header=False)
    return '数据保存完成'


def main():
    spark_session, log, config = start_spark(app_name='nlp_clause',
                                             files=['./configs/sentence_spilt_config.json'])
    # 本地测试用
    # input_file = 'E:/tmp/review_csv/output'
    # output_file = 'E:/tmp/output_review'
    # data = load_data(spark_session, input_file)
    # data_transform = transform_data(data)

    data = load_data(spark_session, config['input_path'])
    data_transform = transform_data(data)
    writer_csv(data_transform, config['output_path'])


if __name__ == '__main__':
    main()
