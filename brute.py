# -*- coding: utf-8 -*-
'''
@project:Edge Computing
@author:zongwangz
@time:19-5-4 上午7:45
@email:zongwang.zhang@outlook.com
暴力求解法：穷举每条边的可能权重，将多条边权重组合起来，选取最长时间作为结果
注意
1.每当做完所有任务，也就是递归到最深处，所有边都附上权重时，验证限制条件，不满足则结束返回，相当于丢弃本次结果
2.在做暴力求解前为任务附加上服务器上任务数量。如果在运行时随机生成时，则会影响遇到服务器任务数量的概率，因为我
们是从多个结果中选出最小的那个结果
'''
from global_variables import *
from task import *
import copy
minTime = np.inf #用来记录最短时间，也就是最终结果
import scipy.stats as st
def brute_force(task):
    """
    暴力求解法，采用递归
    :param task:
    :return:
    """
    Energy = parameter["energe"]
    assert isinstance(task,networkx.DiGraph)
    taskNum = parameter["taskNum"]
    task_done = [0 for i in range(taskNum)] #任务完成序列
    global minTime
    minTime = np.inf
    #将每个任务绑定服务器上任务数量值
    task_intensity = []
    for i in range(taskNum):
        task_intensity.append(chooseIntensity())
    step(copy.copy(task_done),task,Energy,task_intensity) #采用递归
    return minTime

def chooseIntensity():
    """
    按照泊松强度生成服务器任务数量
    :return:
    """
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
    print(p)
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
    # print(randomD)
    return chosen

def step(task_done,task,Energy,task_intensity):
    #当能量不足时，这条路断了
    if Energy < parameter["total_power"] * (1 - parameter["power_percentage"]) or Energy < 0:
        return -1
    #当任务满足时记录时间
    if all(task_done):
        global minTime
        Time = findmax(task)
        if minTime > Time:
            minTime = Time
            print(minTime)
        return 1
    serial_number = -1
    assert isinstance(task, networkx.DiGraph)
    for i in range(len(task_done)):
        if task_done[i] == 0:
            ##此时处理这个任务
            serial_number = i+1
            break
    ways = [1, 2, 3]
    energies = parameter["energies"]
    for way in ways:
        if way == 1:
            for energy in energies[0]:
                time = device.calTime(energy,task.node[serial_number]["computing_circle"])
                for adj_node in task.pred[serial_number]:
                    if adj_node < serial_number:
                        task.add_weighted_edges_from([(adj_node, serial_number, time)])
                copy_task_done = copy.copy(task_done)
                copy_task_done[i] = 1
                flag = step(copy_task_done,task,Energy-energy,task_intensity)
                if flag == -1:
                    #说明这条路不通，马上切换下一条路
                    continue
        elif way == 2:
            for energy in energies[1]:
                time = edgeServer.calTime(task.node[serial_number]["data_size"],energy,task_intensity[serial_number-1])
                for adj_node in task.pred[serial_number]:
                    if adj_node < serial_number:
                        task.add_weighted_edges_from([(adj_node, serial_number, time)])
                copy_task_done = copy.copy(task_done)
                copy_task_done[i] = 1
                flag = step(copy_task_done, task, Energy - energy,task_intensity)
                if flag == -1:
                    # 说明这条路不通，马上切换下一条路
                    continue
        elif way == 3:
            for energy in energies[1]:
                time = cloudServer.calTime(task.node[serial_number]["data_size"],task.node[serial_number]["computing_circle"],energy)
                for adj_node in task.pred[serial_number]:
                    if adj_node < serial_number:
                        task.add_weighted_edges_from([(adj_node, serial_number, time)])
                copy_task_done = copy.copy(task_done)
                copy_task_done[i] = 1
                flag = step(copy_task_done, task, Energy - energy,task_intensity)
                if flag == -1:
                    # 说明这条路不通，马上切换下一条路
                    continue
    return 0
def doSim():
    parameter["taskNum"] = 8
    task = createTask()
    minTime = brute_force(task)
    print(minTime)
if __name__ == '__main__':
    parameter["taskNum"] = 8
    task = createTask()
    bruteTime = []
    Time2 = []
    for i in range(100):
        resetTask(task)
        Time2.append(brute_force(task))
    bruteTime.append(np.mean(Time2))
    print(bruteTime)