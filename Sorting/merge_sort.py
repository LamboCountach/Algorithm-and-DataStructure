def merge(li,low,mid,high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high: #只要左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1

    #while执行完,肯定有一边没数了
    while i <= mid:
         ltmp.append(li[i])
         i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp

#归并排序--使用归并
# 分解: 将列表越分越小,直至分成一个元素
# 终止条件: 一个元素的列表是有序的
# 合并: 将两个有序列表归并,列表越来越大

def merge_sort(li,low,high): #运用递归
    #时间复杂度:(0(nlogn))
    #一次归并(即merge方法)的时间复杂度是O(n),
    #合并过程(诸如长度为2的列表和长度为2的列表合并成长度为4的列表,长度为4的列表和长度为4的列表合并成长度为8的列表,最后长度为n/2的列表和长度为n/2的列表合并为长度为n的列表)的时间复杂度O(logn)
    #所以总的时间复杂度为O(nlogn)
    # 空间复杂度: O(n)
    if low < high:  #至少有两个元素
        mid = (low + high) // 2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)

    #递归终止条件:一个列表一定是有序的
    else:
        return li
    return li

# li = [15,13,2,8,6,14,5,10,3,4,12,1,0,11,9,7]
# print(merge_sort(li,0,len(li)-1))

def merge_sort_test(li,low,high):
    if low < high:
        mid = (low + high) // 2
        merge_sort_test(li,low,mid)
        merge_sort_test(li,mid+1,high)
        print(li)

li = [5,7,4,6,3,1,2,9,8]
print(merge_sort(li,0,len(li)-1))
#merge_sort_test(li,0,len(li)-1)






