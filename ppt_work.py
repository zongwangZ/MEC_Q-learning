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

filename1 = "/home/zongwangz/PycharmProjects/q_learning/result/count1"
filename2 = "/home/zongwangz/PycharmProjects/q_learning/result/convergedstate1"
counts = ast.literal_eval(open(filename1,"r").readline())
convergedStates = ast.literal_eval(open(filename2,"r").readline())
x = range(len(counts))
y1 = []
y2 = []
y3 =[]
for key in counts:
    y1.append(counts[key][0])
    y2.append(counts[key][1])
    y3.append(convergedStates[key])
# print(x)
# print(y1)
# print(y2)
# print(y3)
# y1 = np.log10(y1)
# y2 = np.log10(y2)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.bar(x,np.array(y1)/5000000,label="# Choose",color="blue")
ax1.bar(x,np.array(y2)/5000000,label="# opt",color="red")
ax2.scatter(x,y3,label="state",color="black")
ax1.set_ylabel("# hit",fontdict={'size':18})
ax2.set_ylabel("state value",fontdict={'size':18})
plt.xticks([0,5,10,15,20,25,30,35,39])
ax2.set_yticks([-1,1])
plt.xlabel("state",fontdict={'size':15})
plt.show()

# for i in [3,4,5,6,7,8]:
#     parameter["taskNum"] = i
#     filename = "/media/zongwangz/RealPAN-13438811621/q_learning/data/record/100_/"+str(i)+"/Q_learning Table"+str(i)+".csv"
#     calTime(filename)

# Q_learning1 = [166.545,339.07,493.4,389.025,790.75,713.97]
# random_choose = [401.178,475.155,605.5105,705.575,846.427,953.2165]
# brute_force = [43.8,55.05,69.5,79.6,102.8,110.15]
# Q_learning2 = [61.665,150.705,228.05,365.69,510.39,663.785]
# Q_learning3 = [59.33,78.26,127.705,116.89,198.965,277.66]
# max = 953.2165
# plt.subplots()
# plt.plot([3,4,5,6,7,8],np.log10(random_choose)/np.log10(max),marker=".",linestyle="--",label="Random")
# plt.plot([3,4,5,6,7,8],np.log10(brute_force)/np.log10(max),marker="o",linestyle="--",label="Brute_force")
# plt.plot([3,4,5,6,7,8],np.log10(Q_learning1)/np.log10(max),"v-",label="Q_learning(100thousand)")
# plt.plot([3,4,5,6,7,8],np.log10(Q_learning2)/np.log10(max),"<-",label="Q_learning(300thousand)")
# plt.plot([3,4,5,6,7,8],np.log10(Q_learning3)/np.log10(max),">-",label="Q_learning(1000thousand)")
# # plt.plot([3,4,5,6,7,8],random_choose,"-.",label="Random")
# # plt.plot([3,4,5,6,7,8],brute_force,"-o",label="Brute_force")
# # plt.plot([3,4,5,6,7,8],Q_learning1,label="Q_learning(100thousand)")
# # plt.plot([3,4,5,6,7,8],Q_learning2,label="Q_learning(300thousand)")
# # plt.plot([3,4,5,6,7,8],Q_learning3,label="Q_learning(1000thousand)")
# value = (np.log10(brute_force)/np.log10(max))[0]
# plt.annotate(s=str(round(value,3)),xy=(3,value),xytext=(3,0.7),
#              arrowprops={'arrowstyle':'->'})
# plt.xlabel("#task",fontdict={'size':15})
# plt.ylabel("consumed_time",fontdict={'size':15})
# plt.xticks([3,4,5,6,7,8])
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.legend(loc=2,prop={'size': 12})
# plt.show()

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
# x1 = [1, 7, 14, 20, 112, 123, 132, 148, 183, 215, 216, 228, 246, 336, 447, 853, 1714, 1716]
# x2 = [1, 7, 14, 20, 112, 123, 132, 148, 183, 215, 216, 228, 246, 336, 447, 853, 1714, 1716]
# y2 = [365.9695, 251.275, 246.478, 182.1475, 91.6215, 91.189, 91.0145, 89.9225, 87.5825, 86.2395, 86.9475, 85.118, 75.4505, 75.5365, 76.1735, 75.656, 74.4175, 75.506]
# y1 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
# # plt.subplots()
# # plt.plot(x1,y1,"o-")
# # plt.xlabel("#episode",fontdict={'size':15})
# # plt.ylabel("#converged state",fontdict={'size':15})
# # plt.xlim((1,3001))
# # plt.annotate(s='37',xy=(2076,37),xytext=(2200,30),
# #              arrowprops={'arrowstyle':'->'})
# # plt.show()
# # plt.close()
# #
# max = 1000.451
# y2 = np.log10(y2)/np.log10(max)
# plt.subplots()
# plt.plot(x2,y2,".-")
# plt.xlabel("#episode",fontdict={'size':15})
# plt.ylabel("consumed_time",fontdict={'size':15})
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
# bruteTime = [55.7,113.3,247.1,355.65,411.55,440.5,]
# Q_Time = [189.275,379.477,363.5475,469.862,535.143,614.146]

