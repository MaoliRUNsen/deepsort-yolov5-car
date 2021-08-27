#_*_coding:UTF-8_*_
'''
@Author��Runsen
'''
import json

'''
@Author��Runsen


˼·����ʼ������
���㣺�����ε�ƽ���ٶ�
�жϵ����������ε�ƽ���ٶ��ǲ���С��ƽ���ٶȣ���������ˣ��ͽ��б�������

205  455  295 455
224  480  342 480
253  490  351 490
277  516  391 516
304  546  440 546
351  595  506 595
402  650  590 650
482  727  712 727


'''
import pika
import base64
import cv2
import tracker
from detector import Detector
from utils.utils import Point
# ������λ��
from utils import *

# ����MQ
credentials = pika.PlainCredentials(
    username='guest',
    password='guest',
)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='127.0.0.1',  # MQ��ַ(����)
        port=5672,  # �˿ں�,ע����5672,����15672
        virtual_host='/',  # ��������
        credentials=credentials,  # �û���/����
    )
)


channel = connection.channel()
channel.queue_declare(
    queue='hzairport',  # ������
    durable=True,  # ʹ���г־û�
)




def Judge_overspeed(distance, first_time, second_time, third_time, fouth_time, fith_time, final_time):

    # if first_time and start_time:
    #     fisrt_speed = distance / (first_time - start_time)
    # else:
    #     fisrt_speed = 0

    if second_time and first_time:
        fisrt_speed = distance / (second_time - first_time)
    else:
        fisrt_speed = 0

    if third_time and second_time:
        second_speed = distance / (third_time - second_time)
    else:
        second_speed = 0

    if fouth_time and third_time:
        third_speed = distance / (fouth_time - third_time)
    else:
        third_speed = 0

    if fith_time and fouth_time:
        fouth_speed = distance / (fith_time - fouth_time)
    else:
        fouth_speed = 0

    if final_time and fith_time:
        last_speed = distance / (final_time - fith_time)
    else:
        print("ʲô����ģ�ͣ��ⶼ��ⲻ��")
        last_speed = 3

    print(fisrt_speed, second_speed, third_speed, fouth_speed, last_speed)
    # ����ƽ���ٶ�

    # avg_speed = (fisrt_speed + second_speed + third_speed + fouth_speed  + last_speed) / 6
    #
    # speeds = [fisrt_speed, second_speed, third_speed, fouth_speed, last_speed]

    if last_speed > THRESHOLD_SPEED:
        alert =  True
    else:
        alert = False

    message = {
        "alert": alert,
    }
    return message





