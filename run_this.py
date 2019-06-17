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
    REWARDS = []
    for episode in range(10000):
        rewards = [] ##目前初始reward为0，后面可以定义为maxReward
        observation = env.reset()
        while True:
            action = RL.choose_action(str(observation))
            observation_, reward, done = env.step(action)
            RL.learn(str(observation), action, reward, str(observation_))
            rewards.append(reward) #保存本次的reward
            observation = copy.deepcopy(observation_)
            if done:
                break
        REWARDS.append(rewards)
        # REWARDS.append(np.mean(rewards))
    open(filename,"w").write(str(REWARDS))
    # np.savetxt(filename,np.array(REWARDS))

def plotTraing(filename):
    '''
    画出训练过程
    :return:
    '''
    REWARDS = ast.literal_eval(open(filename, "r").readlines()[0])
    reward = []
    for rewards in REWARDS:
        reward.append(rewards[-1])

    t = []
    for i in range(int(len(reward)/50)):
        t.append(np.mean(reward[i*50:(i+1)*50]))
    traing_step = range(len(t))
    plt.subplots()
    plt.plot(traing_step[0:100],t[0:100],".-")
    plt.xlabel("traing_steps")
    plt.ylabel("reward")
    plt.show()
    plt.close()



def plot3D(filename):
    '''
    效果一般般
    :param filename:
    :return:
    '''
    fig = plt.figure(figsize=(8, 6))
    axes3d = Axes3D(fig)
    REWARDS = ast.literal_eval(open(filename, "r").readlines()[0])
    for i in range(100000):
        z = [i]
        x = [i for i in range(len(REWARDS[i]))]
        y = REWARDS[i]
        axes3d.plot(x, y, zs=z, zdir='x',marker="o")
    plt.ylabel('phase')
    plt.xlabel('step')
    axes3d.set_zlabel('reward')

    # axes3d.set_ylim((0,10))
    plt.show()

def plotCompletion(filename):
    REWARDS = ast.literal_eval(open(filename, "r").readlines()[0])
    completion = []
    t = []
    for rewards in REWARDS:
        list.sort(rewards)
        if len(rewards) == parameter["taskNum"] and rewards[0] > -parameter["maxReward"]:
            completion.append(1)
        else:
            completion.append(0)
    for i in range(int(len(completion)/10)):
        t.append(np.mean(completion[i*10:(i+1)*10]))
    plt.subplots()
    plt.plot(range(len(t)), t, ".-")
    # plt.plot(range(100,110),[1,1,1,1,1,1,1,1,1,1],".-",color="red")
    plt.xlabel("#step(10)")
    plt.ylabel("#completion")
    plt.show()
    plt.close()
def reward():
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    update("./Reward")
    RL.q_table.to_csv("Q_learning Table")
    plotTraing("./Reward")

    rewards = []
    for i in range(100):
        observation = env.reset()
        while True:
            action = RL.choose_action_real(str(observation))
            observation_, reward, done = env.step(action)
            RL.learn(str(observation), action, reward, str(observation_))
            observation = observation_
            # 如果掉下地狱或者升上天堂, 这回合就结束了
            if done:
                rewards.append(reward)
                break
    print(rewards)
    open("./Test", "w").write(str(rewards))

    plotCompletion("./Reward")

def plot1():
    task_num = [3, 4, 5, 6, 7, 8]
    plt.subplots()
    plt.plot(task_num, [294.99540794870126, 304.8415458901125, 416.74637198087686, 486.95626385097717, 579.4240315960806, 691.6511181472915],linestyle="--", label="random choose")
    plt.plot(task_num, [187.17534634306597, 188.8838154275818, 251.67967243876575, 303.4673788495804, 356.355979465629, 422.94017724955097],linestyle="--", label="brute force")
    plt.plot(task_num, [219.17720795124572, 225.97073611249363, 298.52385281385284, 380.16892297595075, 431.6240666540665, 509.3337582741419], label="Q-learning")
    plt.xlabel("#task")
    plt.ylabel("comsumed time")
    plt.legend()
    plt.show()

