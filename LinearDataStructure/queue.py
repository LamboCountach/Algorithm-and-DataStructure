#队列实现方式: 使用固定长度的数组
    #队列仅允许在队列的一端进行插入,另一端进行删除
    #进行插入的一端成为队尾(rear)
    #进行删除的一端称为队头(front)

#环形队列:当队尾指针rear==max_size + 1时,再前进一个位置就会回到0
    #由于实现队列的数组的长度固定,这里的max_size指的是队列的长度
#队首指针前进1: front = (front+1) % max_size
#队尾指针前进1: rear = (rear+1) % max_size
#队列为空的条件:front == rear
#队列满的条件: (rear+1) % max_size == front

class Queue:
    def __init__(self, size): #创建一个固定长度的队列
        self.size = size
        self.queue = [0 for i in range(size)]  #初始化的队列,所有元素都是0
        self.front = 0 #队头指针
        self.rear = 0 #队尾指针

    def enqueue(self,element):
        if not self.is_filled():
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = element
    #从push()方法我们可以发现,当队列为空时,第一个被push的元素实际上是被push到队列中编号下标为1(而不是0)的位置,此时queue[front]的位置没有元素
    #无论何时,在front指针所指的位置,即queue[front],不会被添加元素
        else:
            raise IndexError("The queue is full!")

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front] #此时我们不用管queue[front]上之前是否被添加过元素,因为添不添加我们都不管
        else:
            raise IndexError("Queue is empty!")

    def is_empty(self):
        return self.front == self.rear

    def is_filled(self): #判断是否队列满了
        return (self.rear + 1) % self.size == self.front
    #注意：由于无论在queue[front]上之前是否被添加过元素,我们都当作queue[front]这里没有被添加过元素,
    #因此,对于一个size为n的队列,当队列满时,实际上队列里只有(n-1)个元素

q =Queue(5)
for i in range(4):
    q.enqueue(i)
q.dequeue()
print(q.is_filled())