#_*_coding:UTF-8_*_

'''
@Author��Runsen
'''

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

import cv2
import tracker
from detector import Detector
from utils.utils import Point
# ������λ��
from utils import *
from algorithm_core import Judge_overspeed

def alarm_video(video):
    # ��ʼ�� yolov5
    detector = Detector()
    # ����Ƶ
    capture = cv2.VideoCapture(video)
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
                if poly1.contains(Point(2 * x, 2 * y)) and line1_value[y, x] == 1:
                    start_time = time + (divided / fps)
                    print(f'�����һ��������: {label} | id: {track_id} | : ��ײ������� {x, y} | : start_time: {start_time}')
                    try:
                        print(f'��һ�ν���ʱ�䣺 {start_time}')
                    except:
                        print(f'�����ڣ�start_time ���: {label} | id: {track_id} | �ڽ����һ�����û�м�⵽')
                # ͬһ��ͬһtrack_id

                if poly2.contains(Point(2 * x, 2 * y)) and line2_value[
                    y, x] == 1 and track_id == track_id and label == label:
                    first_time = time + (divided / fps)
                    # spend_time_1 = first_time - start_time
                    print(f'����ڶ���������: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {first_time}')
                    try:
                        print(f'��һ�黨�ѵ�ʱ�䣺 {first_time - start_time}')
                    except:
                        print(f'�����ڣ�start_time ���: {label} | id: {track_id} | �ڽ����һ�����û�м�⵽')

                if poly3.contains(Point(2 * x, 2 * y)) and line3_value[
                    y, x] == 1 and track_id == track_id and label == label:
                    second_time = time + (divided / fps)
                    # spend_time_2 = second_time - first_time
                    print(f'���������������: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {second_time}')
                    try:
                        print(f'�ڶ��黨�ѵ�ʱ�䣺 {second_time - first_time}')
                    except:
                        print(f'�����ڣ�first_time ���: {label} | id: {track_id} | �ڽ���ڶ������ǰû�м�⵽')

                if poly4.contains(Point(2 * x, 2 * y)) and line4_value[
                    y, x] == 1 and track_id == track_id and label == label:
                    third_time = time + (divided / fps)
                    print(f'������Ŀ�������: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {third_time}')
                    try:
                        print(f'���Ŀ黨�ѵ�ʱ�䣺 {third_time - second_time}')
                    except:
                        print(f'�����ڣ�second_time ���: {label} | id: {track_id} | �ڽ�����������ǰû�м�⵽')

                if poly5.contains(Point(2 * x, 2 * y)) and line5_value[
                    y, x] == 1 and track_id == track_id and label == label:
                    fouth_time = time + (divided / fps)
                    print(f'��������������: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {fouth_time}')

                    try:
                        print(f'����黨�ѵ�ʱ�䣺 {fouth_time - third_time}')
                    except:
                        print(f'�����ڣ�second_time ���: {label} | id: {track_id} | �ڽ�����Ŀ����ǰû�м�⵽')

                if poly6.contains(Point(2 * x, 2 * y)) and line6_value[
                    y, x] == 1 and track_id == track_id and label == label:
                    fith_time = time + (divided / fps)
                    print(f'���������������: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {fith_time}')

                    try:
                        print(f'�����黨�ѵ�ʱ�䣺 {fith_time - fouth_time}')
                    except:
                        print(f'�����ڣ�second_time ���: {label} | id: {track_id} | �ڽ����������ǰû�м�⵽')

                if poly7.contains(Point(2 * x, 2 * y)) and line7_value[y, x] == 1 and track_id == track_id and label == label:
                    final_time = time + (divided / fps)
                    print(f'�뿪��ʱ��:: {label} | id: {track_id} | : ��ײ������� {x, y} | : time: {final_time}')
                while 2 * y >= 750  and track_id == track_id and label == label:
                    print(f'idx time divided ��� 0')
                    idx = 0
                    fps = capture.get(5)
                    divided = 0
                    time = 0
                    break


    capture.release()
    cv2.destroyAllWindows()
    try:
        print(start_time, first_time, second_time, third_time, fouth_time, fith_time, final_time)
    except Exception as e:
        print(e)

    return start_time, first_time, second_time, third_time, fouth_time, fith_time, final_time


start_time, first_time, second_time, third_time, fouth_time, fith_time, final_time = alarm_video('./video/test2.mp4')

print(Judge_overspeed(DISTANCE, start_time, first_time, second_time, third_time, fouth_time, fith_time, final_time))