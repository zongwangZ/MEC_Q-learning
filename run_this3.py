# -*- coding: utf-8 -*-
'''
@project:q_learning
@author:zongwangz
@time:19-5-21 下午9:57
@email:zongwang.zhang@outlook.com
保存一些工具函数
'''

from maze_env import Maze
from RL_brain import QLearningTable
import matplotlib.pyplot as plt
import numpy as np
import copy
import ast
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(suppress=True)
from global_variables import *
import sys
import pandas as pd
from task import *
dir = "./data/record" ##存放数据的根目录

def update(flag=False):
    clearData(flag)
    for episode in range(0,100000):
        if (episode+1)%10000 == 0:
            output(RL.q_table,episode+1)
        observation = env.reset()
        while True:
            # action = RL.choose_action(str(observation),0.1)
            action = RL.choose_action_right(str(observation))
            observation_, reward, done = env.step(action)
            RL.learn(str(observation), action, reward, str(observation_))

            record(str(observation),action,reward,str(observation_),done,RL.q_table,int(int(episode/10000+1)*10000))

            observation = copy.deepcopy(observation_)
            if done:
                break

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
                max_action = RL.choose_action_real(state) ##这个地方导致误判
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
        if policy_class != 2:
            return -1
    elif es_intensity > 6:
        if energy_rank != 1 or policy_class != 1:
            return -1
    return 1

def printState(episode):
    cnt = 0 #表示现在是第几步
    result = {}
    filename = dir+"/"+str(episode)+"/logFile"+str(episode)
    file = open(filename,"r")
    while True:
        line = file.readline()
        cnt+=1
        if line:
            log_list = [ast.literal_eval(item) for item in line.split("|")]
            # log_list = map(lambda x: ast.literal_eval(x),line.split("|")) #这句还要检查一下
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

def calTime(filename):
    """
    使用Q表来计算完成所有任务消耗的时间
    :param filename:
    :return:
    """
    task = createTask()
    env = Maze(task)
    RL = QLearningTable(actions=list(range(env.n_actions)),filename=filename)
    Time = []
    for i in range(10000):
        observation = env.reset()
        while True:
            action = RL.choose_action_real(str(observation))
            observation_, reward, done = env.step(action)
            observation = observation_
            if done:
                time = findmax(task)
                Time.append(time)
                break
    # print(np.mean(Time))
    return np.mean(Time)

def view(filelist):
    '''
    对多个logfile进行输出内容
    :param filelist:
    :return:
    '''

    result = {}
    count = {}
    actionChoose = {}
    cnt = 0 ##记步数
    for filename in filelist:
        file = open(filename, "r")
        while True:
            line = file.readline()
            cnt += 1
            if line:
                log_list = [ast.literal_eval(item) for item in line.split("|")]
                for i in range(len(log_list)):
                    s, a, Q_sa, r, maxQ, maxAction, optQ, optAction, s_ = log_list[i]
                    if s not in result:
                        result[s] = []
                        result[s].append([cnt, maxQ, optQ,a])
                    else:
                        result[s].append([cnt, maxQ, optQ,a])
                    if s not in count:
                        count[s] = [0,0]
                        count[s][0] += 1
                        if check(s,a) == 1:
                            count[s][1] += 1
                    else:
                        count[s][0] += 1
                        if check(s, a) == 1:
                            count[s][1] += 1
                    if s not in actionChoose:
                        actionChoose[s] = []
                        if a == maxAction:
                            actionChoose[s].append([cnt,a])
                    else:
                        if a == maxAction:
                            actionChoose[s].append([cnt,a])
            else:
                break
    print(count)

    #plot
    for key in result:
        x = []
        y1 = [] #max
        y2 = [] #opt

        x_a = []
        a = []
        for item in result[key]:
            x.append(item[0])
            y1.append(item[1])
            y2.append(item[2])

        for item in actionChoose[key]:
            x_a.append(item[0])
            a.append(item[1])
        fig,ax1 = plt.subplots()
        ax2 = ax1.twinx()
        plt.title(key)
        ax1.plot(x,y1,label="max")
        ax1.plot(x,y2,label="opt")
        ax2.scatter(x_a,a,label="action",s=4)

        plt.legend()
        plt.savefig("./"+key+".png")
        # plt.show()
        plt.close()
        print(x,y1,y2)

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

