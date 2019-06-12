# -*- coding: utf-8 -*-
'''
@project:q_learning
@author:zongwangz
@time:19-5-26 下午5:25
@email:zongwang.zhang@outlook.com
'''
'''
为了PPT出图
'''
from run_this3 import *
# filelist = []
# for i in range(10):
#     filename = "/media/zongwangz/RealPAN-13438811621/myUbuntu/q_learning/q_learning/data/record/"+str((i+1)*10000)+"/logFile"+str((i+1)*10000)
#     filelist.append(filename)
# view(filelist)

# printConvergedState("/media/zongwangz/RealPAN-13438811621/myUbuntu/q_learning/q_learning/data/record/100000/Q_learning Table100000")

# filename1 = "/home/zongwangz/桌面/ppt/counts/counts"
# filename2 = "/home/zongwangz/桌面/ppt/convergedStates/convergedStates"
# counts = ast.literal_eval(open(filename1,"r").readline())
# convergedStates = ast.literal_eval(open(filename2,"r").readline())
# x = range(len(counts))
# y1 = []
# y2 = []
# y3 =[]
# for key in counts:
#     y1.append(counts[key][0])
#     y2.append(counts[key][1])
#     y3.append(convergedStates[key])
# # print(x)
# # print(y1)
# # print(y2)
# # print(y3)
# # y1 = np.log10(y1)
# # y2 = np.log10(y2)
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
# ax1.bar(x,y1,label="#Choose",color="blue")
# ax1.bar(x,y2,label="#opt",color="red")
# ax2.scatter(x,y3,label="state",color="black")
# plt.xlabel("training steps")
# ax1.set_ylabel("#hit")
# ax2.set_ylabel("state value")
# plt.xticks([0,5,10,15,20,25,30,35,39])
# ax2.set_yticks([-1,1])
# plt.legend()
# plt.show()

# for i in [3,4,5,6,7,8]:
#     parameter["taskNum"] = i
#     filename = "/media/zongwangz/RealPAN-13438811621/q_learning/data/record/100_/"+str(i)+"/Q_learning Table"+str(i)+".csv"
#     calTime(filename)

Q_learning1 = [166.545,339.07,493.4,389.025,790.75,713.97]
random_choose = [401.178,475.155,605.5105,705.575,846.427,953.2165]
brute_force = [43.8,55.05,69.5,79.6,102.8,110.15]
Q_learning2 = [61.665,150.705,228.05,365.69,510.39,663.785]
Q_learning3 = [59.33,78.26,127.705,116.89,198.965,277.66]
max = 953.2165
plt.subplots()
plt.plot([3,4,5,6,7,8],np.log10(random_choose)/np.log10(max),"-.",label="Random")
plt.plot([3,4,5,6,7,8],np.log10(brute_force)/np.log10(max),"-o",label="Brute_force")
plt.plot([3,4,5,6,7,8],np.log10(Q_learning1)/np.log10(max),label="Q_learning(100thousand)")
plt.plot([3,4,5,6,7,8],np.log10(Q_learning2)/np.log10(max),label="Q_learning(300thousand)")
plt.plot([3,4,5,6,7,8],np.log10(Q_learning3)/np.log10(max),label="Q_learning(1000thousand)")
# plt.plot([3,4,5,6,7,8],random_choose,"-.",label="Random")
# plt.plot([3,4,5,6,7,8],brute_force,"-o",label="Brute_force")
# plt.plot([3,4,5,6,7,8],Q_learning1,label="Q_learning(100thousand)")
# plt.plot([3,4,5,6,7,8],Q_learning2,label="Q_learning(300thousand)")
# plt.plot([3,4,5,6,7,8],Q_learning3,label="Q_learning(1000thousand)")
value = (np.log10(brute_force)/np.log10(max))[0]
plt.annotate(s=str(round(value,3)),xy=(3,value),xytext=(3,0.7),
             arrowprops={'arrowstyle':'->'})
