#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:13:47 2019

@author: ubuntu
"""

import numpy as np
import cv2

"""refer: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_calib3d/py_calibration/py_calibration.html#calibration
          https://blog.csdn.net/weixin_38746685/article/details/81613065
"""
def get_obj_img_points(images,grid=(7,8)):
    """传入一组图片，识别出每张图片的图片角点img_point，并生成目标角点obj_point，两者是对应关系，用于做标定
    Args:
        images
        grid(tuple): (m,n)代表棋盘m个横点n个竖点，也就是(w,h)
    Return:
        obj_points(array): (m*n, 3)代表默认的把图片第一个角点对齐原点(0,0),其他点单位增加1的手动标注的坐标点(0~w, 0~h, 0)
        img_points(array): (m*n, 1, 2)代表图片实际的每一个角点在图像上的坐标x,y
    """
    object_points=[]
    img_points = []
    for img in images:
        # 先生成0数组
        object_point = np.zeros((grid[0]*grid[1],3),np.float32)  # (m*n, 3)
        object_point[:,:2]= np.mgrid[0:grid[0], 0:grid[1]].T.reshape(-1,2)  # 第一列填充0~6, 第二列填充0～7,从而得到(x,y,z=0)的坐标值(左上角为0,0原点)

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray, grid, None) # 寻找角点(预提供角点w,h个数), 输出角点坐标(m*n, 1,2)，1行2列的坐标
        if ret:  # 如果有return说明找到了角点
            object_points.append(object_point)
            img_points.append(corners)

    return object_points,img_points


def cal_undistort(img, objpoints, imgpoints):
    """基于目标角点和图片角点进行图片畸变修正
    其中calibrateCamera()函数可以返回相机矫正矩阵(mtx)，失真系数(dist)，旋转向量(rvecs)，平移向量(tvecs)
    Args:
        img
        objpoints
        imgpoints
    Return:
        dst
    """
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[1::-1], None, None)
    dst = cv2.undistort(img, mtx, dist, None, mtx)
    return dst


def get_M():
    """图片视角转换为鸟瞰视角
    """
    src


if __name__ == '__main__':
    img_path = './chess.jpg'
    img = cv2.imread(img_path)
    obj_points, img_points = get_obj_img_points([img], grid=(7,8))
    
    # draw
#    cv2.drawChessboardCorners(img, (7,8), corners, ret)
#    cv2.imshow('img', img)
#    cv2.waitKey(500)
    
    new_img = cv2.imread('./chess2.jpg')
    new_img = cal_undistort(new_img, obj_points, img_points)
    cv2.imshow('new img', new_img)
    cv2.waitKey(5000)
    