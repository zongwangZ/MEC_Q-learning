# -*- coding: utf-8 -*-
'''
@project:q_learning
@author:zongwangz
@time:19-6-17 下午7:26
@email:zongwang.zhang@outlook.com
Figure2 的实验代码 time vs intensity
'''
import sys
from run_this3 import *
from global_variables import *
import randomChoose
from task import *
import brute
tasknumer = 8
from maze_env import Maze
from RL_brain import QLearningTable
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
#     print("Figure2:   ","Random time:",randomTime)
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
#     print("Figure2:   ","intensity:",intensity,"bruteTime:",bruteTime)
# elif sys.argv[1] == "Q_learning":
#     parameter["taskNum"] = tasknumer
#     intensity = int(sys.argv[2])
#     parameter["intensity"] = intensity
#     task = createTask()
#     env = Maze(task)
#     RL = QLearningTable(actions=list(range(env.n_actions)))
#     train(env,RL,5000000)
#     RL.q_table.to_csv("Q_learning Table" + str(intensity))
#     Q_time = calTime("Q_learning Table" + str(intensity))
#     print("Figure2:   ","intensity:",intensity,"Q_learning time:",Q_time)

'''
Figure2:    intensity: 8 bruteTime: 287.0
Figure2:    intensity: 20 bruteTime: 560.0
Figure2:    intensity: 16 bruteTime: 555.25
Figure2:    intensity: 12 bruteTime: 545.75
Figure2:    intensity: 4 bruteTime: 53.0
Figure2:    Random time: [760.7475, 1400.457, 1809.7705, 1860.674, 1868.1635]


maxreward错误
Figure2:    intensity: 12 Q_learning time: 248.0335
Figure2:    intensity: 4 Q_learning time: 162.5635
Figure2:    intensity: 8 Q_learning time: 316.554
Figure2:    intensity: 16 Q_learning time: 320.1125
Figure2:    intensity: 20 Q_learning time: 420.3795

Figure2:    intensity: 20 Q_learning time: 592.341
Figure2:    intensity: 8 Q_learning time: 351.718
Figure2:    intensity: 16 Q_learning time: 563.939
Figure2:    intensity: 4 Q_learning time: 168.1205
Figure2:    intensity: 12 Q_learning time: 560.313
'''

Random = [760.7475, 1400.457, 1809.7705, 1860.674, 1868.1635]
Brute = [53.0,287.0,545.75,555.25,560.0]
Q_learning = [168.1205,351.718,560.313,563.939,592.341]

Q_learning = [168.1205,351.718,560.313,563.939,592.341]
random_time = [760.7475, 1400.457, 1809.7705, 1860.674, 1868.1635]
brute_time = [53.0,287.0,545.75,555.25,560.0]
plt.subplots()
max = 1868.1635
plt.plot([4,8,12,16,20],np.log10(random_time)/np.log10(max),markersize=10,linewidth =3.5,marker=".",linestyle="--",label="Random")
plt.plot([4,8,12,16,20],np.log10(brute_time)/np.log10(max),markersize=10,linewidth =3.5,marker="o",linestyle="--",label="Brute-force")
plt.plot([4,8,12,16,20],np.log10(Q_learning)/np.log10(max),"v-",markersize=10,linewidth =3.5,label="Q-learning(5e6)")
plt.xlabel("# task(es)",fontdict={'size':18})
plt.ylabel("consumed time",fontdict={'size':18})
plt.xticks([4,8,12,16,20])
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc=2,prop={'size': 12})
plt.show()