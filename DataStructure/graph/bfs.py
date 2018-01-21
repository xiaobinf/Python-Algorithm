from collections import deque
# define the graph
graph={}
graph[0]=[1,3]
graph[2]=[0,4,3]
graph[3]=[4]
graph[1]=[0,2]
graph[4]=[]
def bfs_1():
    '''
    通过字典构建图模型，实现广度遍历  进栈出栈顺序
    searched[]用于防止两个节点拥有同一个字节点，重复遍历
    :return:
    '''
    search_deque=deque()
    search_deque+=graph[0]
    searched=[]
    print(0)
    searched.append(0)
    while search_deque:
        node=search_deque.popleft()
        if not node in searched:
            print(node)
            search_deque+=graph[node]
            searched.append(node)
bfs_1()