def alarm(video=None):
    # ��ʼ�� yolov5
    detector = Detector()
    # ����Ƶ
    # video_path = r'rtsp://admin:nianguo2020@192.168.31.64:554/Streaming/Channels/101?transportmode=unicast'

    if video:
        capture = cv2.VideoCapture(video)
    else:
        # ��ʾ����ͷ
        capture = cv2.VideoCapture(0)
    # capture.set(5,capture.get(5))

    idx = 0
    fps = capture.get(5)
    divided = 0
    time = 0

    while True:
        # ��ȡÿ֡ͼƬ
        _, im = capture.read()

        if im is None:
            break
        # ��С�ߴ磬1920x1080->960x540
        im = cv2.resize(im, (960, 540))

        list_bboxs = []

        # bboxes �� yolov5���ĵ�
        # eg: (93, 192, 116, 218, 'truck', tensor(0.61563, device='cuda:0')
        # x1, y1, x2, y2, lbl, conf
        bboxes = detector.detect(im)

        # ��������� ��bbox
        if len(bboxes) > 0:
            list_bboxs = tracker.update(bboxes, im)

        idx += 1
        divided = idx % fps

        if divided == 0: time += 1

        if len(list_bboxs) > 0:
            # ----------------------�ж�ײ��----------------------
            for item_bbox in list_bboxs:
                x1, y1, x2, y2, label, track_id = item_bbox
                # ײ�߼��㣬(x1��y1)��y����ƫ�Ʊ��� 0.0~1.0
                x = int((x1 + x2) / 2)
                y = y2

                # if poly1.contains(Point(2 * x, 2 * y)) and line1_value[y, x] == 1:
                #     start_time = time + (divided / fps)
                #     print(f'�����һ��������: {label} | id: {track_id} | : ��ײ������� {x, y} | : start_time: {start_time}')

                # ͬһ��ͬһtrack_id

                if poly2.contains(Point(2 * x, 2 * y)) and line2_value[y, x] == 1 :
                    first_time = time + (divided / fps)
                    # spend_time_1 = first_time - start_time
                    print(f'�����һ��������: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {first_time}')

                    # try:
                    #     print(f'��һ�ν���ʱ�䣺 {start_time}')
                    # except:
                    #     start_time = 0
                    #     print(f'�����ڣ�start_time ���: {label} | id: {track_id} | �ڽ����һ�����û�м�⵽')
                    #


                if poly3.contains(Point(2 * x, 2 * y)) and line3_value[ y, x] == 1 and track_id == track_id and label == label:
                    second_time = time + (divided / fps)
                    # spend_time_2 = second_time - first_time
                    print(f'����ڶ���������: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {second_time}')

                    try:
                        print(f'��һ�黨�ѵ�ʱ�䣺 {second_time - first_time }')
                    except:
                        print(f'�����ڣ�first_time ���: {label} | id: {track_id} | �ڽ����һ�����û�м�⵽')
                        first_time = 0


                if poly4.contains(Point(2 * x, 2 * y)) and line4_value[ y, x] == 1 and track_id == track_id and label == label:
                    third_time = time + (divided / fps)
                    print(f'���������������: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {third_time}')

                    try:
                        print(f'�ڶ��黨�ѵ�ʱ�䣺 {third_time  - second_time}')
                    except:
                        print(f'�����ڣ�second_time ���: {label} | id: {track_id} | �ڽ���ڶ������ǰû�м�⵽')
                        first_time = second_time = 0


                if poly5.contains(Point(2 * x, 2 * y)) and line5_value[
                    y, x] == 1 and track_id == track_id and label == label:
                    fouth_time = time + (divided / fps)
                    print(f'��������������: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {fouth_time}')

                    try:
                        print(f'���Ŀ黨�ѵ�ʱ�䣺 {third_time - second_time}')
                    except:
                        print(f'�����ڣ�third_time ���: {label} | id: {track_id} | �ڽ�����������ǰû�м�⵽')
                        first_time = second_time = third_time = 0



                if poly6.contains(Point(2 * x, 2 * y)) and line6_value[
                    y, x] == 1 and track_id == track_id and label == label:
                    fith_time = time + (divided / fps)
                    print(f'��������������: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {fith_time}')
                    try:
                        print(f'����黨�ѵ�ʱ�䣺 {fouth_time - third_time}')
                    except:
                        print(f'�����ڣ�fouth_time ���: {label} | id: {track_id} | �ڽ�����Ŀ����ǰû�м�⵽')

                        first_time = second_time = third_time = fouth_time = 0


                if poly7.contains(Point(2 * x, 2 * y)) and line7_value[ y, x] == 1 and track_id == track_id and label == label:
                    final_time = time + (divided / fps)
                    print(f'�뿪��ʱ��:: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {final_time}')
                    message = Judge_overspeed(DISTANCE,first_time, second_time, third_time, fouth_time,fith_time, final_time)

                    # �����Ʊ���ַ���
                    img_data = base64.b64encode(im).decode('utf-8')

                    print(message["alert"])
                    message["img"] = img_data
                    # ����Ϣ����
                    message = json.dumps(message)
                    channel.basic_publish(
                        exchange='',
                        routing_key='hzairport',  # ����rabbitmq����Ϣ���͵� queue_name_test ������
                        body=message,  # ������Ϣ������
                        properties=pika.BasicProperties(delivery_mode=2, )  # ��Ϣ�־û�
                    )




                while 750 < 2 * y < 800  and 600 < 2 * x < 750 and track_id == track_id and label == label:
                    print(f'idx time divided ��� 0')
                    idx = 0
                    fps = capture.get(5)
                    divided = 0
                    time = 0
                    break


    capture.release()
    cv2.destroyAllWindows()
    try:
        print(first_time, second_time, third_time, fouth_time, fith_time, final_time)
    except Exception as e:
        print(e)



alarm("./video/test.mp4")
alarm("./video/test1.mp4")
alarm("./video/test2.mp4")
alarm("./video/test4.mp4")
alarm("./video/test5.mp4")
alarm("./video/test6.mp4")
alarm("./video/test7.mp4")
alarm("./video/test8.mp4")
alarm("./video/test9.mp4")
alarm("./video/test10.mp4")
alarm("./video/test11.mp4")
alarm("./video/test12.mp4")
alarm("./video/test13.mp4")
alarm("./video/test14.mp4")
alarm("./video/test15.mp4")
alarm("./video/test16.mp4")