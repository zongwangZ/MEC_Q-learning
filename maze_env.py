'''
我们参考了莫烦的代码，
https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/2_Q_Learning_maze
'''

import scipy.stats as st
import gym
import random
from gym.utils import seeding
from global_variables import *
from task import *
import copy
Energe = parameter["energe"]
maxReward = parameter["maxReward"]
energies = parameter["energies"]
class Maze(gym.Env):
    def __init__(self,task=None):
        super(Maze, self).__init__()
        if task == None:
            self.task = createTask()
        else:
            assert isinstance(task,networkx.DiGraph)
            self.task = task
        self.taskNum = parameter['taskNum']
        self.action_space = [[[0]*2]*3]*self.taskNum
        self.n_actions = 6 * self.taskNum  # len(self.action_space)
        # self.n_features = 2
        self.state = np.zeros(3)
        self.seed()
        self.poisson = self.initPoisson()

    def step(self, action):
        reward = 0
        CTaksQueue = self.state[0]  # 已完成的task
        self.energy_left = self.state[1]  # 能量
        ctask = CTaksQueue.astype(int)
        intensity = self.state[2]
        serial_number = int(action/6)+1  # 任务节点
        policy_class = int((action-(serial_number-1)*6)/2)+1  # 位置(1,2,3)
        energy_rank = (action-(serial_number-1)*6)%2+1  # 四个能量级(1,2)
        if not self.check_dependency(serial_number,ctask):
            #不满足依赖关系，则给予惩罚，任务队列，和能量不变，服务器状态不变
            done = False
            reward = -maxReward
            # self.state[2] = self.chooseIntensity()
            return copy.copy(self.state), reward, done
        else:
            #符合依赖关系
            #检查是否符合能量限制
            if self.check_energy(policy_class,energy_rank):  # 满足就开始执行
                CTaksQueue += 2 ** (serial_number-1)
                if policy_class == 1:  # 本地处理
                    if energy_rank == 1:
                        energy = energies[0][0]
                    elif energy_rank == 2:
                        energy = energies[0][1]
                    self.energy_left = self.energy_left - energy
                    time = device.calTime(energy,self.task.node[serial_number]["computing_circle"])
                    add_edge_time(self.task,serial_number,time)
                elif policy_class == 2:  # offloading到BS
                    if energy_rank == 1:
                        energy = energies[1][0]
                    elif energy_rank == 2:
                        energy = energies[1][1]
                    self.energy_left = self.energy_left - energy
                    time = edgeServer.calTime(self.task.node[serial_number]["data_size"],energy,intensity)
                    add_edge_time(self.task,serial_number,time)
                elif policy_class == 3:  # offloading到云端
                    if energy_rank == 1:
                        energy = energies[1][0]
                    elif energy_rank == 2:
                        energy = energies[1][1]
                    self.energy_left = self.energy_left - energy
                    time = cloudServer.calTime(self.task.node[serial_number]["data_size"],self.task.node[serial_number]["computing_circle"],energy)
                    add_edge_time(self.task, serial_number, time)
                if self.checkCompletion(CTaksQueue.astype(int)):
                    reward = maxReward - calOmegaT(self.task,CTaksQueue)
                    done = True
                    # print("complete")
                else:
                    done = False
                    reward = maxReward - calOmegaT(self.task,CTaksQueue)
                self.state[0] = CTaksQueue  # 已处理序列
                self.state[1] = self.energy_left  # 剩余电量
                self.state[2] = self.chooseIntensity()
                return copy.copy(self.state), reward, done

            else:  # 不满足能量限制关系
                self.state[0] = -1
                self.state[1] = -1
                self.state[2] = -1
                done = True
                reward = -maxReward
                return copy.copy(self.state),reward,done


    def reset(self):
        ##也要把任务图上的权重清除为0
        resetTask(self.task)
        self.state[0] = 0  # 已处理序列
        self.state[1] = Energe  # 能量
        self.state[2] = self.chooseIntensity()
        # self.state[2] = 8
        return copy.copy(self.state)


    def chooseIntensity(self):
        """
        从泊松分布中生成服务器任务数量
        :return:
        """
        randomD = np.random.uniform()
        p = copy.copy(self.poisson)
        taskNum_es = parameter["taskNum_es"]
        chosen = -1
        for i in range(len(p)-1):
            if i == 0 and randomD <= p[0] and randomD >= 0:
                chosen = 0
                break
            elif randomD > p[i] and randomD <= p[i+1]:
                chosen = i+1
                break
        chosen = taskNum_es[chosen]
        return chosen


    def initPoisson(self):
        """
        初始化泊松分布
        :return:
        """
        taskNum_es = parameter["taskNum_es"]
        assert isinstance(taskNum_es, list)
        intensity = parameter["intensity"]
        p = []
        for num in taskNum_es:
            if taskNum_es.index(num) == 0:
                probability = st.poisson.cdf(num, intensity)
            elif taskNum_es.index(num) == len(taskNum_es) - 1:
                probability = 1 - st.poisson.cdf(num, intensity)
            else:
                probability = st.poisson.pmf(num, intensity)
            p.append(probability)
        p = list(np.array(p) * 1 / sum(p))
        for i in range(len(p) - 1):
            p[i + 1] = p[i + 1] + p[i]
        # print(p)
        return p

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def check_dependency(self,serial_number,ctask):
        """
        检查是否符合依赖关系
        :param serial_number:
        :param ctask:
        :return:
        """
        flag1 = True
        task_queue = list(bin(ctask)[2:])
        task_queue.reverse()
        ##判断当前任务做没做
        if serial_number <= len(task_queue) and task_queue[serial_number-1] == "1":
            flag1 = False
            print("the task has been done")


        for pre_task in self.task.pred[serial_number]:
            if pre_task == 0:
                #满足依赖关系直接break
                break
            if pre_task > len(task_queue):
                flag1 = False
            elif task_queue[pre_task-1] != "1":
                flag1 = False
        return flag1

    def check_energy(self,policy_class,energy_rank):
        """
        检查是否符合能量依赖
        :param policy_class:
        :param energy_rank:
        :return:
        """
        flag2 = False
        if self.energy_left >= parameter["total_power"]*(1-parameter["power_percentage"]):
            if policy_class == 1 and energy_rank == 1 and self.energy_left-parameter["total_power"]*(1-parameter["power_percentage"]) >= energies[0][0]:
                flag2 = True
            elif policy_class == 1 and energy_rank == 2 and self.energy_left-parameter["total_power"]*(1-parameter["power_percentage"]) >= energies[0][1]:
                flag2 = True
            elif policy_class != 1 and energy_rank == 1 and self.energy_left-parameter["total_power"]*(1-parameter["power_percentage"]) >= energies[1][0]:
                flag2 = True
            elif policy_class != 1 and energy_rank == 2 and self.energy_left-parameter["total_power"]*(1-parameter["power_percentage"]) >= energies[1][1]:
                flag2 = True
        return flag2


    def checkCompletion(self,ctask):
        '''
        检查整个任务是否完成
        :return:
        '''
        flag = True
        task_queue = list(bin(ctask)[2:])
        task_queue.reverse()
        if len(task_queue) == self.taskNum:
            for item in task_queue:
                if item == "0":
                    flag = False
        else:
            flag = False
        return flag


if __name__ == '__main__':
    env = Maze()
    env.chooseIntensity()