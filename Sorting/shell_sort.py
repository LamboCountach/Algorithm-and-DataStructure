#希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。
#希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
#子列表的间隔一般从n//2开始,每趟倍增: n//4, n//8 ...直到1
def insert_sort_gap(li,gap):
    for i in range(gap,len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp
    return li

def shell_sort(li):
    gap = len(li) // 2
    while gap >= 1:
        insert_sort_gap(li, gap)
        gap //= 2
    return li

li = [5,7,4,6,3,1,2,9,8]
print(shell_sort(li))