#任务数量和训练次数
# training = int(sys.argv[1])
# tasknum = int(sys.argv[2])
# if training == 10:
#     parameter["taskNum"] = tasknum
#     parameter["intensity"] = 6
#     task = createTask()
#     env = Maze(task)
#     RL = QLearningTable(actions=list(range(env.n_actions)))
#     train(env,RL,100000)
#     RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
#     Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
#     print("training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)
# if training == 30:
#     parameter["taskNum"] = tasknum
#     parameter["intensity"] = 6
#     task = createTask()
#     env = Maze(task)
#     RL = QLearningTable(actions=list(range(env.n_actions)))
#     train(env,RL,300000)
#     RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
#     Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
#     print("training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)
# if training == 100:
#     parameter["taskNum"] = tasknum
#     parameter["intensity"] = 6
#     task = createTask()
#     env = Maze(task)
#     RL = QLearningTable(actions=list(range(env.n_actions)))
#     train(env,RL,1000000)
#     RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
#     Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
#     print("training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)
#
# #将两个大实验跑了一下
# [3,4,5,6,7,8]
# #10万次
# Q_learning1 = [199.794,399.2845,435.464,619.9595,700.9,829.568,]
# #30万次
# Q_learning2 = [111.5515,107.1015,198.724,435.7295,617.3015,739.763]
# #100万次
# Q_learning3 = [51.032,103.634,109.7885,138.45,214.44,260.324]
# random = [401.178,475.155,605.5105,705.575,846.427,953.2165]
# brute_force = [43.8,55.05,69.5,79.6,103.95,110.15]
#
#
# [4,8,12,16,20]
# bruteTime = [49.25,230.75,420.55,446.2,450.0]
# Q_time = [110.238,525.6155,581.635,525.5395,405.487]

#因为findmax有一些问题，需要修改Random和Brute-force所有的结果，Q-learning的训练不受影响，但是结果需要重新运行
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


# import sys
# from global_variables import *
# import randomChoose
# from task import *
# import brute
# if sys.argv[1] == "Random":
#     taskNum = [3,4,5,6,7,8]
#     randomTime = []
#     for tasknum in taskNum:
#         parameter["taskNum"] = tasknum
#         parameter["intensity"] = 6
#         Time = []
#         task = createTask()
#         for i in range(10000):
#             resetTask(task)
#             time = randomChoose.doRandom(task)
#             Time.append(time)
#         randomTime.append(np.mean(Time))
#     print("randomTime")
# elif sys.argv[1] == "Brute-force":
#     tasknum = int(sys.argv[2])
#     parameter["taskNum"] = tasknum
#     parameter["intensity"] = 6
#     task = createTask()
#     bruteTime = 0
#     Time = []
#     for i in range(100):
#         resetTask(task)
#         Time.append(brute.brute_force(task))
#     bruteTime = np.mean(Time)
#     print("tasknum:",tasknum,"bruteTime:",bruteTime)

#重新将训练好的数据取下来

# Q_learning = [190.079,376.768,363.5555,472.5135,536.586,614.1145]
# for i in [4,6,8,10,12,14]:
#     filename = "/home/zongwangz/PycharmProjects/q_learning/ex2/Q_learning Table"+str(i)+"T"
#     parameter["taskNum"] = 8
#     parameter["intensity"] = i
#     print(i,calTime(filename))


# Q_learning = []
# for i in [4,8,12,16,20]:
#     filename = "/home/zongwangz/PycharmProjects/q_learning/ex3/Q_learning Table"+str(i)+"T"
#     parameter["taskNum"] = 8
#     parameter["intensity"] = i
#     print(i,calTime(filename))

