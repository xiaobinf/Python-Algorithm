import numpy as np
class HMM:
    """
    Order 1 Hidden Markov Model
    Attributes
    ----------
    A : numpy.ndarray
        State transition probability matrix
    B: numpy.ndarray
        Output emission probability matrix with shape(N, number of output types)
    pi: numpy.ndarray
        Initial state probablity vector
    Common Variables
    ----------------
    obs_seq : list of int
        list of observations (represented as ints corresponding to output
        indexes in B) in order of appearance
    T : int
        number of observations in an observation sequence
    N : int
        number of states
    """

    def __init__(self, A, B, pi):
        self.A = A
        self.B = B
        self.pi = pi

    def _forward(self,obs_seq):
        '''
        HMM前向算法 统计学习方法10.2
        :param obs_seq:
        :return:返回概率数组  见图_forward.png
        '''
        N=self.A.shape[0]
        T=len(obs_seq)

        F=np.zeros((T,N))
        # (1)初值
        for i in range(N):
            F[0,i]=self.pi[i]*self.B[i,obs_seq[0]]
        for i in range(1,T):
            for j in range(N):
                F[i,j]=np.dot(F[i-1,:],self.A[:,j])*self.B[j,obs_seq[i]]
        print(F)
        return F

    def observation_prob(self, obs_seq):
        """ P( entire observation sequence | A, B, pi )
        计算概率
        """
        return np.sum(self._forward(obs_seq)[-1,:])


    def _backward(self,obs_seq):
        '''
        后向算法 完全与书上完全相同
        :param obs_seq:
        :return:
        '''
        N=self.A.shape[0]
        T=len(obs_seq)
        X=np.zeros((T,N))
        X[-1,:]=1
        for t in range(T-2,-1,-1):
            for i in range(N):
                # 完全参考公式（10.20）
                X[t,i]=np.sum([self.A[i,j]*X[t+1,j]*self.B[j,obs_seq[t+1]] for j in range(N)])
        return X
        # 统计学习方法 10.3 (3)
        # print('X',X)
        # # 公式（10.23）
        # prob=np.sum([self.pi[i]*self.B[i,obs_seq[0]]*X[0,i] for i in range(N)])
        # return prob


    def _viterbi(self, obs_seq):
        '''
        返回两个中间矩阵
        :param obs_seq:观测序列
        :return:
        '''
        N = self.A.shape[0]
        T = len(obs_seq)
        V = np.zeros((T, N))
        D=np.zeros((T,N),dtype=int)
        for i in range(N):
            V[0][i]=self.pi[i]*self.B[:,obs_seq[0]][i]
        for t in range(1, T):
            for k in range(N):
                V[t][k]=max([V[t-1][i]*self.A[:,k][i] for i in range(N)])*self.B[k,obs_seq[t]]
                D[t][k]=np.argmax([V[t-1][i]*self.A[:,k][i] for i in range(N)])
        return V, D

    def build_viterbi_path(self,obs_seq):
        """
        Returns
        path : list(int)
            Optimal state path for the observation sequence
        """
        V,D=self._viterbi(obs_seq)
        T=len(V[:,0])
        prev = [0] * T
        prev[T-1]=np.argmax(V[T-1])
        for i in range(T-2,-1,-1):
            prev[i]=D[i+1][prev[T-1]]
        return prev

    def baum_welch_train(self, obs_seq):
        N = self.A.shape[0]
        T = len(obs_seq)

        forw = self._forward(obs_seq)
        back = self._backward(obs_seq)

        # P( entire observation sequence | A, B, pi )
        obs_prob = np.sum(forw[:,-1])
        if obs_prob <= 0:
            raise ValueError("P(O | lambda) = 0. Cannot optimize!")

        xi = np.zeros((T-1, N, N))
        for t in range(xi.shape[0]):
            xi[t,:,:] = self.A * forw[:,[t]] * self.B[:,obs_seq[t+1]] * back[:, t+1] / obs_prob

        gamma = forw * back / obs_prob

        # Gamma sum excluding last column
        gamma_sum_A = np.sum(gamma[:,:-1], axis=1, keepdims=True)
        # Vector of binary values indicating whether a row in gamma_sum is 0.
        # If a gamma_sum row is 0, save old rows on update
        rows_to_keep_A =  (gamma_sum_A == 0)
        # Convert all 0s to 1s to avoid division by zero
        gamma_sum_A[gamma_sum_A == 0] = 1.
        next_A = np.sum(xi, axis=0) / gamma_sum_A


        gamma_sum_B = np.sum(gamma, axis=1, keepdims=True)
        rows_to_keep_B = (gamma_sum_B == 0)
        gamma_sum_B[gamma_sum_B == 0] = 1.

        obs_mat = np.zeros((T, self.B.shape[1]))
        obs_mat[range(T),obs_seq] = 1
        next_B = np.dot(gamma, obs_mat) / gamma_sum_B

        # Update model
        self.A = self.A * rows_to_keep_A + next_A
        self.B = self.B * rows_to_keep_B + next_B
        self.pi = gamma[:,0] / np.sum(gamma[:,0])

# HMM参数定义  该测试用例取自维基百科:维特比算法
# states = ('Healthy', 'Fever')
#
# observations = ('normal', 'cold', 'dizzy')
#
# start_probability = {'Healthy': 0.6, 'Fever': 0.4}
#
# transition_probability = {
#     'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
#     'Fever': {'Healthy': 0.4, 'Fever': 0.6},
# }
#
# emission_probability = {
#     'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
#     'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
# }
# observations = ('normal', 'cold', 'dizzy')
#
# A=np.mat([[0.7,0.3],[0.4,0.6]])
# B=np.mat([[0.5,0.4,0.1],[0.1,0.3,0.6]])
# pi=[0.6,0.4]


# A=np.mat([[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]])
# B=np.mat([[0.5,0.5],[0.4,0.6],[0.7,0.3]])
# print(np.shape(B))
# pi=[0.2,0.4,0.4]

# hmm=HMM(A,B,pi)
# obs_seq=[0,1,2]
# V,D=hmm.viterbi(obs_seq)
# print(V,D)
# prev=hmm.build_viterbi_path(V,D)
# out=list()
# for i in prev:
#     if i == 0:
#         out.append('Healthy')
#     else:
#         out.append('Fever')
#         out.append('Fever')
#
# print("观察序列：[0,1,2,2,2,1,1,0,0,0]")
# print("隐藏序列："+str(out))


# 该测试用例取自统计学习方法 例10.2  由观察序列计算前向概率
A=np.mat([[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]])
B=np.mat([[0.5,0.5],[0.4,0.6],[0.7,0.3]])
pi=(0.2,0.4,0.4)
hmm=HMM(A,B,pi)
print(hmm.observation_prob([0,1,0]))
print(hmm.build_viterbi_path([0,1,0]))
# print(hmm.backward_1([0,1,0]))
# print(hmm.backward([0,1,0]))



