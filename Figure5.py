# -*- coding: utf-8 -*-
'''
@project:q_learning
@author:zongwangz
@time:19-6-20 下午8:58
@email:zongwang.zhang@outlook.com
在训练中加入正确的数据训练
'''
from maze_env import Maze
from RL_brain import QLearningTable
import random
from global_variables import *
import copy
np.set_printoptions(suppress=True)
import matplotlib.pyplot as plt
import pandas as pd
import os
import ast
dir = "./data/record" ##存放数据的根目录
def clearData(flag=False):
    if not flag:
        return
def record(s,a,r,s_,done,qtable,episode):
    '''
    传过来的变量不要更改
    在Q表更新后记录的
    :param s:
    :param a:
    :param r:
    :param s_:
    :param qtable:
    :return:
    '''
    assert isinstance(qtable,pd.DataFrame)
    data_dir = dir+"/"+str(episode)
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    Q_sa = qtable.loc[s,a]
    maxAction = RL.choose_action_real(s)
    maxQ = qtable.loc[s,maxAction]
    optAction = optimal_action(s)
    optQ = qtable.loc[s,optAction]

    record = [s,a,Q_sa,r,maxQ,maxAction,optQ,optAction,s_]
    filename = data_dir+"/logFile"+str(episode)
    if not done:
        open(filename,"a+").write(str(record)+"|")
    else:
        open(filename,"a+").write(str(record)+"\n")


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

def output(dataframe,episode):
    assert isinstance(dataframe,pd.DataFrame)
    #保存Q表
    dataframe.to_csv(dir+"/"+str(episode)+"/Q_learning Table"+str(episode))
    #输出Q表收敛状况
    printQTable(dataframe,episode)
    #输出现有状态的情况
    printState(episode)


def printQTable(dataframe,episode):
    result = {}
    for state in dataframe.index:
        if state not in result:
            if int(state.split(".")[0][1:]) != 7 and int(state.split(".")[0][1:]) != -1:
                result[state] = 1
                max_action = RL.choose_action_real(state)
                result[state] = check(state, max_action)
    print(result)
    t1 = []
    t2 = []
    for item in result:
        t1.append(item)
        t2.append(result[item])
    fig, ax1 = plt.subplots()
    plt.plot(t1, t2, ".")
    for xtick in ax1.get_xticklabels():
        xtick.set_rotation(50)
    plt.title("QTable"+str(episode))
    plt.savefig(dir + "/" + str(episode) + "/" + "QTable" + str(episode) + ".png")
    plt.show()
    plt.close()

def check(state, action):
    es_intensity = int(state.split(".")[2])
    serial_number = int(action / 6) + 1
    policy_class = int((action - (serial_number - 1) * 6) / 2) + 1  # 位置(1,2,3)
    energy_rank = (action - (serial_number - 1) * 6) % 2 + 1  # 四个能量级(1,2)
    if es_intensity <= 6:
        if policy_class != 2 or energy_rank != 1:
            #边缘服务器工作 且传输使用更多能量
            return -1
    elif es_intensity > 6:
        #在本地做且使用更多能量
        if energy_rank != 1 or policy_class != 1:
            return -1
    return 1

def printState(episode):
    '''
    输出每个state最大Q和最优Q的变化
    :param episode:
    :return:
    '''
    cnt = 0 #表示现在是第几步
    result = {}
    filename = dir+"/"+str(episode)+"/logFile"+str(episode)
    file = open(filename,"r")
    while True:
        line = file.readline()
        cnt+=1
        if line:
            log_list = [ast.literal_eval(item) for item in line.split("|")]
            for i in range(len(log_list)):
                s, a, Q_sa, r, maxQ, maxAction, optQ, optAction, s_ = log_list[i]
                if s not in result:
                    result[s] = []
                    result[s].append([cnt, maxQ, optQ])
                else:
                    result[s].append([cnt,maxQ,optQ])
        else:
            break
    #plot
    for key in result:
        x = []
        y1 = [] #max
        y2 = [] #opt
        for item in result[key]:
            x.append(item[0])
            y1.append(item[1])
            y2.append(item[2])
        plt.subplots()
        plt.title(key+" "+str(episode))
        plt.plot(x,y1,label="max")
        plt.plot(x,y2,label="opt")
        plt.legend()
        plt.savefig(dir+"/"+str(episode)+"/"+key+" "+str(episode)+".png")
        # plt.show()
        plt.close()

