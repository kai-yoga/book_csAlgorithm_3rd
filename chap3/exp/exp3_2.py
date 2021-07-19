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


def partitionSearch(A, left, right):
    '''分治算法'''
    pass
    sum = 0
    if left == right:
        sum = A[left] if A[left] > 0 else 0
    else:
        mid = (left + right) // 2
        leftsum = partitionSearch(A, left, mid)
        rightsum = partitionSearch(A, mid, right)
        left_value, right_value, lefts, rights = 0, 0, 0, 0
        for i in range(left, mid):
            lefts += A[i]
            if lefts > left_value:
                left_value = lefts
        for i in range(mid, right):
            rights += A[i]
            if rights > right_value:
                right_value = rights
        sum = left_value + right_value
        if sum < leftsum:
            sum = leftsum
        if sum < rightsum:
            sum = rightsum
    return sum


def dyanmicSearch(A):
    '''动态规划算法'''
    sum = 0
    b = 0
    for i in range(len(A)):
        if b > 0:
            b += A[i]
        else:
            b = A[i]
        if b > sum:
            sum = b
    return sum


def d2DyanmicSearch(A,rows,cols):
    '''二维的动态规划算法
    A=[
    [-1,-1,1,2],
    [-1,-1,1,2],
    [-1,-1,1,2]
    ]'''
    pass
    sum=0
    b=[0 for i in range(cols)]
    for row in range(rows):
        for col in range(cols):
            if b[col]>0:
                b+=A[row][col]
            else:
                b=A[row][col]
