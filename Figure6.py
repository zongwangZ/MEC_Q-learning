# -*- coding: utf-8 -*-
'''
@project:q_learning
@author:zongwangz
@time:19-6-24 上午6:24
@email:zongwang.zhang@outlook.com
'''
from run_this3 import *
parameter["taskNum"] = 3
parameter["intensity"] = 6
# max = 0
# for i in range(3000):
#     filename = "/home/zongwangz/PycharmProjects/q_learning/Figure3/table/Q_learning Table" + str((i+1)*10000)
#     wrong,sum = printConvergedState(filename)
#     print(sum, sum-wrong)
#     if sum-wrong > max:
#         time = calTime(filename)
#         print(i+1,time)
#     open("./figure6","a+").write(str(wrong)+","+str(sum)+"    "+str(time)+"\n")

def printLog():
    '''
    根据1000万次的实验log，输出状态变化和收敛情况。
    :return:
    '''
    filename = "/home/zongwangz/PycharmProjects/q_learning/result.txt"
    f = open(filename,"r")
    maxright = 0
    c = 0
    x = []
    y = []
    x_time = []
    y_time = []
    while True:
        line = f.readline()
        if line:
            item = ast.literal_eval(line)
            if isinstance(item,dict):
                c += 1
                result = item
                right = 0
                for key in result:
                    if result[key] == 1:
                        right += 1
                if right > maxright:
                    maxright = right
                    x.append(c)
                    y.append(right)
        else:
            break
    print(x,y)
    max = 0
    for i in range(len(y)):
        if y[i]>max:
            max = y[i]
            x_time.append(x[i])
            filename = "/home/zongwangz/PycharmProjects/q_learning/Figure3/table"+"/Q_learning Table" + str((x[i]) * 10000)
            print(x[i], y[i])
            y_time.append(calTime(filename))
    print(x_time,y_time)
    fig,ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(x,y,label="state")
    ax2.scatter(x_time,y_time,label="time")
    plt.show()

def plot():
    x1 = [1, 7, 14, 20, 112, 123, 132, 148, 183, 215, 216, 228, 246, 336, 447, 853, 1714, 1716,3000]
    x2 = [1, 7, 14, 20, 112, 123, 132, 148, 183, 215, 216, 228, 246, 336, 447, 853, 1714, 1716,3000]
    y2 = [365.9695, 251.275, 246.478, 182.1475, 91.6215, 91.189, 91.0145, 89.9225, 87.5825, 86.2395, 86.9475, 85.118,
          75.4505, 75.5365, 76.1735, 75.656, 74.4175, 75.506,75.8775]
    y1 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,23]
    # plt.subplots()
    plt.plot(x1,y1,"o-",linewidth=3.5,markersize=10)
    plt.xlabel("# episode",fontdict={'size':18})
    plt.ylabel("# converged state",fontdict={'size':18})
    plt.xlim((1,3001))
    # plt.annotate(s='37',xy=(2076,37),xytext=(2200,30),
    #              arrowprops={'arrowstyle':'->'})
    plt.show()
    plt.close()
    #
    max = 1000.451
    y2 = np.log10(y2) / np.log10(max)
    plt.subplots()
    plt.plot(x2, y2, "o-",linewidth=3.5,markersize=10)
    plt.xlabel("# episode", fontdict={'size': 18})
    plt.ylabel("consumed_time", fontdict={'size': 18})
    plt.xlim((1, 3001))
    # plt.annotate(s=str(round(y2[-1], 3)), xy=(2076, y2[-1]), xytext=(2500, y2[-1]),
    #              arrowprops={'arrowstyle': '->'})
    plt.show()
