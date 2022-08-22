#在计数排序中,如果元素的范围比较大(比如0-10000之间),如何改造算法？

#桶排序:首先将元素分在不同的桶中,再对每个桶中的元素进行排序

# eg: li=[29,25,3,49,9,37,21,43] 我们分5个桶(0-9是第一个桶,10-19是第二个桶,20-29是第三个桶,30-39是第四个桶,40-49是第5个桶),
# 将每个元素装到其对应范围的桶中,再在桶内进行冒泡排序,最终将每个排好序的桶中的元素按桶1到桶5的顺序加入到一个空list中,最终返回这个list

def bucket_sort(li, n=100, max_num = 10000): #这里算法适用的范围是对于一个每个元素的范围都在0-10000的列表,我们创建100个桶
    buckets = [[] for i in range(n)] #初始化100个桶
    for var in li:
        # 对于li中的每个元素(除了值为10000的元素),它应该被装到bucket[var // (max_num //n)],
        # 对于值为10000的元素,我们想要将它加入到bucket[99](即第100个桶),即bucket[n-1]
        #使用min()方法就能将值不等于10000和值等于10000的元素能恰好把它们放到它们所对应的桶中
        j = min(var // (max_num // n), n-1) #j指的就是li中一个元素应该被放入的桶的index
        buckets[j].append(var)

        #使用冒泡排序将每个桶内元素排好序
        for k in range(len(buckets[j])-1, 0,-1):
            if buckets[j][k-1] > buckets[j][k]:
                buckets[j][k-1],buckets[j][k] = buckets[j][k],buckets[j][k-1]
            else:
                break
    li.clear()
    for m in range(n):
        li.extend(buckets[m])#extend()方法可以在一个列表末尾一次性追加另一个序列中的多个值
    return li



#extend()方法例子:
    # aList = []
    # bList = [2009, 'manni']
    # aList.extend(bList)
    # 那么aList的值变为: aList = [2009, 'manni']


li = [5,7,4,6,3,1,2,9,8]
print(bucket_sort(li))