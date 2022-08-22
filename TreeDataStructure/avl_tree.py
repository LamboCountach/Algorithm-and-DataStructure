#二叉搜索树的效率:
#平均情况下,二叉搜索树搜索的时间是O(logn)
#最坏情况下,二叉树可能非常倾斜(搜索时间为O(n))
#eg:
     # 10
     #   \
     #   20
     #     \
     #      30
     #       \
     #        40
     #          \
     #           50

#AVL树:
#AVL树是一棵自平衡的二叉搜索树
#AVL树具有以下性质:
    #一个节点的左右子树高度之差的绝对值不超过1
    #根的左右子树都是平衡二叉树
    #balance factor定义: 一个节点的右子树的高度减去该节点左子树的高度的值

#eg:(注:括号内的值是该节点的balance factor)
#                                     25(0)
#                                    /     \
#                                   /       \
#                                  /         \
#                                 /           \
#                                20(-1)       36(0)
#                               /  \          /  \
#                              /    \        /    \
#                             /      \      /      \
#                           10(1)    22(0) 30(-1)  40(0)
#                             \           /       /   \
#                              12(0)     28(0)   38(0) 48(0)
#
#
#

#初始化AVL树
from binary_search_tree import BinaryTreeNode, BST

class AVLNode(BinaryTreeNode):
    def __init__(self,data):
        BinaryTreeNode.__init__(self,data)
        self.bf = 0    #AVL节点初始化时balance factor为0

class AVLTree(BST):
    def __init__(self,li):
        BST.__init__(self,li)




#AVL树 -- 插入
##插入一个节点可能破坏AVL树的平衡, 可以通过旋转操作来进行修正
#插入一个节点后,只有从插入节点到根节点的路径上的节点的平衡可能被改变。我们需要找出第一个破坏了平衡条件的节点,称之为K。K的左右子树的高度之差为2(不可能为3)

#不平衡的出现可能有4种情况:
# (1)不平衡是由于对K的右孩子的右子树插入导致的: 我们进行左旋操作
#     eg:
#         插入前:    p                           插入后:     p                                                  左旋后:           c
#                 /   \                                  /   \                                                               /   \
#                s1    c                                s1    c                                                             p    s3
#                    /   \                                  /   \                                                         /   \
#                   s2   s3                                s2   s3                                                       s1   s2
#         (设此时s1,s2,s3的高度都是h,此时树平衡)    (新节点被插入在s3上,s1,s2的高度仍为h,s3高度变为h+1,此时树不平衡)

    def left_rotation(self,p,c):
        s2 = c.lchild
        p.rchild = s2
        if s2 != None:
            s2.parent = p

        c.lchild = p
        p.parent = c

    #p,c的balance factor要改变
        p.bf = 0
        c.bf = 0

        return c   #return这棵树的根节点的bf  (注:这棵树的根节点是K(即在插入操作后第一个被破坏了平衡条件的节点),它不一定是整个树的根节点!)


# (2)不平衡是由于对K的左孩子的左子树插入导致的: 我们进行右旋操作
#         插入前:    p                           插入后:     p                                                  左旋后:           c
#                 /   \                                  /   \                                                               /   \
#                c    s3                                c     s3                                                            s1    p
#              /   \                                  /   \                                                                     /   \
#             s1   s2                                s1   s2                                                                   s2    s3
#         (设此时s1,s2,s3的高度都是h,此时树平衡)    (新节点被插入在s1上,s2,s3的高度仍为h,s1高度变为h+1,此时树不平衡)
    def right_rotation(self,p,c):
        s2 = c.rchild
        p.lchild = s2
        if s2 != None:
            s2.parent = p

        c.rchild = p
        p.parent = c

        # 更新balance factor
        p.bf = 0
        c.bf = 0

        return c  # return这棵树的根节点的bf (注:这棵树的根节点是K(即在插入操作后第一个被破坏了平衡条件的节点),它不一定是整个树的根节点!)