plt.xlabel("#task")
plt.ylabel("consumed_time")
plt.xticks([3,4,5,6,7,8])
plt.legend(loc=2)
plt.show()

#输出3000万次状态收敛数和时间变化曲线
'''
1 10
378.9575
2 11
318.355
3 12
284.393
4 14
244.5885
6 15
200.993
10 17
119.206
14 18
103.4755
16 19
102.924
17 20
103.859
24 21
81.0765
26 22
78.029
27 23
75.3275
44 24
75.3245
514 25
61.81
517 26
61.303
794 27
60.585
813 28
59.3945
840 29
57.59
853 30
55.1385
1040 31
50.826
1699 32
50.7005
1732 33
50.667
1811 34
49.3905
1831 35
49.125
1962 36
49.013
2076 37
48.264
'''
# x1 = [1, 2, 3, 4, 6, 10, 14, 16, 17, 24, 26, 27, 44, 514, 517, 794, 813, 840, 853, 1040, 1699, 1732, 1811, 1831, 1962, 2076]
# x2 = [1, 2, 3, 4, 6, 10, 14, 16, 17, 24, 26, 27, 44, 514, 517, 794, 813, 840, 853, 1040, 1699, 1732, 1811, 1831, 1962, 2076]
# y2 = [378.9575, 318.355, 284.393, 244.5885, 200.993, 119.206, 103.4755, 102.924, 103.859, 81.0765, 78.029, 75.3275, 75.3245, 61.81, 61.303, 60.585, 59.3945, 57.59, 55.1385, 50.826, 50.7005, 50.667, 49.3905, 49.125, 49.013, 48.264]
# y1 = [10, 11, 12, 14, 15, 17, 18, 19, 20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]
# plt.subplots()
# plt.plot(x1,y1,"o-")
# plt.xlabel("#episode")
# plt.ylabel("#converged state")
# plt.xlim((1,3001))
# plt.annotate(s='37',xy=(2076,37),xytext=(2200,37),
#              arrowprops={'arrowstyle':'->'})
# plt.show()
# plt.close()
#
# max = 953.2165
# y2 = np.log10(y2)/np.log10(max)
# plt.subplots()
# plt.plot(x2,y2,".-")
# plt.xlabel("#episode")
# plt.ylabel("consumed_time")
# plt.xlim((1,3001))
# plt.annotate(s=str(round(y2[-1],3)),xy=(2076,y2[-1]),xytext=(2500,y2[-1]),
#              arrowprops={'arrowstyle':'->'})
# plt.show()


#针对未收敛的三个状态 输出他们经历的次数 [   3. 4300.   10.]   [   1. 4400.   10.]  [   3. 4300.    8.]
# def view1(filelist):
#     '''
#     对多个logfile进行输出内容
#     :param filelist:
#     :return:
#     '''
#     count = {}
#     cnt = 0 ##记步数
#     for filename in filelist:
#         file = open(filename, "r")
#         while True:
#             line = file.readline()
#             cnt += 1
#             if line:
#                 log_list = [ast.literal_eval(item) for item in line.split("|")]
#                 for i in range(len(log_list)):
#                     s, a, Q_sa, r, maxQ, maxAction, optQ, optAction, s_ = log_list[i]
#                     if s not in count:
#                         count[s] = [0,0]
#                         count[s][0] += 1
#                         if check(s,a) == 1:
#                             count[s][1] += 1
#                     else:
#                         count[s][0] += 1
#                         if check(s, a) == 1:
#                             count[s][1] += 1
#             else:
#                 break
#     print(count)
# dir = "/home/zongwangz/PycharmProjects/q_learning/data/record/corret"
# filelist = []
# for i in range(10):
#     filename = dir+"/"+str((i+1)*10000)+"/logFile"+str((i+1)*10000)
#     filelist.append(filename)
# view1(filelist)

