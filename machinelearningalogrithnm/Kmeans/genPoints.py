import numpy as np
import matplotlib.pyplot as  plt
#
# (2,10)输出2×10个样本  ndarray类型
cluster1=np.random.uniform(0.5,1.5,(2,10))
cluster2=np.random.uniform(3.5,4.5,(2,10))

X=np.hstack((cluster1,cluster2)).T
# print(X)
# plt.figure()
# plt.axis([0,5,0,5])
# plt.grid(True)
# plt.plot(X[:,0],X[:,1],'k.')
# plt.show()

'''
------------------------------------------
'''

from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

K=range(1,10)
meandistortions=[]
for k in K:
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(X)
    meandistortions.append(sum(np.min(cdist(X,kmeans.cluster_centers_,'euclidean'),axis=1))/X.shape[0])
plt.plot(K,meandistortions,'bx-')
plt.xlabel('k')
plt.ylabel('Average distortion degree')
plt.title('The elbows rule is used to determine the best K value')
plt.show()
