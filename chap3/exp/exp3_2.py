'''
最大字段和
对于给定的序列 A={a_i,i
'''

A = [-2, 11, -4, 13, -5, -2]


def searchAll(A):
    '''穷举算法
    i:dynamic start postion
    j:dynamic end position
    find the max sum in A[i:j]
    '''
    len_A = len(A)
    sum = 0
    best_i = 0
    best_j = 0
    for i in range(len_A):
        for j in range(i, len_A):
            thissum = 0
            for k in range(i, j + 1):
                thissum = thissum + A[k]
            if thissum > sum:
                sum = thissum
                best_i = i
                best_j = j
        return sum, best_i, best_j


def partitionSearch(A,left,right):
    '''分治算法'''
    pass
    sum=0
    if left==right:
        sum=A[left] if A[left]>0 else 0
    else:
        mid=(left+right)//2



