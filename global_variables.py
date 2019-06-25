# -*- coding: utf-8 -*-
'''
@project:Edge Computing
@author:zongwangz
@time:19-4-29 上午8:38
@email:zongwang.zhang@outlook.com
我们使用一个dict描述所有要使用的变量，但是在实验中，我们对参数做了比较多的简化，保存了关键部分。
'''
parameter={
    "energe":4500, #剩余能量
    "taskNum":3, #任务数量
    "data_size":5,
    "computing_circle":6,
    "esc":15000, #the effective switched capacitiance
    "fmax_cpu":0.1, #the maximum CPU-cycle frequency of the device(0.06)
    "tr_es":10,#wired transmission time for RTT to the edge
    "f_es":11,#service rate of edge server
    "e_max":0.04, #the maximum allocated energy
    "tr_power":2, #the maximum transmit power of the mobile device
    "g":8,#Channel gain
    "I":1.5e-8, #Noise power
    "W":3,#Wireless bandwidth
    "f_cs":3,#Service rate of cloud server
    "tr_cs":100,#wired transmission time for RTT to the cloud
    "maxReward":4000,
    "total_power":10000,
    "power_percentage":0.75,
    "tr_delay":1,
    "taskNum_es":[4,6,8,10],
    "intensity":6,
    "energies":[[400,200],[200,100]]
}
from device import *
from edgeServer import *
from cloudServer import *
device = device()
edgeServer = edgeServer()
cloudServer = cloudServer()