# state1 = [] #[   3. 4300.   10.]
# state2 = []#[   1. 4400.   10.]
# state3 = []#[   3. 4300.    8.]
# filename = "/home/zongwangz/PycharmProjects/q_learning/nohup.out"
# file = open(filename, "r")
# while True:
#     line = file.readline()
#     if line:
#         item = ast.literal_eval(line)
#         if isinstance(item,dict):
#             if "[   3. 4300.   10.]" in item:
#                 state1.append(item["[   3. 4300.   10.]"])
#             if "[   1. 4400.   10.]" in item:
#                 state2.append(item["[   1. 4400.   10.]"])
#             if "[   3. 4300.    8.]" in item:
#                 state3.append(item["[   3. 4300.    8.]"])
#     else:
#         break
# print(state1)
# print(state2)
# print(state3)
# for state in [state1,state2,state3]:
#     hit_1 = 0
#     hit_2 = 1
#     for item in state:
#         hit_1 += item[0]
#         hit_2 += item[1]
#     print(hit_1,hit_2)

#输出泊松强度强度与消耗时间图
# import sys
# from global_variables import *
# import randomChoose
# from task import *
# import brute
# tasknumer = 8
# from maze_env import Maze
# from RL_brain import QLearningTable
# if sys.argv[1] == "Random":
#     parameter["taskNum"] = tasknumer
#     intensities = [4, 8, 12, 16, 20]
#     randomTime = []
#     task = createTask()
#     for intensity in intensities:
#         Time = []
#         parameter["intensity"] = intensity
#         for i in range(10000):
#             resetTask(task)
#             time = randomChoose.doRandom(task)
#             Time.append(time)
#         randomTime.append(np.mean(Time))
#     print("Random time:",randomTime)
# elif sys.argv[1] == "Brute-force":
#     intensity = int(sys.argv[2])
#     parameter["taskNum"] = tasknumer
#     parameter["intensity"] = intensity
#     task = createTask()
#     bruteTime = 0
#     Time = []
#     for i in range(100):
#         resetTask(task)
#         Time.append(brute.brute_force(task))
#     bruteTime = np.mean(Time)
#     print("intensity:",intensity,"bruteTime:",bruteTime)
# elif sys.argv[1] == "Q_learning":
#     parameter["taskNum"] = tasknumer
#     intensity = int(sys.argv[2])
#     parameter["intensity"] = intensity
#     task = createTask()
#     env = Maze(task)
#     RL = QLearningTable(actions=list(range(env.n_actions)))
#     train(env,RL)
#     RL.q_table.to_csv("Q_learning Table" + str(intensity))
#     Q_time = calTime("Q_learning Table" + str(intensity))
#     print("intensity:",intensity,"Q_learning time:",Q_time)
# intensities = [4,6,8,10,12,14]
# randomTime = [710.2185, 951.1735, 1349.6915, 1645.8505, 1759.8135, 1799.751]
# bruteTime = [55.7,113.3,247.1,247.1,355.65,411.55,440.5,]
# Q_Time = [189.275,379.477,363.5475,469.862,535.143,614.146]

#任务数量和训练次数
training = int(sys.argv[1])
tasknum = int(sys.argv[2])
if training == 10:
    parameter["taskNum"] = tasknum
    parameter["intensity"] = 6
    task = createTask()
    env = Maze(task)
    RL = QLearningTable(actions=list(range(env.n_actions)))
    train(env,RL,100000)
    RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
    Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
    print("training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)
if training == 30:
    parameter["taskNum"] = tasknum
    parameter["intensity"] = 6
    task = createTask()
    env = Maze(task)
    RL = QLearningTable(actions=list(range(env.n_actions)))
    train(env,RL,300000)
    RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
    Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
    print("training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)
if training == 100:
    parameter["taskNum"] = tasknum
    parameter["intensity"] = 6
    task = createTask()
    env = Maze(task)
    RL = QLearningTable(actions=list(range(env.n_actions)))
    train(env,RL,1000000)
    RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
    Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
    print("training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)