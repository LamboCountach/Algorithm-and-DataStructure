

#哈希表,是一种线性表的存储结构。哈希表由一个 直接寻址表 & 一个哈希函数组成。哈希函数h(k)将元素关键字k作为变量,h(k)即为元素在哈希表中的存储下标
#eg: 假设一个长度为7的哈希表, 哈希函数h(k) = k % 7。 元素集合{14,22,3,5}的存储方式如下:
    #设T为哈希表, 则T[0]= 14, T[1] = 22, T[3] = 3, T[5]  = 5

# 哈希冲突:
#     由于哈希表的大小是有限的,因此对于任意的哈希函数,都可能会出现两个不同的元素映射到同一个存储下标上的情况
# 比如对于h(k) = k % 7, h(0) = h(7) = h(14) = ...

# 解决哈希冲突: 拉链法
#     拉链法:哈希表的每一个元素都是一个链表,当冲突发生时,冲突的元素将被加到该位置链表的最后


class LinkList:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    class LinkListIterator: #迭代器
        def __init__(self, node):
            self.node = node

        def __next__(self): #支持__next__方法
            if self.node != None:
                curNode = self.node
                self.node = curNode.next
                return curNode.item
            else:
                raise StopIteration
        def __iter__(self):
            return self



    def __init__(self, list):
        self.head = None
        self.tail = None
        if list != None:  #如果list != None, 调用extend()方法在链表尾部插入list中的所有元素
            self.extend(list)

    def append(self,obj): #在链表尾部插入元素
        s = self.Node(obj)
        if self.head == None:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, li): #在链表尾部插入多个元素
        for obj in li:
            self.append(obj)

    def find(self,obj): #查找一个元素是否已经存在于列表中
        for node in self:
            if node == obj:
                return True
        return False

    def __iter__(self): #让LinkList支持迭代
        return self.LinkListIterator(self.head)

    def __repr__(self): #toString方法
        return "<<" + ",".join(map(str, self))+">>" # map(str,self)是将本来是int类型的self转化成str型

#hash_table实际上是一个类似于集合的结构,即集合中不存在重复元素
class hash_table:
    def __init__(self, size):
        self.size = size
        self.T = [LinkList(None) for i in range(size)] #初始化一个哈希表T

    def h(self, k): #哈希函数
        return k % self.size

    def insert(self,k):
        i = self.h(k)
        if self.find(k): #如果被插入元素已经存在于链表中
            print("Duplicated insertion is not allowed!")
        else:
            self.T[i].append(k)


    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)

ht = hash_table(101)

ht.insert(0)
ht.insert(1)
ht.insert(102)

print(",".join(map(str,ht.T)))













