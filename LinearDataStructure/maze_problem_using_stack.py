#迷宫问题

#给一个二维列表,表示迷宫(0表示通道,1表示围墙). 给出算法,求一条走出迷宫的路径

#方法:深度优先搜索(回溯法)
    #从一个节点开始,依次查看它的上、右、下、左四个节点能不能走(不是墙而且没有走过的节点定义为能走的节点),当一个节点4个方向都不能走时,退回至该节点的上一个点,寻找它的另外3个方向能不能走
    #使用栈存储当前路径

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
#实现:
def maze_path(x1,y1,x2,y2): #(x1,y1)是起点坐标,(x2,y2)是终点坐标
    stack = []
    stack.append((x1,y1)) #stack存储的是长度为2的元组
    while (len(stack) > 0):
        curNode = stack[-1] #stack的最后一个元素就是当前所在的节点
        if curNode[0] == x2 and curNode[1] == y2:#如果有路通往终点
            for p in stack:
                print(p)
            return True

        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])  #curNode[0]是curNode的x坐标, curNode[1]是curNode的y坐标
            if maze[nextNode[0]][nextNode[1]] == 0: #如果存在一个方向的节点能走
                stack.append(nextNode) #将nextNode append进stack,使它成为下一步时的curNode
                maze[nextNode[0]][nextNode[1]] = 2 #将走过的节点标记为2
                break
        else:#如果curNode的四个方向都走不通的话
            stack.pop() #回退到curNode之前所在的一个节点
    else:
        print("没有路通往终点")
        return False

maze_path(1,1,8,8)

