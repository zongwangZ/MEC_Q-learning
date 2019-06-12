# -*- coding: utf-8 -*-
'''
@project:Edge Computing
@author:zongwangz
@time:19-4-30 上午10:00
@email:zongwang.zhang@outlook.com

crital path method
'''

import networkx as nx
import matplotlib.pyplot as plt

class CPM(nx.DiGraph):

    def __init__(self):
        super().__init__()
        self._dirty = True
        self._critical_path_length = -1
        self._criticalPath = None

    def add_node(self, *args, **kwargs):
        self._dirty = True
        super().add_node(*args, **kwargs)

    def add_nodes_from(self, *args, **kwargs):
        self._dirty = True
        super().add_nodes_from(*args, **kwargs)

    def add_edge(self, *args):  # , **kwargs):
        self._dirty = True
        super().add_edge(*args)  # , **kwargs)

    def add_edges_from(self, *args, **kwargs):
        self._dirty = True
        super().add_edges_from(*args, **kwargs)

    def remove_node(self, *args, **kwargs):
        self._dirty = True
        super().remove_node(*args, **kwargs)

    def remove_nodes_from(self, *args, **kwargs):
        self._dirty = True
        super().remove_nodes_from(*args, **kwargs)

    def remove_edge(self, *args):  # , **kwargs):
        self._dirty = True
        super().remove_edge(*args)  # , **kwargs)

    def remove_edges_from(self, *args, **kwargs):
        self._dirty = True
        super().remove_edges_from(*args, **kwargs)

        # 根据前向拓扑排序算弧的最早发生时间

    def _forward(self):
        for n in nx.topological_sort(self):
            es = max([self.node[j]['EF'] for j in self.predecessors(n)], default=0)
            self.add_node(n, ES=es, EF=es + self.node[n]['duration'])

            # 根据前向拓扑排序算弧的最迟发生时间

    def _backward(self):
        # for n in nx.topological_sort(self, reverse=True):
        for n in list(reversed(list(nx.topological_sort(self)))):
            lf = min([self.node[j]['LS'] for j in self.successors(n)], default=self._critical_path_length)
            self.add_node(n, LS=lf - self.node[n]['duration'], LF=lf)

            # 最早发生时间=最迟发生时间,则判断该节点为关键路径上的关键活动

    def _compute_critical_path(self):
        graph = set()
        for n in self:
            if self.node[n]['EF'] == self.node[n]['LF']:
                graph.add(n)
        self._criticalPath = self.subgraph(graph)

    @property
    def critical_path_length(self):
        if self._dirty:
            self._update()
        return self._critical_path_length

    @property
    def critical_path(self):
        if self._dirty:
            self._update()
        return sorted(self._criticalPath, key=lambda x: self.node[x]['ES'])

    def _update(self):
        self._forward()
        self._critical_path_length = max(nx.get_node_attributes(self, 'EF').values())
        self._backward()
        self._compute_critical_path()
        self._dirty = False


if __name__ == "__main__":
    # 构建graph
    G = CPM()
    G.add_node('A', duration=5)
    G.add_node('B', duration=2)
    G.add_node('C', duration=4)
    G.add_node('D', duration=4)
    G.add_node('E', duration=3)
    G.add_node('F', duration=7)
    G.add_node('G', duration=4)

    G.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('C', 'D'),
        ('C', 'E'),
        ('C', 'G'),
        ('B', 'D'),
        ('D', 'F'),
        ('E', 'F'),
        ('G', 'F'),
    ])

    # 显示graph
    nx.draw_spring(G, with_labels=True)
    plt.title('AOE网络')
    plt.axis('on')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    print('关键活动为:')
    print(G.critical_path_length, G.critical_path)

    G.add_node('D', duration=2)
    print('\n修改D活动持续时间4为2后的关键活动为:')
    print(G.critical_path_length, G.critical_path)