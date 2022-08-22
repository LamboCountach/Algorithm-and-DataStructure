#迷宫问题

#给一个二维列表,表示迷宫(0表示通道,1表示围墙). 给出算法,求一条走出迷宫的最优路径

#方法:广度优先搜索
    #从一个节点开始,寻找所有接下来能继续走的点,继续不断寻找,直到找到出口
    #使用队列存储当前正在考虑的节点

    #我们需要一个列表存储路径中所有节点的坐标(x,y),并对每个节点增设一个变量index,用于表示这条路径中某个节点是由哪一个节点来引出,
    #起点的index是-1,其它节点的index则是在它前面一个节点在列表中的编号下标
    #这样组成的元组(x,y,index)在入队时使用
    #eg:存储路径的列表为[(1,1),(2,2),(2,3)],那么(1,1)的index是-1,(2,2)由(1,1)引出,所有(2,2),的index是(1,1)在列表的编号下标,即0。同理,(3,3)的下标是1

from collections import deque

maze= [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

#dirs表示根据一个节点的坐标(x,y),求出这个点在上、右、下、左四个点的坐标
dirs = [
    lambda x,y: (x,y+1), #上
    lambda x,y: (x+1,y), #右
    lambda x,y: (x,y-1), #下
    lambda x,y: (x-1,y)  #左
]

def print_r(path): #走到终点时print路径的方法
    curNode = path[-1] #走到终点时,path的最后一个元素就是curNode
    realPath = []

    while curNode[2] != -1:
        realPath.append((curNode[0],curNode[1]))
        curNode = path[curNode[2]]
    realPath.append((curNode[0],curNode[1])) #realPath append起点

    realPath.reverse()
    for node in realPath:
        print(node)


def maze_path_queue(x1,y1,x2,y2):
    queue = deque()
    queue.append((x1,y1,-1)) #起点入队  (注:queue中的元素是(x,y,index), path中的元素是(x,y))
    path = []
    while len(queue) > 0: #如果队空,一定没有路了
        curNode = queue.popleft() #当前节点是队首元素,而队首要出队,我们把当前节点存储到curNode这个变量中然后将curNode添加到path中
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True

        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0: #如果存在一个方向的节点能走
                queue.append((nextNode[0],nextNode[1],len(path)-1))  #引出nextNode的节点就是path中的最后一个元素,因此nextNode的index等于path中的最后一个元素的编号下标
                maze[nextNode[0]][nextNode[1]] = 2 #将走过的节点标记为2
                #由于深度优先找完一个能走的方向就不找了,而广度优先要探寻一个节点所有下一步能走的方向,所以此处不写break

            #注:
            # 如果一个方向的节点都走不了也没关系,程序会最终因为len(queue)不再大于0而跳出while循环,执行71-73行代码,说明这条路是死胡同
    else:
        print("没有路")
        return False

maze_path_queue(1,1,8,8)



