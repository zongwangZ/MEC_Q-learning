'''
我们参考了莫烦的代码，
https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/2_Q_Learning_maze
'''
import numpy as np
import pandas as pd
import copy
from global_variables import *
import os
import random
from tool import *
# pd.set_option('precision', 7)
class QLearningTable:
    # 初始化
    def __init__(self, actions, filename="",learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions  # a list
        self.lr = learning_rate  # 学习率
        self.gamma = reward_decay  # 奖励衰减
        self.epsilon = e_greedy  # 贪婪度
        self.taskNum = parameter["taskNum"]
        #如果指定的文件不为空，那么从指定文件中读取Q表
        if filename != "":
            self.q_table = pd.read_csv(filename,index_col=0)
            self.q_table.columns = list(range(0,self.taskNum*6))
        else:
            #如果根目录下存在Q表则则读取
            if os.path.exists("./Q_learning Table"+str(self.taskNum)+".csv"):
                self.q_table = pd.read_csv("./Q_learning Table"+str(self.taskNum)+".csv",index_col=0)
                self.q_table.columns = list(range(0,self.taskNum*6))
            else:
                #创建新的Q表
                self.q_table = pd.DataFrame(columns=self.actions,dtype=np.float64)

    # 选行为
    def choose_action(self, observation):
        #取得任务队列
        task_done = list(bin(int(observation.split(".")[0][1:]))[2:])
        task_done.reverse()
        self.check_state_exist(observation)  # 检测本 state 是否在 q_table 中存在
        # 选择 action
        if np.random.uniform() < self.epsilon:  # 选择 Q value 最高的 action
            state_action = self.q_table.loc[observation, :]
            action_list = copy.deepcopy(state_action)
            for i in range(self.taskNum):
                if i+1 <= len(task_done) and task_done[i] == "1":
                    for j in range(i*6,(i+1)*6):
                        action_list[j] = -np.inf
            # 同一个 state, 可能会有多个相同的 Q action value, 所以我们乱序一下
            action = np.random.choice(action_list[action_list == np.max(action_list)].index)
        else:  # 随机选择 action
            ##这个地方加一个限制 只能选择未做的任务
            state_action = self.q_table.loc[observation, :]
            action_list = copy.deepcopy(state_action)
            for i in range(self.taskNum):
                if i + 1 <= len(task_done) and task_done[i] == "1":
                    for j in range(i * 6, (i + 1) * 6):
                        action_list[j] = -np.inf

            action = np.random.choice(action_list[action_list!=-np.inf].index)
        # print(action)
        return action


    def choose_action_real(self, observation):
        """
        只按贪婪策略来选，是用于在训练完Q表以后，计算平均时间
        :param observation:
        :return:
        """
        # 取得任务队列
        task_done = list(bin(int(observation.split(".")[0][1:]))[2:])
        task_done.reverse()
        self.check_state_exist(observation)  # 检测本 state 是否在 q_table 中存在
        # 选择 action
        state_action = self.q_table.loc[observation, :]
        action_list = copy.deepcopy(state_action)
        for i in range(self.taskNum):
            if i + 1 <= len(task_done) and task_done[i] == "1":
                for j in range(i * 6, (i + 1) * 6):
                    action_list[j] = -np.inf
        # 同一个 state, 可能会有多个相同的 Q action value, 所以我们乱序一下
        action = np.random.choice(action_list[action_list == np.max(action_list)].index)
        # print(action)
        return action

    def choose_action_right(self,observation):
        return optimal_action(observation)

    # 学习更新参数
    def learn(self, s, a, r, s_):
        """
        按照Q-learning更新公式对Q值进行更新
        :param s:
        :param a:
        :param r:
        :param s_:
        :return:
        """
        self.check_state_exist(s_)  # 检测 q_table 中是否存在 s_
        q_predict = self.q_table.loc[s, a]

        assert isinstance(s_,str)
        temp = copy.copy(s_)
        if int(temp.split(".")[0][1:]) != 2**self.taskNum-1:
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()  # 下个 state 不是 终止符
        else:#terminal
            q_target = r

        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)# 更新对应的 state-action 值


    # 检测 state 是否存在
    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )
        # print(self.q_table)



if __name__ == '__main__':
    RL = QLearningTable(actions=list(range(18)))
    RL.choose_action_test("[   0. 4500.    8.]")