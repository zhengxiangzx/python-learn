# -*- coding: utf-8 -*-
from dependencies.spark import start_spark

"""
拼字符串
"""


def load_data(session, input_path):
    if input_path:
        data_frame = session.read.csv(path=input_path, header=True, encoding='utf-8')
        return data_frame


def transform_data(df):
    # 返回类型为字符串类型 , 'rating_value as total_score'
    df_transformed = df.selectExpr('id as id', 'name as gamename', 'review_times as review_num',
                                   '1 as details',
                                   'rating_value as total_score', '1 as hot_lable', 'id as gameid', 'author as firm',
                                   '1 as setup_num',
                                   '1 as concern_num', '1 as latest_version', '1 as android_score', '1 as ios_score',
                                   '1 as nearly_7_d_score', '1 as image_url', 'category as game_type',
                                   '1 as rank_list', '1 as score_trends_id', '1 as is_action')
    return df_transformed


def writer_csv(data_frame, output_file):
    (data_frame
     .write.csv(output_file, mode='overwrite', header=True))
    return None


def main():
    input_path = 'E:\\tmp\\game_csv'
    output_path = 'E:\\tmp\\output'
    spark_session, log, config = start_spark(app_name='nlp_tokenization',
                                             files=['./configs/file_list_config.json'])
    data_frame = load_data(spark_session, input_path)
    writer_csv(transform_data(data_frame), output_path)


if __name__ == '__main__':
    main()
