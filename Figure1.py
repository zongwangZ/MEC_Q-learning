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
if sys.argv[1] == "Random":
    taskNum = [3,4,5,6,7,8]
    randomTime = []
    for tasknum in taskNum:
        parameter["taskNum"] = tasknum
        parameter["intensity"] = 6
        Time = []
        task = createTask()
        for i in range(10000):
            resetTask(task)
            time = randomChoose.doRandom(task)
            Time.append(time)
        randomTime.append(np.mean(Time))
    print("Figure1:   ","randomTime:",randomTime)
elif sys.argv[1] == "Brute-force":
    tasknum = int(sys.argv[2])
    parameter["taskNum"] = tasknum
    parameter["intensity"] = 6
    task = createTask()
    bruteTime = 0
    Time = []
    for i in range(100):
        resetTask(task)
        Time.append(brute.brute_force(task))
    bruteTime = np.mean(Time)
    print("Figure1:   ","tasknum:",tasknum,"bruteTime:",bruteTime)
elif sys.argv[1] == "Q-learning":
    training = int(sys.argv[2])
    tasknum = int(sys.argv[3])
    if training == 10:
        parameter["taskNum"] = tasknum
        parameter["intensity"] = 6
        task = createTask()
        env = Maze(task)
        RL = QLearningTable(actions=list(range(env.n_actions)))
        train(env,RL,100000)
        RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
        Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
        print("Figure1:   ","training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)
    if training == 30:
        parameter["taskNum"] = tasknum
        parameter["intensity"] = 6
        task = createTask()
        env = Maze(task)
        RL = QLearningTable(actions=list(range(env.n_actions)))
        train(env,RL,300000)
        RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
        Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
        print("Figure1:   ","training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)
    if training == 100:
        parameter["taskNum"] = tasknum
        parameter["intensity"] = 6
        task = createTask()
        env = Maze(task)
        RL = QLearningTable(actions=list(range(env.n_actions)))
        train(env,RL,1000000)
        RL.q_table.to_csv("Q_learning Table" + str(training)+"_"+str(tasknum))
        Q_time = calTime("Q_learning Table" + str(training)+"_"+str(tasknum))
        print("Figure1:   ","training:",training,"tasknum:",tasknum,"Q_learning time:",Q_time)