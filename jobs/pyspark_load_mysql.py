# -*- coding: utf-8 -*-
import pymysql
from smart_open import smart_open
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
yesterday = yesterday.strftime("%Y-%m-%d")


def load_data_mysql(url, username, password, db_name, sql):
    db = pymysql.connect(url, username, password, db_name, charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return dict(data)


def process(local_data, select_count):
    all_dict = {}
    for name, count in local_data.items():
        count_sql = select_count[name]
        deff = int(count_sql) - int(count)
        all_dict[name] = deff
    writer_count(select_count)
    return all_dict


def writer_count(select_count):
    with smart_open('./dependencies/count_sentences.txt', 'wb', encoding='utf-8') as fin:
        for name, count in select_count.items():
            fin.write(name + " " + str(count) + "\n")
    return "重新添加完成"


def load_count():
    count_dict = {}
    with smart_open('./dependencies/count_sentences.txt', 'rb', encoding='utf-8') as fin:
        for line in fin:
            name = line.split(' ')[0].strip()
            count = line.split(' ')[1].strip()
            count_dict[name] = count
    return count_dict


def send_mail(data_all, count_all):
    sender = '729608526@qq.com'
    # 'guowanfeng@cyou-inc.com', 'shizhan_pt@cyou-inc.com',
    #                 'zhaomingming@cyou-inc.com',
    #                 'zhanghaitao@cyou-inc.com'
    #                 'chufucun@cyou-inc.com',  tianhonghan@cyou-inc.com
    receiver = ['zhengxiang@cyou-inc.com', '729608526@qq.com']
    subject = '标注系统-每天打标注数量统计--' + yesterday + '--测试'
    smtpserver = 'smtp.qq.com'
    username = '729608526@qq.com'
    password = 'uzksheulwgnxbchf'
    data_all['褚福存'] = data_all['chufucun']
    data_all['郭万丰'] = data_all['guowanfeng']
    data_all['施展'] = data_all['shizhan']
    data_all['张海涛'] = data_all['zhanghaitao']
    data_all['赵明明'] = data_all['zhaomingming']
    data_all['郑翔'] = data_all['zhengxiang']
    del data_all['chufucun'], data_all['guowanfeng'], data_all['shizhan'], data_all['zhanghaitao'], data_all[
        'zhaomingming'], data_all['zhengxiang']
    data = []
    for name, count in data_all.items():
        data.append(name + ' : ' + str(count))
    count_all['真实有效的评论总数量'] = count_all['countAll']
    del count_all['countAll']
    data_all = []
    for name, count in count_all.items():
        data_all.append(name + ' : ' + str(count))
    msg = MIMEText('Hi \n \n' + '\n'.join(data) + '\n' + ''.join(data_all), 'plain', 'utf-8')

    msg['From'] = formataddr(["郑翔", sender])
    msg['Subject'] = subject
    msg['To'] = ','.join(receiver)
    msg['Cc'] = 'zhengxiang@cyou-inc.com'

    smtp = smtplib.SMTP(smtpserver)
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def main():
    url = '10.129.129.50'
    username = 'gameprophet'
    password = 'Ch@ngy0u.com'
    db_name = 'gameprophet'
    sentence_count = "SELECT 'countAll',count(sentence) FROM sentence WHERE sentiemnt !=-1 AND sentiemnt !=0 AND target_type !=-1 AND target_type !=0"
    sql = "SELECT lable_username,COUNT(sentence) FROM sentence WHERE sentiemnt !=-1 AND target_type!=-1 and lable_username NOT IN ('tianhonghan','lumeng') GROUP BY lable_username"
    # data 每个人打标注的数量
    data = load_data_mysql(url, username, password, db_name, sql)
    # count_all 真实有效的评论数量
    count_all = load_data_mysql(url, username, password, db_name, sentence_count)
    data_count = load_count()
    # data_all 是每个人当天打的标注数量
    data_all = process(data_count, data)
    send_mail(data_all, count_all)
    print('发送邮件成功')


if __name__ == '__main__':
    main()
