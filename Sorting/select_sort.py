def select_sort(li):
    for i in range(len(li)-1): #第i趟
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]
    return li

print(select_sort([7,5,4,6,3,1,2,8,9]))