#
# def dosim():
#     # randomTime = []
#     # bruteTime = []
#     QLearningTime = []
#     task_num = [6, ]
#     for taskNum in task_num:
#         parameter["taskNum"] = taskNum
#         # intensities = [4,6,8,10,12]
#         # for intensity in intensities:
#         #     parameter["intensity"] = intensity
#         from task import *
#         task = createTask()
#
#         # # random
#         # import randomChoose as rc
#         # Time1 = []
#         # for i in range(100):
#         #     resetTask(task)
#         #     time = rc.doRandom(task)
#         #     Time1.append(time)
#         # randomTime.append(np.mean(Time1))
#
#         # brute
#         # Time2 = []
#         # import brute
#         # for i in range(100):
#         #     resetTask(task)
#         #     Time2.append(brute.brute_force(task))
#         # bruteTime.append(np.mean(Time2))
#
#         # Q-learning
#         Time3 = []
#         env = Maze(task)
#         RL = QLearningTable(actions=list(range(env.n_actions)))
#         update("./Reward" + str(taskNum) + "taskNum")
#         RL.q_table.to_csv("Q_learning Table" + str(taskNum) + "taskNum.csv")
#         plotTraing("./Reward" + str(taskNum) + "taskNum")
#
#         rewards = []
#         for i in range(100):
#             observation = env.reset()
#             while True:
#                 action = RL.choose_action_real(str(observation))
#                 observation_, reward, done = env.step(action)
#                 RL.learn(str(observation), action, reward, str(observation_))
#                 observation = observation_
#                 # 如果掉下地狱或者升上天堂, 这回合就结束了
#                 if done:
#                     rewards.append(reward)
#                     break
#         print(rewards)
#         open("./Test" + str(taskNum) + "taskNum", "w").write(str(rewards))
#
#         plotCompletion("./Reward" + str(taskNum) + "taskNum")
#         for item in rewards:
#             Time3.append(parameter["maxReward"] - item)
#         QLearningTime.append(np.mean(Time3))
#
#     # print("randomTime",randomTime)
#     # print("bruteTime",bruteTime)
#     print("QLearningTime", QLearningTime)
#     # np.savetxt("randomTime", np.array(randomTime))
#     # np.savetxt("bruteTime", np.array(bruteTime))
#     np.savetxt("QLearningTime", np.array(QLearningTime))
#     plt.subplots()
#     # plt.plot(task_num, randomTime,label="random choose")
#     # plt.plot(task_num, bruteTime,label="brute force")
#     plt.plot(task_num, QLearningTime, label="Q-learning")
#     plt.xlabel("#task")
#     plt.ylabel("comsumed time")
#     plt.legend()
#     plt.savefig("curve1")
#     plt.show()


def Qtable_test():
    # from task import *
    # parameter["taskNum"] = 3
    # task = createTask()
    # env = Maze(task)
    # RL = QLearningTable(actions=list(range(env.n_actions)))
    # observations = []
    # for i in range(1000):
    #     observation = env.reset()
    #     observations = []
    #     while True:
    #         action = RL.choose_action_real(str(observation))
    #         observation_, reward, done = env.step(action)
    #         RL.learn(str(observation), action, reward, str(observation_))
    #         observations.append([str(observation), action])
    #         observation = observation_
    #         # 如果掉下地狱或者升上天堂, 这回合就结束了
    #         if done:
    #             observations.append([str(observation),action])
    #             open("./observations","a+").write(str(observations)+"\n")
    #             break
    c = 0
    dataframe = pd.read_csv("./Q_learning Table" + str(3) + "taskNum.csv", index_col=0)
    result = {}
    for state in dataframe.index:
        if state not in result:
            if int(state.split(".")[0][1:]) != 7:
                result[state] = [0,0]


    def check(state, action):
        result[state][1]+=1
        global c
        c += 1
        es_intensity = int(state.split(".")[2])
        serial_number = int(action / 6) + 1
        policy_class = int((action - (serial_number - 1) * 6) / 2) + 1  # 位置(1,2,3)
        energy_rank = (action - (serial_number - 1) * 6) % 2 + 1  # 四个能量级(1,2)
        if es_intensity <= 6:
            if policy_class != 2:
                result[state][0] += 1
                return
        elif es_intensity > 6:
            if energy_rank != 1 or policy_class != 1:
                result[state][0] += 1
                return


    lines = open("./observations", "r").readlines()
    for line in lines:
        stateaction = ast.literal_eval(line)
        state1 = stateaction[0][0]
        action1 = stateaction[0][1]
        state2 = stateaction[1][0]
        action2 = stateaction[1][1]
        state3 = stateaction[2][0]
        action3 = stateaction[2][1]
        check(state1, action1)
        check(state2, action2)
        check(state3, action3)
    print(result, c)

    states = []
    wronghit = []
    hit = []
    for item in result:
        states.append(item)
        wronghit.append(result[item][0] / 1000)
    for item in result:
        hit.append(result[item][1]/1000)
    fog, ax1 = plt.subplots()
    plt.plot(states, wronghit, marker=".")

    for i in range(len(hit)):
        if hit[i] == 0:
            plt.scatter(i,0,color="red")

    for xtick in ax1.get_xticklabels():
        xtick.set_rotation(50)
    plt.show()
