# -*- coding: utf-8 -*-
'''
@project:q_learning
@author:zongwangz
@time:19-6-17 下午7:05
@email:zongwang.zhang@outlook.com
Figure1 的实验代码  时间vs任务数量
'''
from run_this3 import *
import sys
from global_variables import *
import randomChoose
from task import *
import brute
from maze_env import Maze
from RL_brain import QLearningTable
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
#     print("Figure1:   ","randomTime:",randomTime)
# elif sys.argv[1] == "Brute-force":
#     tasknum = int(sys.argv[2])
#     parameter["taskNum"] = tasknum
#     parameter["intensity"] = 6
#     task = createTask()
#     bruteTime = 0
#     Time = []
#     for i in range(1000):
#         resetTask(task)
#         Time.append(brute.brute_force(task))
#     bruteTime = np.mean(Time)
#     print("Figure1:   ","tasknum:",tasknum,"bruteTime:",bruteTime)
# elif sys.argv[1] == "Q-learning":
#     training = int(sys.argv[2])
#     tasknum = int(sys.argv[3])
#     if training == 10:
#         parameter["taskNum"] = tasknum
#         parameter["intensity"] = 6
#         task = createTask()
#         env = Maze(task)
#         RL = QLearningTable(actions=list(range(env.n_actions)))
#         train(env,RL,100000)
#         RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
#         Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
#         print("Figure1:   ","training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)
#     if training == 30:
#         parameter["taskNum"] = tasknum
#         parameter["intensity"] = 6
#         task = createTask()
#         env = Maze(task)
#         RL = QLearningTable(actions=list(range(env.n_actions)))
#         train(env,RL,300000)
#         RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
#         Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
#         print("Figure1:   ","training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)
#     if training == 100:
#         parameter["taskNum"] = tasknum
#         parameter["intensity"] = 6
#         task = createTask()
#         env = Maze(task)
#         RL = QLearningTable(actions=list(range(env.n_actions)))
#         train(env,RL,1000000)
#         RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
#         Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
#         print("Figure1:   ","training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)
#     if training == 500:
#         parameter["taskNum"] = tasknum
#         parameter["intensity"] = 6
#         task = createTask()
#         env = Maze(task)
#         RL = QLearningTable(actions=list(range(env.n_actions)))
#         train(env,RL,5000000)
#         RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
#         Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
#         print("Figure1:   ","training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)
#     if training == 20:
#         parameter["taskNum"] = tasknum
#         parameter["intensity"] = 6
#         task = createTask()
#         env = Maze(task)
#         RL = QLearningTable(actions=list(range(env.n_actions)),filename="Q_learning Table" + str(10)+"_"+str(tasknum))
#         train(env,RL,200000)
#         RL.q_table.to_csv("Q_learning Table" + str(30)+"_"+str(tasknum))
#         Q_time = calTime("Q_learning Table" + str(30)+"_"+str(tasknum))
#         print("Figure1:   ","training:",30,"tasknum:",tasknum,"Q_learning time:",Q_time)
#     if training == 70:
#         parameter["taskNum"] = tasknum
#         parameter["intensity"] = 6
#         task = createTask()
#         env = Maze(task)
#         RL = QLearningTable(actions=list(range(env.n_actions)),filename="Q_learning Table" + str(30)+"_"+str(tasknum))
#         train(env,RL,700000)
#         RL.q_table.to_csv("Q_learning Table" + str(100)+"_"+str(tasknum))
#         Q_time = calTime("Q_learning Table" + str(100)+"_"+str(tasknum))
#         print("Figure1:   ","training:",100,"tasknum:",tasknum,"Q_learning time:",Q_time)

