#二叉搜索树
#定义:二叉搜索树是一棵二叉树且满足性质:设x是一个二叉搜索树的一个节点。如果y是x左子树的一个节点,那么y.data ≤ x.data。如果y是x右子树的一个节点,那么y.data ≥ x.data。
#eg:
#                                      17
#                                    /     \
#                                   /       \
#                                  /         \
#                                 /           \
#                                5            35
#                              /   \         /  \
#                             /     \       /    \
#                            /       \     /      \
#                           2        11   29      38
#                                   /
#                                  /
#                                 9
#                                /
#                               8


class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST:
    def __init__(self,li):
        self.root = None
        if li != None:
            for val in li:
                self.insert_using_loop(val)

#插入操作
    def insert_using_recursion(self,node,val):
        if node == None: #最开始的时候node就是self.root
            self.root = BinaryTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert_using_recursion(node.lchild,val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert_using_recursion(node.rchild, val)
            node.rchild.parent = node
        #不用考虑val=node.data的情况

        return node

    def insert_using_loop(self,val):
        p = self.root
        if p == None:
            self.root = BinaryTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild != None: #如果p有左孩子
                    p = p.lchild #将p赋值为p的左孩子,用于判断p左孩子的data和val的大小关系
                else: #如果p没有左孩子
                    p.lchild = BinaryTreeNode(val) #让data为val的二叉树节点成为p的左节点
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild != None:
                    p = p.rchild
                else:
                    p.rchild = BinaryTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

#查询操作
    def search_using_recursion(self,node,val):
        if node == None: #最开始的时候node就是self.root
            return None
        else:
            if val < node.data:
                return self.search_using_recursion(self.lchild,val)
            elif val > node.data:
                return self.search_using_recursion(self.rchild,val)
            else:
                return node

    def search_using_loop(self,val):
        p = self.root
        if p == None:
            return None
        while p != None:
            if val < p.data:
                p = p.lchild
            elif val > p.data:
                p = p.rchild
            else: # if val == p.data
                return p




#删除操作
#删除分3种情况:
# 1)如果要删除节点是一个叶节点: 直接删除
# 2)如果要删除节点只有1个孩子:将此节点的孩子与父节点连接 (如果被删除节点是根节点且根节点只有1个孩子，要注意将树的root变为这个根节点的子节点)
# 3)如果要删除的节点有两个孩子:将其右子树的最小节点(该节点最多有一个右孩子)删除,并用该节点替换被删除节点
#eg:
#                                 (删除5这个节点)
#                                      17                                                                     17
#                                    /     \                                                                 /  \
#                                   /       \                                                               /    \
#                                  /         \                                                             /      \
#                                 /           \                                                           /        \
#                                /             \                                                         /          \
#                                5             35                ------------------>                    7           35
#                              /   \          /  \                                                     / \         /  \
#                             /     \        /    \                                                   /   \       /    \
#                            /       \      /      \                                                 /     \     /      \
#                           /         \    /        \                                               /       \   /        \
#                          2          11  29        38                                             2        11 29         38
#                                    /  \                                                                  /  \
#                                   /    \                                                                /    \
#                                  9      16                                                             9      16
#                                 /                                                                       \
#                                7                                                                         8
#                                 \
#                                  8
#                       (7是5的右子树上最小的节点)

    #如果被删除的是叶节点
    def remove_node_1(self,node):#node是被删除节点
        if node.parent == None: #如果node是根节点
            self.root = None
        elif node.parent.lchild == node: #如果node是其父节点的左节点
            node.parent.lchild = None
        elif node.parent.rchild == node: #如果node是其父节点的右节点
            node.parent.rchild = None

    #如果被删除的节点只有一个左子节点
    def remove_node_21(self,node): #node是被删除节点
        if node.parent == None:   #如果node是根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:#如果node是其父节点的左子节点
                node.parent.lchild = node.lchild
                node.lchild.parent = node.parent
        else:#如果node是其父节点的右子节点
                node.parent.rchild = node.lchild
                node.lchild.parent = node.parent

    # 如果被删除的节点只有一个右子节点
    def remove_node_22(self, node):  # node是被删除节点
        if node.parent==None:  # 如果node是根节点
            self.root = node.rchild
            node.rchild.parent = None
        elif node==node.parent.lchild:  # 如果node是其父节点的左子节点
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:  # 如果node是其父节点的右子节点
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent



    def delete(self, val):
        if self.root != None: #如果不是空树
            node = self.search_using_loop(val) #找到被删除节点
            if node == None: #如果被删除节点不存在
                return False
            if node.lchild == None and node.rchild == None:
                self.remove_node_1(node)
            elif node.lchild != None and node.rchild == None:
                self.remove_node_21(node)
            elif node.lchild == None and node.rchild != None:
                self.remove_node_22(node)
            else:#被删除节点既有左子节点又有右子节点
                min_node = node.rchild
                while min_node.lchild != None: #我们要找到被删除节点右子树的最小节点(该节点最多有一个右孩子)
                    min_node = min_node.rchild
                #删除min_node并用它替换被删除节点
                node.data = min_node.data #替换

                #删除
                if min_node.rchild != None: #如果min_node有右子节点
                    self.remove_node_22(min_node)
                else:#如果min_node没有右子节点
                    self.remove_node_1(min_node)



    def in_order(self,root):
        if root != None:
            self.in_order(root.lchild)
            print(root.data, end=" ")
            self.in_order(root.rchild)

    def pre_order(self,root):
        if root!=None:
            print(root.data, end=" ")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

# li = [1,4,2,5,3,7,6,8,9]
# tree = BST(li)
# for i in li:
#     tree.insert_using_loop(i)
# tree.in_order(tree.root)
# print("")
#
# tree.delete(4)
# tree.delete(1)
# tree.delete(8)
# tree.in_order(tree.root)



