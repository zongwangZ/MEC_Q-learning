# -*- coding: utf-8 -*-
'''
@project:Edge Computing
@author:zongwangz
@time:19-4-29 上午9:13
@email:zongwang.zhang@outlook.com
随机选取：随机分配能量和任务处理方法
注意能量限制
'''
import numpy as np
from global_variables import *
from task import *
import scipy.stats as st
def randomChooseWay():
    ways = [1,2,3]
    way = np.random.choice(ways)
    return way
def randomChooseEnergy(way):
    Energy = parameter["energies"]
    if way == 1:
        energy = np.random.choice(Energy[0])
    else:
        energy = np.random.choice(Energy[1])
    return energy

def chooseIntensity():
    taskNum_es = parameter["taskNum_es"]
    assert isinstance(taskNum_es, list)
    intensity = parameter["intensity"]
    p = []
    for num in taskNum_es:
        if taskNum_es.index(num) == 0:
            probability = st.poisson.cdf(num, intensity)
        elif taskNum_es.index(num) == len(taskNum_es) - 1:
            probability = 1 - st.poisson.cdf(num, intensity)
        else:
            probability = st.poisson.pmf(num, intensity)
        p.append(probability)
    p = list(np.array(p) * 1 / sum(p))
    for i in range(len(p) - 1):
        p[i + 1] = p[i + 1] + p[i]
    # print(p)
    randomD = np.random.uniform()
    chosen = -1
    for i in range(len(p) - 1):
        if i == 0 and randomD <= p[0] and randomD >= 0:
            chosen = 0
            break
        elif randomD > p[i] and randomD <= p[i + 1]:
            chosen = i + 1
            break
    chosen = taskNum_es[chosen]
    return chosen

def doRandom(task):
    assert isinstance(task,networkx.DiGraph)
    taskNum = parameter["taskNum"]
    Nodes = [i+1 for i in range(taskNum)]
    Energy = parameter["energe"]
    Ways = []
    for i in range(taskNum):
        Ways.append(randomChooseWay())
    Energies = []
    while True:
        if len(Energies) == taskNum:
            break
        if Energy-sum(Energies) < parameter["total_power"] * (1 - parameter["power_percentage"]) or sum(Energies) > Energy:
            Energies = []
        else:
            Energies.append(randomChooseEnergy(Ways[len(Energies)]))
    for node in Nodes:
        way = Ways[node-1]
        energy = Energies[node-1]
        if way == 1:
            time = device.calTime(energy,task.node[node]["computing_circle"])
        elif way == 2:
            time = edgeServer.calTime(task.node[node]["data_size"],energy,chooseIntensity())
        elif way == 3:
            time = cloudServer.calTime(task.node[node]["data_size"],task.node[node]["computing_circle"],energy)
        for adj_node in task.pred[node]:
            if adj_node < node:
                task.add_weighted_edges_from([(adj_node,node,time)])
    return findmax(task)

def doSim():
    Time = []
    task = createTask()
    for i in range(100):
        resetTask(task)
        time = doRandom(task)
        Time.append(time)
    plt.subplots()
    plt.plot(range(len(Time)),Time)
    plt.show()

if __name__ == '__main__':
    doSim()