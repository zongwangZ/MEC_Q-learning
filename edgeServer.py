# -*- coding: utf-8 -*-
'''
@project:Edge Computing
@author:zongwangz
@time:19-4-29 下午3:26
@email:zongwang.zhang@outlook.com
需要说明的是：
我们对部分值做了简化
'''
import numpy as np
from global_variables import *

class edgeServer:
    def __init__(self):
        self.tr_rtt = parameter["tr_es"]
        self.f_es = parameter["f_es"]
        self.e_max = parameter["e_max"]
        self.tr_power = parameter["tr_power"]
        self.g = parameter["g"] #channel gain
        self.I = parameter["I"] #Noise power
        self.W = parameter["W"]
    def calTime(self,data_size,energy,es_intensity):
        '''

        :param data_size: 当前任务大小
        :param energy:  当前任务分配的能量
        :param es_intensity: 当前阶段边缘服务器的泊松强度
        :return:
        '''
        # dot_trDelay = self.e_max/self.tr_power
        # tr_delay = dot_trDelay/2 + (np.square(dot_trDelay)*self.I*np.log(2)*(1+(self.g*energy)/(self.I*dot_trDelay)))/(2*self.g* energy)\
        #            *(dot_trDelay*np.log2(1+(self.g*energy)/(self.I*dot_trDelay))-data_size/self.W)
        # es_delay = 1/(self.f_es-es_intensity) + 1/self.f_es
        # es_time = tr_delay + es_delay + self.tr_rtt
        # return es_time
        #这里我们做了简化，突出服务器任务数量对处理时间影响程度
        if es_intensity < 8:
            return 5
        if es_intensity >= 8 :
            return 500

if __name__ == '__main__':
    edgeServer = edgeServer()
    print(edgeServer.calTime(5,400,8))