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
if sys.argv[1] == "Random":
    parameter["taskNum"] = tasknumer
    intensities = [4, 8, 12, 16, 20]
    randomTime = []
    task = createTask()
    for intensity in intensities:
        Time = []
        parameter["intensity"] = intensity
        for i in range(10000):
            resetTask(task)
            time = randomChoose.doRandom(task)
            Time.append(time)
        randomTime.append(np.mean(Time))
    print("Figure2:   ","Random time:",randomTime)
elif sys.argv[1] == "Brute-force":
    intensity = int(sys.argv[2])
    parameter["taskNum"] = tasknumer
    parameter["intensity"] = intensity
    task = createTask()
    bruteTime = 0
    Time = []
    for i in range(100):
        resetTask(task)
        Time.append(brute.brute_force(task))
    bruteTime = np.mean(Time)
    print("Figure2:   ","intensity:",intensity,"bruteTime:",bruteTime)
elif sys.argv[1] == "Q_learning":
    parameter["taskNum"] = tasknumer
    intensity = int(sys.argv[2])
    parameter["intensity"] = intensity
    task = createTask()
    env = Maze(task)
    RL = QLearningTable(actions=list(range(env.n_actions)))
    train(env,RL)
    RL.q_table.to_csv("Q_learning Table" + str(intensity))
    Q_time = calTime("Q_learning Table" + str(intensity))
    print("Figure2:   ","intensity:",intensity,"Q_learning time:",Q_time)