def why():
    status = {'[   0. 4500.    6.]': 1, '[   1. 4400.    4.]': 1, '[   3. 4300.    8.]': -1, '[   0. 4500.   10.]': -1,
     '[   1. 4300.    4.]': -1, '[   3. 4100.    6.]': 1, '[   0. 4500.    4.]': 1, '[   1. 4300.    8.]': 1,
     '[   3. 4200.    8.]': 1, '[   3. 4200.    4.]': 1, '[   3. 4200.    6.]': 1, '[   1. 4400.    6.]': 1,
     '[   1. 4300.    6.]': -1, '[   3. 4300.    4.]': 1, '[   1. 4400.    8.]': -1, '[   0. 4500.    8.]': -1,
     '[   1. 4300.   10.]': 1, '[   3. 4300.    6.]': 1, '[   3. 4000.    4.]': 1, '[   3. 4200.   10.]': 1,
     '[   1. 4400.   10.]': -1, '[   3. 4100.    4.]': 1, '[   3. 3900.    4.]': 1, '[   3. 4300.   10.]': -1,
     '[   3. 3900.    8.]': 1, '[   3. 4100.    8.]': 1, '[   3. 3900.   10.]': 1, '[   3. 3900.    6.]': 1,
     '[   1. 4100.    4.]': 1, '[   1. 4100.    6.]': 1, '[   3. 4100.   10.]': 1, '[   3. 4000.    6.]': -1,
     '[   3. 4000.   10.]': -1, '[   3. 4000.    8.]': -1, '[   1. 4100.    8.]': -1, '[   1. 4100.   10.]': -1,
     '[   3. 3700.    4.]': -1, '[   3. 3700.    6.]': -1, '[   3. 3700.    8.]': -1, '[   3. 3700.   10.]': -1}
    count = {'[   0. 4500.    6.]': [8726644, 7947764], '[   1. 4400.    4.]': [207659, 159969], '[   3. 4300.    8.]': [15321, 264], '[   0. 4500.   10.]': [2315254, 38328], '[   1. 4300.    4.]': [14916046, 249236], '[   3. 4100.    6.]': [210848, 158916], '[   0. 4500.    4.]': [15486982, 14198272], '[   1. 4300.    8.]': [5403533, 4678957], '[   3. 4200.    8.]': [3878343, 3555429], '[   3. 4200.    4.]': [10709222, 9764780], '[   3. 4200.    6.]': [6029283, 5486361], '[   1. 4400.    6.]': [116641, 106771], '[   1. 4300.    6.]': [8409335, 140575], '[   3. 4300.    4.]': [42683, 17568], '[   1. 4400.    8.]': [75150, 1260], '[   0. 4500.    8.]': [5611624, 94098], '[   1. 4300.   10.]': [2231717, 1924091], '[   3. 4300.    6.]': [24167, 22085], '[   3. 4000.    4.]': [39882, 6991], '[   3. 4200.   10.]': [1601671, 1467401], '[   1. 4400.   10.]': [31268, 547], '[   3. 4100.    4.]': [374338, 303723], '[   3. 3900.    4.]': [3292844, 2988261], '[   3. 4300.   10.]': [6269, 110], '[   3. 3900.    8.]': [1194300, 1073499], '[   3. 4100.    8.]': [135831, 110780], '[   3. 3900.   10.]': [492495, 439825], '[   3. 3900.    6.]': [1852272, 1667957], '[   1. 4100.    4.]': [90394, 36380], '[   1. 4100.    6.]': [51036, 46700], '[   3. 4100.   10.]': [55939, 37050], '[   3. 4000.    6.]': [22503, 365], '[   3. 4000.   10.]': [5890, 82], '[   3. 4000.    8.]': [14311, 251], '[   1. 4100.    8.]': [32642, 555], '[   1. 4100.   10.]': [13736, 248], '[   3. 3700.    4.]': [780, 18], '[   3. 3700.    6.]': [439, 13], '[   3. 3700.    8.]': [275, 3], '[   3. 3700.   10.]': [94, 1]}
    for item in status:
        if status[item] == -1:
            print(item,count[item],count[item][1]/count[item][0])
if __name__ == '__main__':
    # printLog()
    plot()
    # why()