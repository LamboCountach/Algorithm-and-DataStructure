#基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较(从个位开始,比较到最高位)
def radix_sort(li):
    max_num = max(li) #找出li中最大的数,实际上也是为了找出要比较位数的次数(eg: 10000是5次(因为它是5位数),88是2次)
    it = 0 #it代表迭代的次数
    while 10 ** it <= max_num:
        buckets = [[] for i in range(10)] #该算法分桶的方法是按照一个位上数字的范围分类(一个位上只能是0-9中的一个数)
        for var in li:
            digit = (var // 10 ** it) % 10 #这一步得到第it次迭代时var在这一位上对应的元素(eg: var=987, it=0时比较的是个位,digit=（987 // 10**0) % 10 = 7
                                           #i = 2时, digit = (987 // 10 ** 2) % 10 = 9)
            buckets[digit].append(var) #根据在第it次迭代得到的digit的值,将这个数append到bucket[i]

        li.clear()
        for b in buckets:
            li.extend(b)#extend()方法可以在一个列表末尾一次性追加另一个序列中的多个值
        #将每个桶里的数按照从bucket[0]到bucket[9]的顺序加入到list,就算完成一次排序

        it += 1
    return li

    #当10 ** it > max_num时,跳出循环,相当于我们把各个元素的每一位上的数都按照8-14行的代码执行了一遍,最终返回的li一定是排好序的li