#
# def Qtable_test1():
#     def check(state, action):
#         es_intensity = int(state.split(".")[2])
#         serial_number = int(action / 6) + 1
#         policy_class = int((action - (serial_number - 1) * 6) / 2) + 1  # 位置(1,2,3)
#         energy_rank = (action - (serial_number - 1) * 6) % 2 + 1  # 四个能量级(1,2)
#         if es_intensity <= 6:
#             if policy_class != 2:
#                 return -1
#         elif es_intensity > 6:
#             if energy_rank != 1 or policy_class != 1:
#                 return -1
#         return 1
#
#     result = {}
#     from task import *
#     parameter["taskNum"] = 3
#     task = createTask()
#     env = Maze(task)
#     RL = QLearningTable(actions=list(range(env.n_actions)))
#     dataframe = pd.read_csv("./Q_learning Table" + str(3) + "taskNum.csv", index_col=0)
#     dataframe.columns = list(range(0, 3 * 6))
#     for state in dataframe.index:
#         if state not in result:
#             if int(state.split(".")[0][1:]) != 7 and int(state.split(".")[0][1:]) != -1:
#                 result[state] = 1
#                 max_action = RL.choose_action_real(state)
#                 result[state] = check(state,max_action)
#     print(result)
#
#     t1 = []
#     t2 = []
#     for item in result:
#         t1.append(item)
#         t2.append(result[item])
#     fig,ax1 = plt.subplots()
#     plt.plot(t1,t2,".")
#     for xtick in ax1.get_xticklabels():
#         xtick.set_rotation(50)
#     plt.show()
#     plt.close()


def update1(filename):
    REWARDS = []
    for episode in range(10000):
        rewards = [] ##目前初始reward为0，后面可以定义为maxReward
        observation = env.reset()
        while True:
            action = RL.choose_action_test(str(observation))
            observation_, reward, done = env.step(action)
            RL.learn(str(observation), action, reward, str(observation_))
            rewards.append(reward) #保存本次的reward
            observation = copy.deepcopy(observation_)
            if done:
                break
        REWARDS.append(rewards)
    open(filename,"w").write(str(REWARDS))
if __name__ == "__main__":
    # task_num = [3, ]
    # for taskNum in task_num:
    #     parameter["taskNum"] = taskNum
    #     from task import *
    #
    #     task = createTask()
    #
    #     # Q-learning
    #     env = Maze(task)
    #     RL = QLearningTable(actions=list(range(env.n_actions)))
    #     update1("./Reward" + str(taskNum) + "taskNum")
    #     RL.q_table.to_csv("Q_learning Table" + str(taskNum) + "taskNum.csv")
    #
    # def check(state, action):
    #     es_intensity = int(state.split(".")[2])
    #     serial_number = int(action / 6) + 1
    #     policy_class = int((action - (serial_number - 1) * 6) / 2) + 1  # 位置(1,2,3)
    #     energy_rank = (action - (serial_number - 1) * 6) % 2 + 1  # 四个能量级(1,2)
    #     if es_intensity <= 6:
    #         if policy_class != 2:
    #             return -1
    #     elif es_intensity > 6:
    #         if energy_rank != 1 or policy_class != 1:
    #             return -1
    #     return 1
    #
    # result = {}
    # from task import *
    # parameter["taskNum"] = 3
    # task = createTask()
    # env = Maze(task)
    # RL = QLearningTable(actions=list(range(env.n_actions)))
    # dataframe = pd.read_csv("./Q_learning Table" + str(3) + "taskNum.csv", index_col=0)
    # dataframe.columns = list(range(0, 3 * 6))
    # for state in dataframe.index:
    #     if state not in result:
    #         if int(state.split(".")[0][1:]) != 7 and int(state.split(".")[0][1:]) != -1:
    #             result[state] = 1
    #             max_action = RL.choose_action_real(state)
    #             result[state] = check(state,max_action)
    # print(result)
    #
    # t1 = []
    # t2 = []
    # for item in result:
    #     t1.append(item)
    #     t2.append(result[item])
    # fig,ax1 = plt.subplots()
    # plt.plot(t1,t2,".")
    # for xtick in ax1.get_xticklabels():
    #     xtick.set_rotation(50)
    # plt.show()
    # plt.close()
    from task import *
    task = createTask()
    env = Maze(task)
    RL = QLearningTable(actions=list(range(env.n_actions)))
    rewards = []
    for i in range(1000):
        observation = env.reset()
        while True:
            action = RL.choose_action_real(str(observation))
            observation_, reward, done = env.step(action)
            # RL.learn(str(observation), action, reward, str(observation_))
            observation = observation_
            # 如果掉下地狱或者升上天堂, 这回合就结束了
            if done:
                time = findmax(task)
                rewards.append(reward)
                break
    print(rewards)
    open("./Test", "w").write(str(rewards))
    Time3 = []
    for item in rewards:
        Time3.append(parameter["maxReward"] - item)
    print(np.mean(Time3))