def update1(number,flag=False):
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
                print(int(episode/cnt),len(right_trajectory))
        else:
            observation = env.reset()
            while True:
                action = RL.choose_action(str(observation),0.1)
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
def printConvergedState(filename):
    '''
    根据Q表输出收敛状态和未收敛状态
    :param filename Q表的文件名
    :return:
    '''
    result = {}
    dataframe = pd.read_csv(filename, index_col=0)
    dataframe.columns = list(range(0, parameter["taskNum"]* 6))
    for state in dataframe.index:
        if state not in result:
            if int(state.split(".")[0][1:]) != 7 and int(state.split(".")[0][1:]) != -1:
                result[state] = 1
                max_action = maxAction(dataframe,state)
                result[state] = check(state,max_action)
    print(result)
    sum = 0
    wrong = 0
    for key in result:
        sum += 1
        if result[key] == -1:
            wrong+=1
    return wrong,sum

def maxAction(dataframe,observation):
    task_done = list(bin(int(observation.split(".")[0][1:]))[2:])
    task_done.reverse()
    state_action = dataframe.loc[observation, :]
    action_list = copy.deepcopy(state_action)
    for i in range(parameter["taskNum"]):
        if i + 1 <= len(task_done) and task_done[i] == "1":
            for j in range(i * 6, (i + 1) * 6):
                action_list[j] = -np.inf
    action = np.random.choice(action_list[action_list == np.max(action_list)].index)
    return action


def printLog():
    '''
    根据1000万次的实验log，输出状态变化和收敛情况。
    :return:
    '''
    filename = "/home/zongwangz/PycharmProjects/q_learning/data/record/10million/log.txt"
    f = open(filename,"r")
    c = 0
    x = []
    y = []
    x_time = []
    y_time = []
    while True:
        line = f.readline()
        if line:
            item = ast.literal_eval(line)
            if isinstance(item,dict):
                c += 1
                result = item
                right = 0
                for key in result:
                    if result[key] == 1:
                        right += 1
                x.append(c)
                y.append(right)
        else:
            break
    print(x,y)
    max = 0
    for i in range(len(y)):
        if y[i]>max:
            max = y[i]
            x_time.append(i + 1)
            filename = "/home/zongwangz/PycharmProjects/q_learning/data/record/10million/"+"/Q_learning Table" + str((i + 1) * 10000)
            print(i + 1, y[i])
            y_time.append(calTime(filename))
    print(x_time,y_time)
    fig,ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(x,y,label="state")
    ax2.scatter(x_time,y_time,label="time")
    plt.show()


def train(env,RL,times=100000):
    for episode in range(0, times):
        observation = env.reset()
        while True:
            action = RL.choose_action(str(observation))
            observation_, reward, done = env.step(action)
            RL.learn(str(observation), action, reward, str(observation_))
            observation = copy.deepcopy(observation_)
            if done:
                break
if __name__ == '__main__':
    task_num = [8, ]
    for taskNum in task_num:
        parameter["taskNum"] = taskNum
        from task import *
        task = createTask()

        # Q-learning
        env = Maze(task)
        RL = QLearningTable(actions=list(range(env.n_actions)))
        train(env,RL)
        RL.q_table.to_csv("Q_learning Table" + str(taskNum) + ".csv")
    # print(calTime("/home/zongwangz/PycharmProjects/q_learning/data/record/30million/Q_learning Table1000000"))
    # print(printConvergedState("/home/zongwangz/PycharmProjects/q_learning/data/record/old/110000/Q_learning Table110000"))
    # printLog()
    # x = [250,500,1000,2000,5000]
    # y = [14,14,9,10,9]
    # plt.subplots()
    # plt.plot(x,y,"-.")
    # plt.xticks([250,500,1000,2000,5000])
    # plt.show()
