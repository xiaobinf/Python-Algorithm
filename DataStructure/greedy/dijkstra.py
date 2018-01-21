import random
# dijkstra
# 参考了大话数据结构

def random_matrix_genetor(vex_num=10):
    '''
    随机图顶点矩阵生成器
    输入：顶点个数，即矩阵维数
    '''
    data_matrix=[]
    for i in range(vex_num):
        one_list=[]
        for j in range(vex_num):
            one_list.append(random.randint(1, 100))
        data_matrix.append(one_list)
    return data_matrix


data_matrix=[[0,10,1e9,30,100],
   [1e9,0,50,1e9,1e9],
   [1e9,1e9,0,1e9,10],
   [1e9,1e9,20,0,60],
   [1e9,1e9,1e9,1e9,0]]

def dijkstra(data_matrix,start_node):
    '''
    Dijkstra求解最短路径算法
    输入：原始数据矩阵，起始顶点
    输出；起始顶点到其他顶点的最短距离
    '''
    vex_num = len(data_matrix)
    flag_list = [False] * vex_num
    prev = [0] * vex_num
    dist = [1e9] * vex_num
    for i in range(vex_num):
        # 全部顶点初始化为未知最短路径状态
        flag_list[i] = False
        prev[i] = 0
        dist[i] = data_matrix[start_node][i]
    print('----------------------------------------------------')
    print('init flag[]:',flag_list)
    print('init prev[]:',prev)
    print('init dist[]:',dist)
    # v0 to v0 不需要求最短路径
    flag_list[start_node] = True
    dist[start_node] = 0

    k = 0
    # 主循环 每次求得start_node到某个顶点的最短距离 也即确定了一个dist[i],标记了一个flag为True
    for i in range(1, vex_num):
        min_value = 1e9
        for j in range(vex_num):
            if flag_list[j] == False and dist[j] < min_value :
                min_value = dist[j]
                k = j
        print(min_value,k)
        flag_list[k] = True
        # 修正当前最短路径以及距离
        for j in range(vex_num):
            if flag_list[j] == False and ( min_value + data_matrix[k][j] ) < dist[j]:
                dist[j] = min_value + data_matrix[k][j]
                print('k:',k,'j:',j)
                prev[j] = k

    for i in range(vex_num):
        print('顶点' + str(start_node) + '到顶点' + str(i) + '最短距离是--->' + str(dist[i]))
        print('最短路径为:',dijkstra_path(prev,start_node,i))

def dijkstra_path(prev,start_node,end_node):
    '''
    由prev回溯找到路径
    :param prev:
    :param start_node:开始节点
    :param end_node: 末尾节点
    :return: 路径
    '''
    path=list()
    path.append(end_node)
    while prev[end_node]!=0:
        path.append(prev[end_node])
        end_node=prev[end_node]
    path.append(start_node)
    return path[::-1]





dijkstra(data_matrix,0)

# print(random_matrix_genetor())


