# -*- coding: utf-8 -*-
'''
@project:Edge Computing
@author:zongwangz
@time:19-4-29 下午3:07
@email:zongwang.zhang@outlook.com
需要说明的是我们对部分值做了简化
'''
from global_variables import *
import numpy as np
class device:
    def __init__(self):
        self.esc = parameter["esc"]  #the effective switched capacitiance
        self.fmax_cpu = parameter["fmax_cpu"]

    def calTime(self,energy,computing_circle):
        # f_i = np.sqrt(energy/(self.esc*computing_circle))
        # if f_i > self.fmax_cpu:
        #     # print("the allocated power for computing in local device is more than need")
        #     f_i = self.fmax_cpu
        # local_time = computing_circle/(f_i)
        # return local_time

        #这里我们做了简化，区别了能量对本地处理任务的影响
        if energy == 400:
            return 50
        if energy == 200:
            return 300

if __name__ == '__main__':
    device = device()
    print(device.calTime(400,6.5))