def genTrajectory(number):
    '''
    产生3个任务的轨迹，为一个正确选择的序列[（s, a, r, s_）,...]
    递归来做吧
    :param number:
    :return:
    '''
    def step(state,c,trajectory,traces,sequency):
        if sequency != []:
            sequency.append(str(state))
            trajectory.append(sequency)

        if state[0] == 7:
            traces.append(trajectory)
            trajectory = []
            return
        sequency = []
        sequency.append(str(state))
        policy_class = 0
        energy_rank = 0
        if state[2] <= 6:
            policy_class = 2
            energy_rank = 1
        elif state[2] > 6:
            policy_class = 1
            energy_rank = 1
        if policy_class == 1 and energy_rank == 1:
            state[1] -= 400
            action = [0,6,12][c]
            reward = parameter["maxReward"] - device.calTime(400,parameter["computing_circle"])
        elif policy_class == 2 and energy_rank == 1:
            state[1] -= 200
            action = [2,8,14][c]
            reward = parameter["maxReward"] - edgeServer.calTime(parameter["data_size"],200,state[2])
        sequency.append(action)
        sequency.append(reward)
        state[0] += 2 ** c
        for state[2] in [4,6,8,10]:
            step(copy.copy(state),c+1,copy.copy(trajectory),traces,copy.copy(sequency))

    state = np.zeros(3)
    state[0] = 0
    state[1] = 4500
    traces = []
    trajectory = []
    sequency = []
    for state[2] in [4,6,8,10]:
        step(copy.copy(state),0,copy.copy(trajectory),traces,copy.copy(sequency))
    # for item in traces:
    #     print(item)
    result = []
    for i in range(number):
        result.extend(traces)
    random.shuffle(result)
    return result

def update1(env,RL,number,flag=False):
    clearData(flag)
    right_trajectory = genTrajectory(number) ##正确的训练数据
    cnt = int(100000/len(right_trajectory))
    for episode in range(0,100000):
        if (episode+1)%10000 == 0:
            output(RL.q_table,episode+1)
        if (episode+1)%cnt == 0:
            if int(episode/cnt) < len(right_trajectory):
                trainWithTrajectory(right_trajectory[int(episode/cnt)],episode)
            else:
                trainWithTrajectory(right_trajectory[int(episode / cnt)%len(right_trajectory)], episode)
        else:
            observation = env.reset()
            while True:
                action = RL.choose_action(str(observation))
                observation_, reward, done = env.step(action)
                RL.learn(str(observation), action, reward, str(observation_))
                record(str(observation), action, reward, str(observation_), done, RL.q_table,
                       int(int(episode / 10000 + 1) * 10000))
                observation = copy.deepcopy(observation_)
                if done:
                    break

def trainWithTrajectory(trajectory,episode):
    for item in trajectory:
        observation, action, reward, observation_ = item
        RL.learn(observation,action,reward,observation)
        record(observation, action,reward, observation_, True, RL.q_table, int(int(episode / 10000 + 1) * 10000))

if __name__ == '__main__':
    task_num = [3, ]
    for taskNum in task_num:
        parameter["taskNum"] = taskNum
        from task import *

        task = createTask()

        # Q-learning
        env = Maze(task)
        RL = QLearningTable(actions=list(range(env.n_actions)))
        update1(env, RL, 5)
        RL.q_table.to_csv("Q_learning Table" + str(taskNum) + "_Insert")