# (3)不平衡是由于对K的右孩子的左子树插入导致的: 我们先进行右旋操作,再进行左旋操作
#     插入前:     p
#              /   \
#             /     \
#            s1      c
#                   / \
#                  g   s4
#                 / \
#                /   \
#              s2     s3
#     (设s1,s4高度为h,s2,s3高度为h-1)
#
#     插入后分3种情况:
#     1)新节点被插入在s2上:                           2)新节点被插入在s3上:                         3)s1,s2,s3,s4均为None,新插入的这个节点实际上就是g:
#                p                                                p                                                                p
#              /   \                                            /   \                                                               \
#             /     \                                          /     \                                                               \
#            s1      c                                        s1      c                                                               c
#                   / \                                              / \                                                             /
#                  g   s4                                           g   s4                                                          g
#                 / \                                              / \
#                /   \                                            /   \
#              s2     s3                                         s2   s3
#     (此时s1,s4高度仍为h,s3高度仍为h-1,s2高度变为h,此时树不平衡)    (此时s1,s4高度仍为h,s2高度仍为h-1,s3高度变为h,此时树不平衡)           (此时树不平衡)
#
#
#     先右旋再左旋后:                                  先右旋再左旋后:                                                      先右旋再左旋后:
#                g                                                g                                                               g
#              /   \                                            /   \                                                           /   \
#             /     \                                          /     \                                                         /     \
#            p       c                                        p       c                                                       p       c
#           / \     /  \                                     / \     / \
#         s1   s2  s3  s4                                   s1  s2  s3  s4

    def rotate_right_left(self,p,c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3 != None:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2 != None:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 更新balance factor
        if g.bf < 0:     #新节点被插入在s2上
            p.bf = 0
            c.bf = 1
        elif g.bf > 0:   #新节点被插入在s3上
            p.bf = -1
            c.bf = 0
        else: #新插入节点是g
            p.bf = 0
            c.bf = 0
        g.bf = 0

        return g  # return这棵树的根节点的bf (注:这棵树的根节点是K(即在插入操作后第一个被破坏了平衡条件的节点),它不一定是整个树的根节点!)

# (4)不平衡是由于对K的左孩子的右子树插入导致的: 我们先进行左旋操作,再进行右旋操作
#     插入前:     p
#              /   \
#             /     \
#            c       s4
#           / \
#          s1  g
#             / \
#            /   \
#           s2    s3
#     (设s1,s4高度为h,s2,s3高度为h-1)
#
#     插入后分3种情况:
#     1)新节点被插入在s2上:                           2)新节点被插入在s3上:                         3)s1,s2,s3,s4均为None,新插入的这个节点实际上就是g:
#                p                                                p                                                                p
#              /   \                                            /   \                                                             /
#             /     \                                          /     \                                                           /
#            c      s4                                        c       s4                                                        c
#           / \                                              / \                                                                 \
#          s1  g                                           s1   g                                                                 g
#             / \                                              / \
#            /   \                                            /   \
#           s2    s3                                         s2   s3
#     (此时s1,s4高度仍为h,s3高度仍为h-1,s2高度变为h,此时树不平衡)    (此时s1,s4高度仍为h,s2高度仍为h-1,s3高度变为h,此时树不平衡)           (此时树不平衡)
#
#
#     先右旋再左旋后:                                  先右旋再左旋后:                                                      先右旋再左旋后:
#                g                                                g                                                               g
#              /   \                                            /   \                                                           /   \
#             /     \                                          /     \                                                         /     \
#            c       p                                        c       p                                                       c       p
#           / \     /  \                                     / \     / \
#         s1   s2  s3  s4                                   s1  s2  s3  s4

    def rotate_left_right(self,p,c):
        g = c.rchild

        s2=g.lchild
        c.rchild = s2
        if s2 != None:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3 != None:
            s3.parent = p
        g.rchild = p
        p.parent = g

        #更新bf:
        if g.bf < 0:   #新节点被插入在s2上
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:  #新节点被插入在s3上
            p.bf = 0
            c.bf = -1
        else: #新插入节点是g
            p.bf = 0
            c.bf = 0
        g.bf = 0

        return g  # return这棵树的根节点的bf (注:这棵树的根节点是K(即在插入操作后第一个被破坏了平衡条件的节点),它不一定是整个树的根节点!)




    def insert_using_loop(self,val):

        p = self.root
        if p == None:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild != None:  # 如果p有左孩子
                    p = p.lchild  # 将p赋值为p的左孩子,用于判断p左孩子的data和val的大小关系
                else:  # 如果p没有左孩子
                    p.lchild = AVLNode(val)  # 让data为val的二叉树节点成为p的左节点
                    p.lchild.parent = p
                    node = p.lchild  # node存储的就是被插入的新节点
                    break
            elif val > p.data:
                if p.rchild!=None:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild  # node存储的就是被插入的新节点
                    break
            else: #val == p.data #AVL尽量不允许两个有相同data的节点存在
                return

        #对balance factor进行更新

        #思路: 对于被插入节点的父节点一直到这棵树的根节点的这条路径上的节点,如果存在一个节点A的balance factor在新节点被插入后变为0,
        #     那么从A的父节点开始一直到根节点,这些节点的balance factor都不需要被改变。而从被插入节点的父节点开始一直到A的子节点,这些节点的balance factor都需要被改变。
        #     对于在被插入节点的父节点开始一直到A的子节点的这条路径上的节点,
        #     如果它的balance factor在插入前为1,插入后会变为2; 如果它的balance factor在插入前为-1,插入后会变为-2

        #     反之,如果不存在这个A,那么从被插入节点的父节点开始一直到根节点的balance factor都要改变



        # 注意:1)如果被插入节点成为了它的parent的左子节点,那么在进入285行的循环之后,
        #        它实际上只会遇到node.parent.bf>0(297行)和node.parent.bf == 0(301行)这两种情况,不会遇到node.parent.bf < 0(287行)这种情况,
        #        只有node.parent以及它之后的节点才可能会遇到node.parent.bf < 0的情况
        
        #     2)如果被插入节点成为了它的parent的右子节点,那么在进入285行的循环之后,
        #        它实际上只会遇到node.parent.bf<0(319行)和node.parent.bf == 0(323行)这两种情况,不会遇到node.parent.bf > 0(308行)这种情况,
        #        只有node.parent以及它之后的节点才可能会遇到node.parent.bf > 0的情况

        while node.parent != None:     #node.parent不为空(即循环从被插入节点开始,一直到这棵树的根节点的孩子)
            if node.parent.lchild == node: #被插入节点成为了它的parent的左子节点。如果存在A的话,那么从被插入节点的parent开始一直到A的balance factor都要-=1。如果不存在A,那么从被插入节点的parent一直到根节点的孩子的balance factor都要-=1
                if node.parent.bf < 0: #插入前node.parent = -1,插入后应当变为-2 (但此时node.parent的平衡被破坏,需要进行旋转操作进行调整)
                    head = node.parent.parent
                    tmp = node.parent  # 这里的head和tmp用于后续的连接操作, tmp表示旋转操作之前的这棵树的根
                    # n 是旋转后这棵树的根
                    if node.bf > 0:#插入前node.bf = 0, 插入后已经变为了 1
                        n = self.rotate_left_right(node.parent,node)  #这实际上相当于让被插入节点成为node.parent的左子节点的右子节点后的旋转操作
                    else:#插入前node.bf = 0, 插入后已经变为了 -1
                        n = self.right_rotation(node.parent,node)  #这实际上相当于让新节点成为node.parent的左子节点的左子节点后的旋转操作
                    #(注:不会存在插入后node.bf = 0的情况，因为如果node.bf在插入后变为0,则node.parent.bf在插入操作后一定不会变)

                elif node.parent.bf > 0: #插入前node.parent.bf = 1,插入后应当变为0(这个node.parent实际上就是我们在找的A)
                    node.parent.bf = 0
                    break

                else: #node.parent.bf == 0
                    #插入前node.parent.bf = 0,插入后应当变为-1
                    node.parent.bf = -1
                    node = node.parent
                    continue

            else:  #被插入节点成为了它的parent的右子节点。如果存在A的话,那么从被插入节点的parent开始一直到A的balance factor都要+=1。如果不存在A,那么从被插入节点的parent一直到根节点的孩子的balance factor都要+=1
                if node.parent.bf > 0: #插入前node.parent = 1,插入后应当变为2 (但此时node.parent的平衡被破坏,需要进行旋转操作进行调整)
                    head = node.parent.parent  #
                    tmp = node.parent         # 这里的head和tmp用于后续的连接操作, tmp表示旋转操作之前的这棵树的根
                    # n 是旋转后这棵树的根
                    if node.bf < 0:   #插入前node.bf = 0, 插入后已经变为了 -1
                        n = self.rotate_right_left(node.parent,node) #这实际上相当于让被插入节点成为node.parent的右子节点的左子节点后的旋转操作
                    else: #插入前node.bf = 0, 插入后已经变为了 1
                        n = self.left_rotation(node.parent,node)   #这实际上相当于让被插入节点成为node.parent的右子节点的右子节点后的旋转操作
                    #(注:不会存在插入后node.bf = 0的情况，因为如果node.bf在插入后变为0,则node.parent.bf在插入操作后一定不会变)


                elif node.parent.bf < 0:  # 插入前node.parent.bf = -1,插入后应当变为 0(这个node.parent实际上就是我们在找的A)
                    node.parent.bf = 0
                    break

                else: #node.parent.bf == 0
                    #插入前node.parent.bf = 0,插入后应当变为 1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            #连接head和n(只有进行了旋转操作之后才会到这一步)
            n.parent = head
            if head != None: #g不是空
                if tmp == head.lchild:
                    head.lchild = n
                else:
                    head.rchild = n
                break
            else: #g是空,说明n就是整棵树的根节点
                self.root = n
                break

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

tree = AVLTree([9,8,7,6,5,4,3,2,1])

tree.in_order(tree.root)















