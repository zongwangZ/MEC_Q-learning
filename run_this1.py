# -*- coding: utf-8 -*-
'''
@project:Edge Computing
@author:zongwangz
@time:19-5-14 上午9:03
@email:zongwang.zhang@outlook.com
'''

from maze_env import Maze
from RL_brain import QLearningTable
import matplotlib.pyplot as plt
import numpy as np
import copy
import ast
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(suppress=True, threshold=np.nan)
from global_variables import *
import sys
import pandas as pd
def update(filename):
    c1 = 0
    c2 = 0
    OPT = []
    MAX = []
    right = []
    chosen = []
    for episode in range(100000):
        observation = env.reset()
        while True:
            action = RL.choose_action(str(observation))
            # print(episode,RL.q_table.loc["[   0. 4500.    8.]", 0])
            observation_, reward, done = env.step(action)
            RL.learn(str(observation), action, reward, str(observation_))

            if str(observation) == "[   0. 4500.    8.]":
                c1+=1
                chosen.append([episode,action])
                if action == 0:
                    c2+=1
                    right.append(episode)

            observation = copy.deepcopy(observation_)
            if done:

                opt = RL.q_table.loc["[   0. 4500.    8.]", 0]
                action_max = RL.choose_action_real("[   0. 4500.    8.]")
                max = RL.q_table.loc["[   0. 4500.    8.]", action_max]
                OPT.append(opt)
                MAX.append(max)
                break
    print(c1)
    print(c2)
    np.savetxt("./OPT",OPT)
    np.savetxt("./MAX",MAX)
    np.savetxt("./right",right)
    np.savetxt("./chosen", chosen)
    plt.subplots()
    plt.plot(range(100000),OPT,label="optimal")
    plt.plot(range(100000),MAX,label="maximum")
    for i in right:
        plt.scatter(i,OPT[i],color="red",marker=".")
        plt.scatter(i, MAX[i], color="red",marker=".")
    plt.legend()
    plt.show()
    plt.close()

def update1(filename):
    OPT = []
    MAX = []
    for episode in range(100000):
        observation = env.reset()
        while True:
            action = RL.choose_action(str(observation))
            observation_, reward, done = env.step(action)
            RL.learn(str(observation), action, reward, str(observation_))
            if str(observation) == "[   0. 4500.    8.]":
                if action == RL.choose_action_real("[   0. 4500.    8.]"):
                    action_max = RL.choose_action_real("[   0. 4500.    8.]")
                    max = RL.q_table.loc["[   0. 4500.    8.]", action_max]
                    MAX.append(max)
                if action == 0:
                    opt = RL.q_table.loc["[   0. 4500.    8.]", 0]
                    OPT.append(opt)
            observation = copy.deepcopy(observation_)
            if done:
                break
    np.savetxt("./OPT",OPT)
    np.savetxt("./MAX",MAX)
    plt.subplots()
    plt.plot(range(100000),OPT,label="optimal")
    plt.plot(range(100000),MAX,label="maximum")
    plt.legend()
    plt.show()
    plt.close()

def plotTrend():
    OPT = np.loadtxt("./OPT")
    MAX = np.loadtxt("./MAX")
    plt.subplots()
    plt.plot(range(len(OPT)), OPT, label="optimal",color = "black",linewidth=4.0)
    plt.plot(range(len(OPT)), MAX[:len(OPT)], label="maximum")
    plt.legend()
    plt.show()
    plt.close()

if __name__ == "__main__":
    task_num = [3, ]
    for taskNum in task_num:
        parameter["taskNum"] = taskNum
        from task import *
        task = createTask()

        # Q-learning
        env = Maze(task)
        RL = QLearningTable(actions=list(range(env.n_actions)))
        # RL.check_state_exist("[   0. 4500.    8.]")
        update1("./Reward" + str(taskNum) + "taskNum")
        RL.q_table.to_csv("Q_learning Table" + str(taskNum) + "taskNum.csv")


