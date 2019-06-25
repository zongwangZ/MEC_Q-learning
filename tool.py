# -*- coding: utf-8 -*-
'''
@project:q_learning
@author:zongwangz
@time:19-6-17 下午7:50
@email:zongwang.zhang@outlook.com
'''
import copy
import os
import matplotlib.pyplot as plt
import ast
def optimal_action(observation):
    '''
    3个任务的能量充足
    :param observation:
    :return:
    '''
    task_done = int(observation.split(".")[0][1:])
    es_intensity = int(observation.split(".")[2])
    if task_done == 0:
        if es_intensity <= 6:
            # 选择在边缘服务器做
            action = 2
        if es_intensity > 6:
            # 400点能量在本地做
            action = 0
    elif task_done == 1:
        if es_intensity <= 6:
            # 选择在边缘服务器做
            action = 8
        if es_intensity > 6:
            # 400点能量在本地做
            action = 6
    elif task_done == 3:
        if es_intensity <= 6:
            # 选择在边缘服务器做
            action = 14
        if es_intensity > 6:
            # 400点能量在本地做
            action = 12
    elif task_done == 7:
        #终止状态
        action = -1
    return action


