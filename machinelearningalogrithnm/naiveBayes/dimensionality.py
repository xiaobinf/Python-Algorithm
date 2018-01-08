from matplotlib import pyplot as plt
import numpy as np
"""
当有指数量级的参数 维度爆炸  各个维度的特征在类确定的情况下独立同分布
"""

max_dimensionality = 10
ax = plt.axes(xlim=(0, max_dimensionality), ylim=(0, 1 / (0.01 ** max_dimensionality)))
x = np.linspace(0, max_dimensionality, 1000)
y = 1 / (0.01 ** x)
plt.plot(x, y, lw=2)
plt.show()