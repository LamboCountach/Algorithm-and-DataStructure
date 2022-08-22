#计数排序: 对列表进行排序,已知列表中的数都在大于等于0且小于等于100(可重复)
def count_sort(li,max_count=100): #计数排序算法复杂度: O(n)
    count = [0 for i in range(max_count+1)] #创建一个包含100个0元素的列表
    for v in li: #例如li中有一个元素值是2,那么我们就让count[2]+1
        count[v] += 1
     #遍历完一遍li后,我们就能知道每个在0-100之间的值在li中出现了多少次

    li.clear()#清空li,使li=[] (注: clear()方法的时间复杂度是O(n))

    #11-13行虽然是一个嵌套for循环,实际上它的时间复杂度只有O(n)
    for index, value in enumerate(count): #index指的是编号下标,value指的是一个编号下标对应的值,例如:li[3] = 4, 那么index=3,value = 4
        for i in range(value):
            li.append(index)  #例如:count[0] = 4,count[1] = 2,说明li中包含4个0,2个1,那我们先让li append4个0,再append2个1
    #这个嵌套for循环结束后,得到的就是排好序的列表

    return li

#计数排序的缺点:必须要求列表中的元素值在某一个范围之间(比如列表中的数都在大于等于0且小于等于100),否则无法创建一个固定长度的、用于计数的count列表,而且创建列表会增加空间复杂度
li = [5,7,4,6,3,1,2,9,8]
print(count_sort(li,100))