'''
quickSort
'''

import random


def swap(L, value, left, right):
    '''对L进行一趟按value进行左右区分
    对于与所选value相等值时，要注意处理方式,left继续向前移动一次
    :param L:待排序列表,
    :param value:所选的标记值
    :left :起始位置索引
    :right :结束位置索引
    返回[L,left]L为排序后的列表，
    left为所选value最终停留的位置'''
    while left < right:
        if L[right] > value:
            right = right - 1
        elif L[right] < value:
            tmp = L[right]
            L[right] = L[left]
            L[left] = tmp
            left = left + 1
        elif L[left] <= value:  # 等值时，同样进行交换一次
            left = left + 1
        elif L[left] > value:
            tmp = L[left]
            L[left] = L[right]
            L[right] = tmp
            right = right - 1
    return [L, left]


def quickSort(L):
    '''quick sort
    :param L: sort list'''
    pass
    if len(L) >= 2:
        index = random.randint(0, len(L) - 1)
        # print(index)
        res = swap(L=L, value=L[index], left=0, right=len(L) - 1)
        L = res[0]
        left = res[1]
        return quickSort(L[:left]) + L[left:left + 1] + quickSort(L[left + 1:])
    else:  # 递归出口，只有一个元素时
        return L


# print('orig', input_L)
# print('sort', quickSort(input_L))
