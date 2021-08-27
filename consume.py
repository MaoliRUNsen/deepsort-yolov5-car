#_*_coding:UTF-8_*_

'''
@Author��Runsen
'''
import json

import pika
import time

auth = pika.PlainCredentials(
    username='guest',
    password='guest',
) # �û��� / ����



connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        '127.0.0.1', # RabbitMQ ��ַ
        5672, # �˿ں�
        '/', # ��������
        auth, # ��֤
    )
) # ����RabbitMQ
channel = connection.channel() # ����RabbitMQͨ��

channel.queue_declare(
    queue='hzairport', # ���Ѷ�����
    durable=True, # �־û�
)


def callback(ch, method, properties, body):
    result =  json.loads(body)
    print(" [x] Received %r" % result["alert"])


channel.basic_consume(
    queue='hzairport', # ������
    auto_ack=True, # �Զ���Ӧ
    on_message_callback=callback, # �ص���Ϣ
)


time.sleep(5) # ģ������ʱ��
print("������")
channel.start_consuming()

