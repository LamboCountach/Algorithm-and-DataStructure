def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li) - i - 1):
            if li[j+1] < li[j]:
                li[j],li[j+1] = li[j+1],li[j]
    return li

#加强版：
def advanced_bubble_sort(li): #如果在第i趟算法下来后发现没有发生交换，说明列表已经排好序，算法可以提前结束
    for i in range(len(li)-1): #第i趟
        exchanged = False
        for j in range(len(li) - i - 1):
            if li[j+1] < li[j]:
                li[j],li[j+1] = li[j+1],li[j]
                exchanged = True
        if not exchanged:
            break
    return li

print(bubble_sort([7,5,4,6,3,1,2,8,9]))
