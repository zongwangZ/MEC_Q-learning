# -*- coding: utf-8 -*-
'''
@project:Edge Computing
@author:zongwangz
@time:19-4-29 上午8:39
@email:zongwang.zhang@outlook.com
'''
'''
task graph：
dependency
task data size
task required CUP circles
'''
import networkx #create task graph
from global_variables import *
import numpy as np
from matplotlib import pyplot as plt
from CMP import *
import random
import os
import copy
def createTask():
    '''
    生成任务，注释部分是随机生成，为了保证整个实验前后一致，我们生成了任务依赖图以后，将其保存为文件，之后从文件中读取，
    :return:
    '''
    taskNum = parameter['taskNum']
    data_size = parameter['data_size']
    computing_circle = parameter['computing_circle']
    task = networkx.DiGraph()
    task.add_node(0, data_size=0, computing_circle=0)
    for i in range(taskNum):
        # t_data_size = (100+np.random.randint(0,5))/100*data_size
        # t_computing_circle = (1000+np.random.randint(0,5))/1000*computing_circle
        t_data_size = data_size
        t_computing_circle = computing_circle
        task.add_node(i+1, data_size=t_data_size,computing_circle=t_computing_circle)

    '''
    #随机生成task graph
    nodes = [i+1 for i in range(taskNum)]
    for node in nodes:
        if node == 1:
            pre_link = 1
            task.add_weighted_edges_from([(0,1,0)])
            succ_link = random.choice([1,1])
            for i in range(succ_link):
                succ_nodes = nodes[node:]
                for j in task.succ[node]:
                    succ_nodes.remove(j)
                succ_node = random.choice(succ_nodes)
                task.add_weighted_edges_from([(node, succ_node, 0)])
            continue

        pre_link = random.choice([1,1])
        if pre_link > node-1:
            pre_link = node-1
        for i in range(pre_link):
            #找出可选的前置任务
            pre_nodes = nodes[:node-1]
            for j in task.pred[node]:
                pre_nodes.remove(j)
            if len(pre_nodes) == 0:
                ##说明此时前面的操作 导致 当前节点的入度已经设置完成
                break
            pre_node = random.choice(pre_nodes)
            task.add_weighted_edges_from([(pre_node,node,0)])

        if pre_link == 0:
            succ_link = random.choice([1,1,1])
        else:
            succ_link = random.choice([1,1,1])
        if taskNum-node < succ_link:
            succ_link = taskNum-node
        for i in range(succ_link):
            succ_nodes = nodes[node:]
            for j in task.succ[node]:
                succ_nodes.remove(j)
            succ_node = random.choice(succ_nodes)
            task.add_weighted_edges_from([(node,succ_node,0)])
    '''

    # 从文件中读取
    if os.path.exists('./data/task_graph/'+str(taskNum)):
        edgeset = np.loadtxt('./data/task_graph/'+str(taskNum))
        edgeset = edgeset.astype(int)
        for edge in edgeset:
            task.add_weighted_edges_from([tuple(edge)])

    # networkx.draw_spring(task, with_labels=True)
    # plt.show()
    # plt.savefig("task_graph"+str(parameter["taskNum"]))
    return task

# def findmax(task):
#     '''
#     将任务依赖图对应为AOE网络，用CPM来寻找最长链（时间最长）
#     :param task:
#     :return:
#     '''
#     Node = []
#     Edge = []
#     assert isinstance(task, networkx.DiGraph)
#     nodes = task.node
#     for node in nodes:
#         adj_node_dict = task[node]
#         for adj_node in adj_node_dict:
#             if adj_node > node:
#                 duration = task.get_edge_data(node, adj_node)['weight']
#                 Node.append((adj_node,duration))
#                 if node != 0:
#                     Edge.append((node,adj_node))
#     # 构建graph
#     G = CPM()
#     for item in Node:
#         G.add_node(item[0], duration=item[1])
#
#     G.add_edges_from(Edge)
#     # nx.draw_spring(G,with_labels=True)
#     # plt.title('AOE网络')
#     # plt.axis('on')
#     # plt.xticks([])
#     # plt.yticks([])
#     # plt.show()
#     # print('关键活动为:')
#     # print(G.critical_path_length, G.critical_path)
#     return G.critical_path_length

def findmax(task):
    maxtime = 0
    path = []
    root = 0
    path.append(root)
    for node in task.succ[path[-1]]:
        step(copy.copy(path),node,maxtime)
    return maxtime


def step(path,endNode,maxtime):
    path.append(endNode)
    if task.succ[endNode] == {}:
        #路径结束,计算时间
        time = 0
        for i in range(len(path)-1):
            time+=task.get_edge_data(path[i],path[i+1])['weight']
        if time > maxtime:
            maxtime = time
    else:
        for node in task.succ[endNode]:
            step(copy.copy(path),node,maxtime)


def resetTask(task):
    assert isinstance(task,networkx.DiGraph)
    nodes = task.node
    for node in nodes:
        adj_node_dict = task[node]
        for adj_node in adj_node_dict:
            task.get_edge_data(node,adj_node)['weight'] = 0

def add_edge_time(task,node,time):
    assert  isinstance(task,networkx.DiGraph)
    for adj_node in task.pred[node]:
        task.add_weighted_edges_from([(adj_node,node,time)])
if __name__ == '__main__':
    parameter["taskNum"] = 8
    task = createTask()
    resetTask(task)
    findmax(task)
    # print(task.pred[10])
    networkx.draw_spring(task, with_labels=True)
    plt.show()
