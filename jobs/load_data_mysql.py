# -*- coding: utf-8 -*-
from dependencies.spark import start_spark
import logging

logger = logging.getLogger(__name__)


def load_data(session, input_path, id):
    if input_path:
        data_frame = session.read.csv(path=input_path, header=True, encoding='utf-8')
        data_frame = data_frame.filter(
            'app_id in ' + id)
        if data_frame:
            print(data_frame.collect())
            return data_frame


def writer_csv(data_frame, output_file, id):
    (data_frame
     .write.csv(output_file + '/' + id, mode='overwrite', header=True))
    return None


def main():
    # gameid = ['69698', '5151', '60187', '47330', '54928', '10497', '12492', '55307', '2301', '70056', '50500', '74870',
    #           '34768', '35141', '91972', '6922', '69383', '85118', '85452', '69411', '85552', '31074', '69405', '70215',
    #           '59520', '66187', '10056', '85846', '33973', '71417']
    # input_path = 'E:\\tmp\\review_csv'
    # input_path = 'E:\\tmp\\csv_test'
    # output_path = 'E:\\tmp\\output_review'
    spark_session, log, config = start_spark(app_name='nlp_tokenization',
                                             files=['./configs/file_list_config.json'])
    gameid = ('69698', '5151', '60187', '47330', '54928', '10497', '12492', '55307', '2301', '70056', '50500', '74870',
              '34768', '35141', '91972', '6922', '69383', '85118', '85452', '69411', '62422', '31074', '69405', '70215',
              '59520', '66187', '10056', '85846', '33973', '71417')
    data_frame = load_data(spark_session, config[''], str(gameid))
    writer_csv(data_frame, config[''], id.strip())


if __name__ == '__main__':
    main()
