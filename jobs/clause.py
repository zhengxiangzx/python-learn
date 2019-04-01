# -*- coding: utf-8 -*-

# 分句测试逻辑还需要修改
from pyltp import SentenceSplitter
from pyspark.sql.functions import expr, udf, array, explode, explode_outer
from pyspark.sql.types import StringType, MapType, IntegerType

from dependencies.spark import start_spark


def load_data(session, input_file):
    if input_file:
        file_path = input_file + '/*.csv'
        dfs = session.read.csv(file_path, header=True, encoding='utf-8')
        df = dfs.sort((expr('length(contents)')).desc())
        return df


def transform_data(df):
    sentence_split = udf(clause, MapType(IntegerType(), StringType()))
    dfs = df.withColumn('sentences', sentence_split(df.contents))
    data_frame = dfs.select(explode(dfs.sentences).alias('context_sort', "sentence"),
                            'app_id', 'id').selectExpr('sentence', '-1 as sentiemnt', 'app_id as gameid',
                                                       'id as reviewid', '-1 as target_type',
                                                       '-1 as lable_username', 'context_sort')
    return data_frame


def clause(sentences):
    sentences_list = {}
    if len(str(sentences).strip()) >= 10:
        sentence = SentenceSplitter.split(str(sentences).lower().encode('utf-8'))
        context_sort = 0
        string = []
        sentence_filter = list(filter(lambda x: len(x.strip()) > 3, sentence))
        for sent in sentence_filter:
            if len(sent.strip()) < 20:
                string.append(sent.strip())
                if len(''.join(string)) >= 25:
                    context_sort = context_sort + 1
                    sentences_list[context_sort] = ''.join(string).strip()
                    string = []
                elif 20 <= len(''.join(string)) < 25:
                    context_sort = context_sort + 1
                    sentences_list[context_sort] = ''.join(string).strip()
                    string = []
            else:
                context_sort = context_sort + 1
                sentences_list[context_sort] = sent.strip()
    return sentences_list


def writer_csv(data_frame, output_file):
    (data_frame
     .write.csv(output_file, mode='overwrite', sep='\01', header=False))
    return None


def main():
    spark_session, log, config = start_spark(app_name='nlp_clause',
                                             files=['./configs/file_list_config.json'])
    input_file = 'E:/tmp/review_csv/output'
    output_file = 'E:/tmp/output_review'
    data = load_data(spark_session, input_file)
    data_transform = transform_data(data)
    # writer_csv(data_transform, output_file)
    uu = '结果发现不太像探碗蓝月。包括也可以让嫔妃。如果亲密度低了。翰林院感觉好像还还有关卡那里尽量加一个加速按钮,还有很多地方可以让这款游戏更好。个加速按钮，强抢民女啦什么之类的那种很常见的剧情。'
    print(clause(uu))


if __name__ == '__main__':
    main()
