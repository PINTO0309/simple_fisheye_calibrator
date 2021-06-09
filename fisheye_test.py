
import os
import numpy as np
import cv2
from PIL import Image
import cvui
import sys
import copy

WINDOW_NAME = 'Simple Fisheye Calibrator'
cvui.init(WINDOW_NAME)

FILE_PATH = 'fisheye_test.jpg'
dir_name, file_name = os.path.split(FILE_PATH)
file_name_short, ext = os.path.splitext(file_name)

frame = np.zeros((1100, 2000, 3), np.uint8)
view_scale_format = '%.2Lf'
SCALE_VALUE_DEFAULT = [1.50]
scale_value = copy.deepcopy(SCALE_VALUE_DEFAULT)
PARAM1_DEFAULT = [-0.63]
PARAM2_DEFAULT = [-0.15]
PARAM3_DEFAULT = [0.00]
PARAM4_DEFAULT = [0.00]
PARAM5_DEFAULT = [0.55]
param1 = copy.deepcopy(PARAM1_DEFAULT)
param2 = copy.deepcopy(PARAM2_DEFAULT)
param3 = copy.deepcopy(PARAM3_DEFAULT)
param4 = copy.deepcopy(PARAM4_DEFAULT)
param5 = copy.deepcopy(PARAM5_DEFAULT)

image = Image.open(FILE_PATH)
image = np.array(image, dtype=np.uint8)
h, w = image.shape[0], image.shape[1]

while True:
    img = image.copy()

    frame[:] = (60, 60, 60)

    cvui.beginRow(frame, 10, 20, 100, 50)
    cvui.text('FilenPath:', 1.4)
    cvui.text(FILE_PATH, 1.4)
    cvui.endRow()

    cvui.beginRow(frame, 10, 70, 100, 50)
    cvui.text('Scale   :', 1.4)
    cvui.trackbar(300, scale_value, 0.01, 2.00, 1, view_scale_format)
    cvui.endRow()

    cvui.beginRow(frame, 10, 120, 100, 50)
    cvui.endRow()

    cvui.beginRow(frame, 10, 170, 100, 50)
    cvui.text('Distortion Parameters', 1.4)
    cvui.endRow()

    cvui.beginRow(frame, 10, 220, 100, 50)
    cvui.text('Param1   :', 1.0)
    cvui.trackbar(300, param1, -2.00, 2.00, 1, view_scale_format)
    cvui.endRow()

    cvui.beginRow(frame, 10, 270, 100, 50)
    cvui.text('Param2   :', 1.0)
    cvui.trackbar(300, param2, -2.00, 2.00, 1, view_scale_format)
    cvui.endRow()

    cvui.beginRow(frame, 10, 320, 100, 50)
    cvui.text('Param3   :', 1.0)
    cvui.trackbar(300, param3, -1.00, 1.00, 1, view_scale_format)
    cvui.endRow()

    cvui.beginRow(frame, 10, 370, 100, 50)
    cvui.text('Param4   :', 1.0)
    cvui.trackbar(300, param4, -1.00, 1.00, 1, view_scale_format)
    cvui.endRow()

    cvui.beginRow(frame, 10, 420, 100, 50)
    cvui.text('Param5   :', 1.0)
    cvui.trackbar(300, param5, -2.00, 2.00, 1, view_scale_format)
    cvui.endRow()

    mtx = np.array([[h,    0.,  w / 2],
                    [0.,   w,   h / 2],
                    [0.,   0.,  1    ]])
    dist = np.array(
        [
            param1,
            param2,
            param3,
            param4,
            param5
        ]
    )
    n_mtx = cv2.getOptimalNewCameraMatrix(
        mtx,
        dist,
        (img.shape[1], img.shape[0]),
        0
    )[0]
    map = cv2.initUndistortRectifyMap(
        mtx,
        dist,
        np.eye(3),
        n_mtx,
        (img.shape[1], img.shape[0]),
        cv2.CV_32FC1
    )

    mapx = map[0]*scale_value[0] + (1-scale_value[0])*w/2
    mapy = map[1]*scale_value[0] + (1-scale_value[0])*h/2

    img = cv2.remap(
        img,
        mapx,
        mapy,
        cv2.INTER_CUBIC
    )

    view_image = cv2.resize(
        img,
        None,
        fx=0.7,
        fy=0.7,
        interpolation=cv2.INTER_NEAREST
    )
    cvui.image(frame, 600, 20, view_image[:,:,::-1])

    if cvui.button(frame, 230, 500, 100, 30, "RESET"):
        scale_value = copy.deepcopy(SCALE_VALUE_DEFAULT)
        param1 = copy.deepcopy(PARAM1_DEFAULT)
        param2 = copy.deepcopy(PARAM2_DEFAULT)
        param3 = copy.deepcopy(PARAM3_DEFAULT)
        param4 = copy.deepcopy(PARAM4_DEFAULT)
        param5 = copy.deepcopy(PARAM5_DEFAULT)

    if cvui.button(frame, 380, 500, 100, 30, "SAVE"):
        if dir_name:
            path = f'{dir_name}/{file_name}_{param1[0]}_{param2[0]}_{param3[0]}_{param4[0]}_{param5[0]}{ext}'
        else:
            path = f'./{file_name_short}_{param1[0]}_{param2[0]}_{param3[0]}_{param4[0]}_{param5[0]}{ext}'
        print(path)
        cv2.imwrite(path, img[:,:,::-1])

    cvui.imshow(WINDOW_NAME, frame)
    cvui.update()

    # ESC
    if cv2.waitKey(20) == 27:
        break