#500 【4,8,12,16,20】
# Q_learning = [63.796,306.498,400.0245,505.1025,502.1005]
# random_time = [711.611, 1347.2085, 1755.317, 1802.93, 1805.5225]
# brute_time = [48.5,232.4,421.05,449.05,450.0]
# plt.subplots()
# max = 1805.5225
# plt.plot([4,8,12,16,20],np.log10(random_time)/np.log10(max),marker=".",linestyle="--",label="Random")
# plt.plot([4,8,12,16,20],np.log10(brute_time)/np.log10(max),marker="o",linestyle="--",label="Brute_force")
# plt.plot([4,8,12,16,20],np.log10(Q_learning)/np.log10(max),"v-",label="Q_learning(500thousand)")
# plt.xlabel("#task(es)",fontdict={'size':15})
# plt.ylabel("consumed_time",fontdict={'size':15})
# plt.xticks([4,8,12,16,20])
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.legend(loc=2,prop={'size': 12})
# plt.show()

# for i in [4,8,12,16,20]:
#     filename = "/home/zongwangz/PycharmProjects/q_learning/ex4/Q_learning Table"+str(i)+"T"
#     parameter["taskNum"] = 8
#     parameter["intensity"] = i
#     print(i,calTime(filename))

# random_choose = [403.271, 468.477, 604.622, 716.2075, 844.8895, 947.1545]
# brute_force = [47.85,54.6,65.45,82.35,98.25,115.1]
# Q_learning1 = [198.8085,396.7,440.411,627.1005,700.024,826.8125]
# Q_learning2 = [111.814,107.7825,198.6045,436.1815,616.3935,743.348]
# Q_learning3 = [51.2655,103.042,110.373,140.693,211.537,258.4615]
# # for i in [3,4,5,6,7,8]:
# #     filename = "/home/zongwangz/PycharmProjects/q_learning/ex3/Q_learning Table" +"10"+"_"+ str(i)+"T"
# #     parameter["taskNum"] = i
# #     parameter["intensity"] = 6
# #     print(i, calTime(filename))
# max = 947.1545
# plt.subplots()
# plt.plot([3,4,5,6,7,8],np.log10(random_choose)/np.log10(max),marker=".",linestyle="--",label="Random")
# plt.plot([3,4,5,6,7,8],np.log10(brute_force)/np.log10(max),marker="o",linestyle="--",label="Brute_force")
# plt.plot([3,4,5,6,7,8],np.log10(Q_learning1)/np.log10(max),"v-",label="Q_learning(100thousand)")
# plt.plot([3,4,5,6,7,8],np.log10(Q_learning2)/np.log10(max),"<-",label="Q_learning(300thousand)")
# plt.plot([3,4,5,6,7,8],np.log10(Q_learning3)/np.log10(max),">-",label="Q_learning(1000thousand)")
# # plt.plot([3,4,5,6,7,8],random_choose,"-.",label="Random")
# # plt.plot([3,4,5,6,7,8],brute_force,"-o",label="Brute_force")
# # plt.plot([3,4,5,6,7,8],Q_learning1,label="Q_learning(100thousand)")
# # plt.plot([3,4,5,6,7,8],Q_learning2,label="Q_learning(300thousand)")
# # plt.plot([3,4,5,6,7,8],Q_learning3,label="Q_learning(1000thousand)")
# value = (np.log10(brute_force)/np.log10(max))[0]
# plt.annotate(s=str(round(value,3)),xy=(3,value),xytext=(3,0.65),
#              arrowprops={'arrowstyle':'->'})
# plt.xlabel("#task",fontdict={'size':15})
# plt.ylabel("consumed_time",fontdict={'size':15})
# plt.xticks([3,4,5,6,7,8])
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.legend(loc=2,prop={'size': 12})
# plt.show()

#先让Q表恢复正常
# import re
# for i in [4,8,12,16,20]:
#     filename = "/home/zongwangz/PycharmProjects/q_learning/ex4/Q_learning Table"+str(i)
#     lines = open(filename,"r").readlines()
#     tFilename = "/home/zongwangz/PycharmProjects/q_learning/ex4/Q_learning Table"+str(i)+"T"
#     file = open(tFilename,"a+")
#     for line in lines:
#         if "e" in line:
#             state = np.zeros(3)
#             s1,s2,s3 = line.split(",")[0][1:-1].split(" ")
#             state[0] = int(float(s1.split("e+")[0])*10**int(s1.split("e+")[1]))
#             state[1] = int(float(s2.split("e+")[0]) * 10 ** int(s2.split("e+")[1]))
#             state[2] = int(float(s3.split("e+")[0]) * 10 ** int(s3.split("e+")[1]))
#             line_ = copy.copy(line)
#             line__ = line_.replace(line.split(",")[0],str(state))
#             print(line__)
#             file.write(line__)
#         else:
#             file.write(line)