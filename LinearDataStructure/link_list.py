#链表:一系列节点组成的元素集合。每个节点包含两个部分,数据域item和指向下一个节点的指针next。 (链表不是顺序存储)

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

#链表的创建:
    #链表的创建有两种方法:头插法和尾插法
    #头插法:将一个列表中的元素依次插入到链表的头部
    #尾插法:将一个列表中的元素依次插入到链表的尾部

#头插法实现:
    def create_linklist_head(self,li):
        head = Node(li[0])
        for element in li[1:]:
            currentNode = Node(element)
            currentNode.next = head
            head = currentNode
        return head

#尾插法实现:
    def create_linklist_tail(self,li):
        head = Node(li[0])
        tail = head
        for element in li[1:]:
            currentNode = Node(element)
            tail.next = currentNode
            tail = currentNode
        return head

    def print_lk(self,lk):
        while lk: #while lk != None
            print(lk.item, end = "\n")
            lk = lk.next

#链表节点的插入:
    def insert(self,p,currentNode):#p为待插入节点,currentNode是p插入后在p之前的节点
        #40-41行代码顺序不能反!
        p.next = currentNode.next
        currentNode.next = p

#链表节点的删除:
    def remove(self,currentNode):
        p = currentNode.next #p为待删除节点,currentNode是p被删除前在p之前的节点
        currentNode.next = currentNode.next.next
        del(p) #del(p)这一步其实可要可不要



    #                     顺序表(列表/数组)      链表
    # 按元素值查找            O(n)               O(n)
    # 按下标查找              O(1)               O(n)
    # 在某元素后插入           O(n)               O(1)
    # 删除某元素              O(n)               O(1)


