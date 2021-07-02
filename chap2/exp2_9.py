# from chap2 import  exp2_8 as quickSort
# import math
# L=quickSort.input_L
#
# def linerSearch(L,left,right,k):
#     if right-left<=75:
#         return quickSort.quickSort(L)[left+k-1]
#     else:
#         # left=0
#         # right=len(L)-1
#         groups=math.ceil((right-left)/5)
#         print(L)
#         res=[]
#         for g in range(groups):
#             ####将每组排序
#             # print(quickSort.quickSort(L[left + g * 5:left + (g + 1) * 5]))
#             # print('g=>',g,'left=>',left+g*5,'right=>',left+(g+1)*5,
#             #       'mid',min(left+g*5+2,right)
#             #       )
#             # print(quickSort.quickSort(L[left + g * 5:left + (g + 1) * 5]))
#             # L[min(2, right - left - g * 5)]=L[left+g*5]
#             # tmp=quickSort.quickSort(L[left + g * 5:left + (g + 1) * 5])[min(2,right-left-g*5)]
#             # L[min(2, right - left - g * 5)]=L[left+g*5]
#             # L[left + g * 5]=tmp
#             L[left+g*5:min(right,left+(g+1)*5)]=quickSort.quickSort(L[left + g * 5:min(right,left+(g+1)*5)])
#             tmp=L[min(2, right - left - g * 5)+left+g*5]
#             L[min(2, right - left - g * 5)+left+g*5]=L[left+g*5]
#             L[left + g * 5]=tmp
#
#
#             # L[min(2,right-left-g*5)]=tmp
#             res.append({
#                 'value':quickSort.quickSort(L[left + g * 5:left + (g + 1) * 5])[min(2,right-left-g*5)],
#                 'pos':left+5*g
#             })
#         media=linerSearch(L,left,)
#         # media_list=[key for key in res]
#         # media=linerSearch(media_list,k//2)
#
#         print(res)
#         print("quickSort=>",L)
#
#     # res=res+quickSort.quickSort(L[left + g * 5:left + (g + 1) * 5])[min(left+g*5+2,right)]
#           # 'media=>',math.ceil((min(right,left+(g+1)*5)-(left+g*5))/5)+left+g*5
#     # print(
#     #     math.ceil(
#     #         (min(right,left+(g+1)*5)-left*g)/5+left*g
#     #     )
#     # )
#     # res=res+quickSort.quickSort(L[left+g*5:left+(g+1)*5])[math.ceil((min(right,left+(g+1)*5)-left*g)/5)]
#
#     # print('res=>',res)

from chap2 import exp2_8 as quicksort, base
import math
from chap2 import bubleSort


def mediaPartition(L, media):
    '''将L按meidia进行划分,左边小于media,右边大于media,并返回划分后media的位置'''
    left = 0
    right = len(L)-1
    while left < right:
        if L[right] > media:
            right -= 1
        elif L[right] < media:
            tmp = L[left]
            L[left] = L[right]
            L[right] = tmp
            left += 1
        elif L[left] < media:
            left += 1
        elif L[left] >= media:
            tmp = L[right]
            L[right] = L[left]
            L[left] = tmp
            right -= 1
    return [L, left]


# print(base.CONST_L)
# print(mediaPartition(base.CONST_L,0,len(base.CONST_L)-1,13))
def linerSearche(L, left, right, k):
    '''
    寻找L中第k小元素
    :param L: 输入列表
    :param left: 起始位置
    :param right: 结束位置
    :param k: 第k小
    :return: 第k小元素
    '''
    if right - left < 3:
        '''对于长度小于75的列表，直接排序，输出其中的第k小元素即可'''
        L[left:right] = bubleSort.buble(L[left:right])
        # print(L)
        # print('<3','left,', left, 'right,', right, L[left:right])
        return L[left + k]
    else:
        groups = math.ceil((right - left) / 5)
        # print(groups)
        for g in range(groups):
            # print('g=>',g,'g l=>',L[left+5*g:left+5*(g+1)])
            L[left + 5 * g:min(right, left + 5 * (g + 1))] = bubleSort.buble(
                L[left + 5 * g:min(right, left + 5 * (g + 1))])
            # print('g=>', g, 'g l=>', L[left + 5 * g:left + 5 * (g + 1)])
            tmp = L[left + 5 * g + (min(right, left + (g + 1) * 5) - left - 5 * g) // 2]
            L[left + 5 * g + (min(right, left + (g + 1) * 5) - left - 5 * g) // 2] = L[left + g]
            L[left + g] = tmp
        # print('before media', 'left', left, 'groups', groups, 'media_media', groups // 2, 'L', L)
        media = linerSearche(L, left, left + groups, groups // 2)
        # print('left',left,'right',right)
        t = mediaPartition(L, media)
        L = t[0]
        media_pos = t[1]  ###对L进行，找到中位数的中位数位置，并划分
        # print('after find media', media, media_pos, L)
        if media_pos - left + 1 >= k:
            return linerSearche(L, left, media_pos, k)
        else:
            return linerSearche(L, media_pos + 1, right, k - media_pos)
        # print(L)
        # return L
        # print(L)


# print(quicksort.quickSort(base.CONST_L))
# print(quicksort.quickSort())
# print(quicksort.quickSort(base.CONST_L))
# for k in range(12):
# x = linerSearche([13, 16, 9, 19, 15, 18, 18, 14, 13, 20, 35, 100], 0, right=11, k=10)
# # print('k=>',k,'x=>',x)
# print(x)

for k in range(12):
    x = linerSearche([13, 16, 9, 19, 15, 18, 18, 14, 13, 20, 35, 100], 0, right=11, k=k)
    print('k=>',k,'x=>',x)