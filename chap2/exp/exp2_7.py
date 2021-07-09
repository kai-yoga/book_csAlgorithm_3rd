# res=[]
import random


def merge(left, right):
    '''
    合并left，right两个值
    :param left:
    :param right:
    :return:
    '''
    res = []
    len_left, len_right = len(left), len(right)
    index_left, index_right = 0, 0
    while index_left < len_left and index_right < len_right:
        if left[index_left] <= right[index_right]:
            res.append(left[index_left])
            index_left = index_left + 1
        else:
            res.append(right[index_right])
            index_right = index_right + 1
    if index_left==len_left:##左边合并完成
        res=res+right[index_right:]
    else:
        res=res+left[index_left:]

    # print(res)
    return res

def mergeSort(L):
    '''
    合并排序,递归版本
    :param L 待排序的列表
    :left 列表L的左边起点
    :right 列表L的右边结束点
    :return:
    递归版本的设计思路为，分析能力仍为首要，要判断一个问题是否可以使用递归进行解决，
    与之最为紧密的为数学归纳法。
    if n==1 or other conditions find the recurison out_interface:
    else analysis and proof the not in the if code.
    ---mersort recursion algorithms:
    if n==1 just L which has only one elements
    else
        find the middle postion in the L
        merge sort the left
        merge sort the right
        merge left and right

    '''
    if len(L) <= 1:
        return L
    else:
        middle = len(L) // 2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        return merge(left, right)


input_L = [13, 16 , 9, 19, 15, 18, 18, 14, 13, 20]
print(input_L)
print('*****')
print(mergeSort(input_L))
