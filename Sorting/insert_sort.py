def insert_sort(li):
    for i in range(1,len(li) - 1):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
    return li

print(insert_sort([7,5,4,6,3,1,2,8,9]))