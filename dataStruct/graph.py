"""
邻接矩阵、邻接表表示的图
"""

from dataStruct.abstract import Graph
from dataStruct.singleLinkList import SingleLinkList


class MatrixGraph(Graph):
    """
    邻接矩阵表示的图
    """

    def __init__(self, node_set: list, adjacent_matrix: list):
        super(MatrixGraph, self).__init__()

        self.data = node_set
        self._adjacent = adjacent_matrix

    def _DFS(self, i, visited, res: list):
        visited[i] = 1
        res.append(self.data[i])

        for j in range(len(self.data)):
            if self.adjacent[i][j] != 0 and visited[j] == 0:
                res += self._DFS(j, visited, [])

        return res

    def DFSTraverse(self, start) -> list:
        return self._DFS(start, [0]*len(self.data), [])

    def BFSTraverse(self, start) -> list:
        visited = [0] * len(self.data)
        queue = list()
        res = list()

        res.append(self.data[start])
        visited[start] = 1
        vec = self.adjacent[start]

        for i in range(len(self.data)):

            for idx, item in enumerate(vec):
                if item != 0 and visited[idx] == 0:
                    res.append(self.data[idx])
                    queue.append(idx)
                    visited[idx] = 1

            if queue:
                vec = self.adjacent[queue.pop(0)]
            else:
                break

        return res

class AdjacentLinkList:
    """
    依据邻接矩阵生产的邻接表
    """
    def __init__(self, adjacent_matrix):
        super(AdjacentLinkList, self).__init__()

        self._adj_link_list = list()

        for ajd_vec in adjacent_matrix:

            link_list = SingleLinkList()
            for idx, edge in enumerate(ajd_vec):
                if edge != 0:
                    link_list.addAtTail(idx)

            self._adj_link_list.append(link_list)

    @property
    def adj_link_list(self):
        return self._adj_link_list

class LinkListGraph(Graph):
    """
    邻接表表示的图
    """

    def __init__(self, node_set: list, adjacent_matrix: list):
        super(LinkListGraph, self).__init__()

        self.data = node_set
        self._adjacent = AdjacentLinkList(adjacent_matrix).adj_link_list

    def _DFS(self, i, visited, res: list):
        visited[i] = 1
        res.append(self.data[i])

        link = self.adjacent[i]
        current = link.head.next
        while current:
            if visited[current.val] == 0:
                res += self._DFS(current.val, visited, [])

            current = current.next

        return res

    def DFSTraverse(self, start) -> list:
        return self._DFS(start, [0]*len(self.data), [])

    def BFSTraverse(self, start) -> list:
        visited = [0] * len(self.data)
        queue = list()
        res = list()

        res.append(self.data[start])
        visited[start] = 1
        vec = self.adjacent[start]

        for i in range(len(self.data)):

            current = vec.head.next
            while current:

                idx = current.val
                if visited[idx] == 0:
                    res.append(self.data[idx])
                    queue.append(idx)
                    visited[idx] = 1

                current = current.next

            if queue:
                vec = self.adjacent[queue.pop(0)]
            else:
                break

        return res