# 训练集
# 每个样本点有3个分量 (x0,x1,x2)
x = [(1, 0., 3), (1, 1., 3), (1, 2., 3), (1, 3., 2), (1, 4., 4)]
# y[i] 样本点对应的输出
y = [95.364, 97.217205, 75.195834, 60.105519, 49.342380]



def gradientDescent(x,y,alpha=0.01,max_itor=1000,epsilon = 0.0001):
    '''

    :param x:训练集
    :param y: 训练集输出
    :param alpha: 步长
    :param max_itor: 最大迭代次数
    :param epsilon: 迭代阀值，当两次迭代损失函数之差小于该阀值时停止迭代
    :return:
    '''
    diff = [0, 0]
    error1 = 0
    error0 = 0
    cnt = 0
    m = len(x)

    # 初始化参数
    theta0 = 1
    theta1 = 1
    theta2 = 1

    while True:
        cnt += 1
        for i in range(m):
            # 计算误差
            diff[0] = (theta0 * x[i][0] + theta1 * x[i][1] + theta2 * x[i][2]) - y[i]
            print("diff[0]:", diff[0])
            # 计算梯度
            grad0 = diff[0] * x[i][0] / m
            grad1 = diff[0] * x[i][1] / m
            grad2 = diff[0] * x[i][2] / m
            # 更新theta
            theta0 -= alpha * grad0
            theta1 -= alpha * grad1
            theta2 -= alpha * grad2

        # 计算损失函数
        error1 = 0
        for i in range(m):
            error1 += (y[i] - (theta0 * x[i][0] + theta1 * x[i][1] + theta2 * x[i][2])) ** 2 / 2

        if abs(error0 - error1) < epsilon:
            break
        else:
            error0 = error1
        print(' theta0 : %.2f, theta1 : %.2f, theta2 : %.2f, error1 : %.2f' % (theta0, theta1, theta2, error1))
    print('Done: theta0 : %.2f, theta1 : %.2f, theta2 : %.2f' % (theta0, theta1, theta2))
    print('迭代次数: %d' % cnt)


gradientDescent(x,y,0.1)