'''
Figure1:    randomTime: [420.7585, 495.8805, 638.9025, 747.8265, 881.1415, 1000.451]
Figure1:    tasknum: 3 bruteTime: 54.6
Figure1:    tasknum: 4 bruteTime: 60.45
Figure1:    tasknum: 5 bruteTime: 78.5
Figure1:    tasknum: 6 bruteTime: 84.9
Figure1:    tasknum: 7 bruteTime: 94.3
Figure1:    tasknum: 8 bruteTime: 119.45

maxreward错误
Figure1:    training: 10 tasknum: 3 Q_learning time: 132.966
Figure1:    training: 10 tasknum: 4 Q_learning time: 186.82
Figure1:    training: 10 tasknum: 5 Q_learning time: 308.275
Figure1:    training: 10 tasknum: 6 Q_learning time: 354.191
Figure1:    training: 10 tasknum: 7 Q_learning time: 418.9015
Figure1:    training: 10 tasknum: 8 Q_learning time: 430.1675
Figure1:    training: 30 tasknum: 3 Q_learning time: 93.383
Figure1:    training: 30 tasknum: 4 Q_learning time: 129.9885
Figure1:    training: 30 tasknum: 5 Q_learning time: 191.5095
Figure1:    training: 30 tasknum: 6 Q_learning time: 216.8865
Figure1:    training: 30 tasknum: 7 Q_learning time: 301.4595
Figure1:    training: 30 tasknum: 8 Q_learning time: 296.195

Figure1:    training: 100 tasknum: 3 Q_learning time: 115.953
Figure1:    training: 100 tasknum: 4 Q_learning time: 105.5355
Figure1:    training: 100 tasknum: 5 Q_learning time: 158.4775
Figure1:    training: 100 tasknum: 6 Q_learning time: 157.2375
Figure1:    training: 100 tasknum: 7 Q_learning time: 212.995
Figure1:    training: 100 tasknum: 8 Q_learning time: 223.747

Figure1:    training: 500 tasknum: 3 Q_learning time: 97.657
Figure1:    training: 500 tasknum: 4 Q_learning time: 94.0315
Figure1:    training: 500 tasknum: 5 Q_learning time: 144.9595
Figure1:    training: 500 tasknum: 6 Q_learning time: 160.6995
Figure1:    training: 500 tasknum: 7 Q_learning time: 177.543
Figure1:    training: 500 tasknum: 8 Q_learning time: 225.5405


Figure1:    training: 30 tasknum: 3 Q_learning time: 103.3985
Figure1:    training: 30 tasknum: 4 Q_learning time: 129.1785
Figure1:    training: 30 tasknum: 5 Q_learning time: 204.994
Figure1:    training: 30 tasknum: 6 Q_learning time: 287.0845
Figure1:    training: 30 tasknum: 7 Q_learning time: 336.3575
Figure1:    training: 30 tasknum: 8 Q_learning time: 376.3395

Figure1:    training: 100 tasknum: 3 Q_learning time: 82.248
Figure1:    training: 100 tasknum: 4 Q_learning time: 102.8145
Figure1:    training: 100 tasknum: 5 Q_learning time: 157.8495
Figure1:    training: 100 tasknum: 6 Q_learning time: 174.6725
Figure1:    training: 100 tasknum: 7 Q_learning time: 200.179
Figure1:    training: 100 tasknum: 8 Q_learning time: 242.647







10
Figure1:    training: 10 tasknum: 3 Q_learning time: 388.6735
Figure1:    training: 10 tasknum: 4 Q_learning time: 447.315
Figure1:    training: 10 tasknum: 5 Q_learning time: 625.627
Figure1:    training: 10 tasknum: 6 Q_learning time: 725.055
Figure1:    training: 10 tasknum: 7 Q_learning time: 713.823
Figure1:    training: 10 tasknum: 8 Q_learning time: 977.472

100
Figure1:    training: 100 tasknum: 3 Q_learning time: 82.0815
Figure1:    training: 100 tasknum: 4 Q_learning time: 141.087
Figure1:    training: 100 tasknum: 5 Q_learning time: 158.251
Figure1:    training: 100 tasknum: 6 Q_learning time: 216.701
Figure1:    training: 100 tasknum: 7 Q_learning time: 360.999
Figure1:    training: 100 tasknum: 8 Q_learning time: 543.4965

Figure1:    training: 500 tasknum: 3 Q_learning time: 82.032
Figure1:    training: 500 tasknum: 4 Q_learning time: 112.765
Figure1:    training: 500 tasknum: 5 Q_learning time: 138.1935
Figure1:    training: 500 tasknum: 6 Q_learning time: 201.749
191.1645   
269.02
'''
r = [420.7585, 495.8805, 638.9025, 747.8265, 881.1415, 1000.451]
b = [48,50,78.5,84.9,94.3,119.45]
q1 = [388.6735,447.315,625.627,725.055,713.823,977.472]
q2 = [82.0815,141.087,158.251,216.701,360.999,543.4965]
q3 = [82.032,112.765,138.1935,201.749,191.1645,269.02]

Q_learning1 = [388.6735,447.315,625.627,725.055,713.823,977.472]
random_choose = [420.7585, 495.8805, 638.9025, 747.8265, 881.1415, 1000.451]
brute_force = [48,50,78.5,84.9,94.3,119.45]
Q_learning2 = [82.0815,141.087,158.251,216.701,360.999,543.4965]
Q_learning3 = [82.032,112.765,138.1935,201.749,191.1645,269.02]
max = 1000.451
plt.subplots()
plt.plot([3,4,5,6,7,8],np.log10(random_choose)/np.log10(max),markersize=10,marker=".",linestyle="--",linewidth =3.5,label="Random")
plt.plot([3,4,5,6,7,8],np.log10(brute_force)/np.log10(max),markersize=10,marker="o",linestyle="--",linewidth =3.5,label="Brute-force")
plt.plot([3,4,5,6,7,8],np.log10(Q_learning1)/np.log10(max),"X-",markersize=10,linewidth =3.5,label="Q-learning(1e5)")
plt.plot([3,4,5,6,7,8],np.log10(Q_learning2)/np.log10(max),"s-",markersize=10,linewidth =3.5,label="Q-learning(5e6)")
plt.plot([3,4,5,6,7,8],np.log10(Q_learning3)/np.log10(max),"^-",markersize=10,linewidth =3.5,label="Q-learning(1e7)")
# plt.plot([3,4,5,6,7,8],random_choose,"-.",label="Random")
# plt.plot([3,4,5,6,7,8],brute_force,"-o",label="Brute_force")
# plt.plot([3,4,5,6,7,8],Q_learning1,label="Q_learning(100thousand)")
# plt.plot([3,4,5,6,7,8],Q_learning2,label="Q_learning(1000thousand)")
# plt.plot([3,4,5,6,7,8],Q_learning3,label="Q_learning(5000thousand)")
value = (np.log10(brute_force)/np.log10(max))[0]
plt.annotate(s=str(round(value,3)),xy=(3,value),xytext=(4,0.62),
             arrowprops={'arrowstyle':'->'})
plt.xlabel("# task",fontdict={'size':18})
plt.ylabel("consumed time",fontdict={'size':18})
plt.xticks([3,4,5,6,7,8])
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc=2,prop={'size': 12})
plt.show()