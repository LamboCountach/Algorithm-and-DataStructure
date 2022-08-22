def partition(li, left, right): #partition的时间复杂度是O(n)
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:   #从右边找比tmp小的数
        #注意:第四行有加入left < right是因为从右边开始一直往左走直到tmp时，如果都没有比tmp小的数时，会执行right-=1，导致right会比left小，出现问题
        #例如:[5,6,7,8,9]，当right从9一直走到5时，因为li[right] = tmp，right-=1，right的值变为-1，而left=0,导致right最终不等于left,tmp无法被归位到正确的位置上
            right -= 1      #往左走一步
        li[left] = li[right]       #把右边的值填写到左边空位上
        while left < right and li[left] <= tmp: #从左边找比tmp大的数
            left += 1   #往右走一步
        li[right] = li[left]   #把左边的值填到右边空位上
    li[left] = tmp   #此时left一定等于right,我们把tmp归位在中间，使得:
                     #所有比tmp小(或等于)的元素都被排列在tmp左边，比tmp大(或等于)的元素都被排列在tmp右边
                     #此处写li[left] = tmp 和 li[right] = tmp 是一样的
    return left

def quick_sort(li,left, right): #时间复杂度为O(nlogn) #最坏情况(例如[9,8,7,6,5,4,3,2,1])为O(n^2),还可能会达到递归深度最大值
    if left < right: #至少有两个元素
        mid = partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1, right)
    return li

li = [9,8,7,6,5,4,3,2,1]
print(partition(li,0,len(li)-1))
