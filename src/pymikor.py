import math
import numpy as np


class Mikor:

    def __init__(self):
        self.dimS = 4
        self.dimN = 1
        self.nodesN = 100

    def set(self, dims, dimn, nodes):
        """
        Class Mikor
        :param dimS: Dimension of integral
        :param dimN: Dimension of result
        :return:
        """
        self.dimS = dims
        self.dimN = dimn
        self.nodesN = nodes

    def result(self):
        print('dimension of integration:', self.dimS)
        print('dimension of result     :', self.dimN)
        print('number of nodes         :', self.nodesN)
