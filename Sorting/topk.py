#堆排序的应用: topk问题

#问题:
#   现在n个数,设计算法得到前k大的数(k<n)

#解决思路:
# 1)取列表前k个元素建立一个小根堆,堆里就是目前列表中前k大的元素
# 2)依次向后遍历原列表的后(n-k)个元素,对于这些元素元素,如果小于堆顶,则忽略该元素;如果大于堆顶,则将堆顶更换为该元素,并且对堆进行一次调整
# 3)遍历列表所有元素后,倒序弹出堆顶

# eg: 对于列表[6,8,1,9,3,0,7,2,4,5],取前5大的数
#     先取前5个数建立小根堆:                1
#                                    /     \
#                                   /       \
#                                  /         \
#                                 3           6
#                                / \
#                               /   \
#                              9     8

#再依次遍历列表后5个数:如果这个数比堆顶小(比如0),则忽略它; 如果比堆顶大(如7),则将堆顶换为该元素:  7
#                                                                               /     \
#                                                                              /       \
#                                                                             /         \
#                                                                            3           6
#                                                                           / \
#                                                                          /   \
#                                                                         9     8



#再进行一次调整,得到:                                                                 6
#                                                                               /     \
#                                                                              /       \
#                                                                             /         \
#                                                                            3           7
#                                                                           / \
#                                                                          /   \
#                                                                         9     8

#遍历完所有的元素并调整后就能得到前5大的元素:                                              5
#                                                                               /     \
#                                                                              /       \
#                                                                             /         \
#                                                                            6           7
#                                                                           / \
#                                                                          /   \
#                                                                         9     8


#topk的实现:

def sift(li,low,high):
    """

    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    """

    i = low
    j = 2*i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j+1] < li[j]: #66行和68行这两处用<是用于建立小根堆
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def topk(li,k):
    #79-83行是建堆
    heap = li[0:k]
    for i in range((k - 2) // 2, -1, -1):
        sift(heap,i,k-1)

    #84-88行是遍历原列表的后(n-k)个元素的过程
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap,0,k-1)

    #按顺序从大到小挨个弹出前k大的元素:
    for i in range(k-1,-1,-1):
        # 堆顶元素为这棵树中最大的元素,我们通过将它与树中最后一个尚未排好序的元素互换将它存储在目前堆中最末尾的位置,
        # 同时high—1,使得后面排序的变化都不会影响到这个最大元素
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)#此处high = i-1, 将堆最后一个元素放到堆顶后,此时可以通过一次向下调整使得堆有序,调整后的堆顶的元素又是此时除开排好序的元素后树中最大的元素

    return heap

li = [6,8,1,9,3,0,7,2,4,5,11,13,12,10]
print(topk(li,5))











