#                                       E
#                                    /     \
#                                   /       \
#                                  /         \
#                                 A           G
#                                  \           \
#                                   \           \
#                                    C           F
#                                   /  \
#                                  B    D



class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

a = BinaryTreeNode("A")
b = BinaryTreeNode("B")
c = BinaryTreeNode("C")
d = BinaryTreeNode("D")
e = BinaryTreeNode("E")
f = BinaryTreeNode("F")
g = BinaryTreeNode("G")

e.lchild = a
e.rchild = g
g.rchild = f
a.rchild = c
c.lchild = b
c.rchild = d

root = e

#二叉树的遍历
#依然使用顶上的例子:
# 前序遍历:EACBDGF
# 中序遍历:ABCDEGF
# 后序遍历:BDCAFGE
# 层次遍历:EAGCFBD

#已知二叉树前/中/后序遍历的结果中的任意两个,我们都能画出这个完整的二叉树

#前序遍历
def pre_order(root):
    if root != None:
        print(root.data, end = " ")
        pre_order(root.lchild)
        pre_order(root.rchild)

#中序遍历
def in_order(root):
    if root != None:
        in_order(root.lchild)
        print(root.data, end=" ")
        in_order(root.rchild)

#后序遍历
def post_order(root):
    if root != None:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=" ")

#层次遍历(使用队列来实现)
from collections import deque
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0: #只要队不空
        node = queue.popleft()
        print(node.data, end = " ")
        if node.lchild != None:
            queue.append(node.lchild)
        if node.rchild != None:
            queue.append(node.rchild)

level_order(e)








