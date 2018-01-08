import unittest
import numpy as np
# from .. import *
# from . import HiddenMarkovModels
from HiddenMarkovModels import HMM

A=np.mat([[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]])
B=np.mat([[0.5,0.5],[0.4,0.6],[0.7,0.3]])
pi=(0.2,0.4,0.4)
# test代码
class TestHMM(unittest.TestCase):
    '''
    针对HMM类的测试
    '''
    def setUp(self):
        self.tclass=HMM(A,B,pi)

    def test_observation_prob(self):

        pass

    def test_build_viterbi_path(self):
        self.assertEqual(self.tclass.observation_prob([0,1,0]),0.130218)

    def test_baum_welch_train(self):
        pass

unittest.main()