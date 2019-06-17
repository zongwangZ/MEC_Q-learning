# -*- coding: utf-8 -*-
'''
@project:Edge Computing
@author:zongwangz
@time:19-4-29 下午3:46
@email:zongwang.zhang@outlook.com
需要需要说明的是：
我们将部分值做了简化
'''
import numpy as np
from global_variables import *

class cloudServer:
    def __init__(self):
        self.tr_rtt = parameter["tr_cs"]
        self.f_cs = parameter["f_cs"]
        self.e_max = parameter["e_max"]
        self.tr_power = parameter["tr_power"]
        self.g = parameter["g"]  # channel gain
        self.I = parameter["I"]  # Noise power
        self.W = parameter["W"]
    def calTime(self,data_size,computing_circle,energy):
        # dot_trDelay = self.e_max / self.tr_power
        # tr_delay = dot_trDelay / 2 + (
        #             np.square(dot_trDelay) * self.I * np.log(2) * (1 + (self.g * energy) / (self.I * dot_trDelay))) / (
        #                        2 * self.g * energy) \
        #            * (dot_trDelay * np.log2(1 + (self.g * energy) / (self.I * dot_trDelay)) - data_size / self.W)
        # cs_delay = computing_circle/self.f_cs
        # cs_time = tr_delay+cs_delay+self.tr_rtt
        # return cs_time
        #此处直接返回固定值
        if energy == parameter["energies"][1][0]:
            tr_delay = 0
        elif energy == parameter["energies"][1][1]:
            tr_delay = 20
        return 100+tr_delay

if __name__ == '__main__':
    pass