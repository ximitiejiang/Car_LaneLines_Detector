#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:56:35 2019

@author: ubuntu
"""

import cv2
import numpy
import time

class CaptureManager(object):
    """用于管理摄像头的键盘捕获，鼠标捕获操作"""
    def __init__(self):
        self._is_writing_video = False
    
    def frame(self):
        pass
    
    def enter_frame():
        
        
    
    @property
    def is_writing_video(self):
        return self._is_writing_video
    
    @property
    def is_writing_image(self):
        return self._image_file_name is not None


class WindowManager(object):
    """用于管理窗口的打开关闭以及相应窗口的键盘快捷操作"""
    def __init__(self, 
                 window_name, 
                 keypressCallback = None, 
                 mouseCallback = None):
        self.keypressCallback = keypressCallback
        self.window_name = window_name
        self._is_window_created = False
    
    @property
    def is_window_created(self):
        return self._is_window_created
        
    def create_window(self):
        cv2.namedWindow(self.window_name)
        self._is_window_created = True
    
    def show(self, frame):
        cv2.imshow(self.window_name, frame)
        
    def destroy_window(self):
        cv2.destroyWindow(self.window_name)
        self._is_window_created = False
        
    def processEvents(self):
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode !=-1:
            keycode &= 0xFF
            self.keypressCallback(keycode)

    

class GeneralFramework(object):
    """通用的软件框架，集成了窗口管理，按键和鼠标管理"""
    def __init__(self, fram_name):
        self.window_manager = WindowManager(fram_name, self.my_keypress_callback)
        self.capture_manager = CaptureManager()
    
    def run(self):
        self.window_manager.createWindow()
        while self.window_manager.is_window_created:
            continue
    
    def my_keypress_callback(self, keycode): # ord('s') to get ASCII
        if keycode == 32:  # space: screenshot
            self.capture_manager.writeImage('aaa.jpg')
        elif keycode == 115: # key(s): start/stop
            if not self.capture_manager.is_writing_video:
                self.capture_manager.start_writing_video('new_video.avi')
            else:
                self.capture_manager.stop_writing_video()
        elif keycode == 27:  # esc
            self.window_manager.destroy_window()
            
    def my_mouse_callback(self);:
        pass
            
            
class Cameo(GeneralFramework):
    
    def __init__(self, frame_name='Cameo'):
        pass
    
    
if __name__ == '__main__':
    
    fm = Cameo()
    img = cv2.imread('chess.jpg',1)
    fm.run()
    
    
    
    
    