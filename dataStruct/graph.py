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

    def _DFS(self, visited):
        pass

    def DFSTraverse(self) -> list:
        pass

    def _BFS(self):
        pass

    def BFSTraverse(self) -> list:
        pass

class AdjacentLinkList:
    """
    依据邻接矩阵生产的邻接表
    """
    def __init__(self, adjacent_matrix):
        super(AdjacentLinkList, self).__init__()

        self._adj_link_list = list()

        for ajd_vec in adjacent_matrix:

            link_list = SingleLinkList()
            for edge in ajd_vec:
                if edge != 0:
                    link_list.addAtTail(edge)

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

    def _DFS(self):
        pass

    def DFSTraverse(self) -> list:
        pass

    def _BFS(self):
        pass

    def BFSTraverse(self) -> list:
        pass