

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
def linerSearch(L, left, right, k):
    '''
    寻找L中第k小元素
    :param L: 输入列表
    :param left: 起始位置
    :param right: 结束位置
    :param k: 第k小
    :return: 第k小元素
    '''
    if right - left < 75:
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
        media = linerSearch(L, left, left + groups, groups // 2)
        # print('left',left,'right',right)
        t = mediaPartition(L, media)
        L = t[0]
        media_pos = t[1]  ###对L进行，找到中位数的中位数位置，并划分
        # print('after find media', media, media_pos, L)
        if media_pos - left + 1 >= k:
            return linerSearch(L, left, media_pos, k)
        else:
            return linerSearch(L, media_pos + 1, right, k - media_pos)



for k in range(12):
    x = linerSearch([13, 16, 9, 19, 15, 18, 18, 14, 13, 20, 35, 100], 0, right=11, k=k)
    print('k=>',k,'x=>',x)