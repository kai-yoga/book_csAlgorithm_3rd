'''
矩阵连乘
'''


# A = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
#
# B = [
#     [1, 1],
#     [1, 1],
#     [1, 1]
# ]


# def twoMul(A, B):
#     '''返回两个矩阵相乘需要的总次数'''
#     row_a = len(A)
#     col_a = len(A[0])
#     row_b = len(B)
#     col_b = len(B[0])
#     assert col_a == row_b
#     # res=[[0 for i in range(col_b)] for i in range(row_a)]
#     # print(res)
#     clac = row_a * row_b * col_b
#     # print(clac)
#     # if col_a==row_b:
#     #     for row in range(row_a):
#     #         for col in range(col_b):
#     #             sum=A[row][0]*B[0][col]
#     #             for k in range(1,row_b):
#     #                 sum=sum+A[row][k]*B[k][col]
#     #             res[row][col]=sum
#     # else:
#     #     print('martix not mul')
#     return clac


def dynaminMartixMul(dim):
    '''返回矩阵相乘最优的分解顺序
    :param: dim=[(row,col),(row.col),...]
    '''
    ele_num = len(dim)
    clacMarix = [[0 for i in range(ele_num)] for i in range(ele_num)]
    s = [[0 for i in range(ele_num)] for i in range(ele_num)]
    for r in range(1, ele_num):
        for start in range(ele_num - r):
            end = start + r
            print('start=', start, 'end=', end)
            # print(dim[start:end + 1])
            # print('*'*30)
            clacMarix[start][end] = clacMarix[start + 1][end] + dim[start][0] * dim[start][1] * dim[end][1]
            s[start][end] = start
            for breakPostion in range(start + 1, end):
                # print('exe')
                t = clacMarix[start][breakPostion] + clacMarix[breakPostion + 1][end] + dim[start][0] * \
                    dim[breakPostion][1] * dim[end][1]
                # print()
                if t < clacMarix[start][end]:
                    clacMarix[start][end] = t
                    s[start][end] = breakPostion
                    # print('change')
    # print(clacMarix)
    return s


def clacMartixMul(*dim):
    '''返回矩阵连乘需要计算的次数
    :param: dim=[(row,col),(row.col),...]
    '''
    print(dim)
    # dim=dim[0]
    # sum = dim[0][0]*dim[0][1]
    if len(dim) > 1:
        sum = dim[0][0] * dim[0][1] * dim[1][1]
        t = (dim[0][0], dim[1][1])
        # print(t,sum)
        for i in range(2, len(dim)):
            sum = sum + t[0] * t[1] * dim[i][1]
            t = (dim[0][0], dim[i][1])
            # print(t,sum)
    # return sum
    # for ele in dim[1:]:
    #     # for e in ele:
    #     sum=sum*ele[1]
    print(sum)
    return sum


dim = [
    (30, 35),
    (35, 15),
    (15, 5),
    (5, 10),
    (10, 20),
    (20, 25)
]


# print(clacMartixMul(dim))
# print(dynaminMartixMul(dim))
def trackback(start, end, s):
    if start == end:
        return
    trackback(start, s[start][end], s)
    trackback(s[start][end] + 1, end, s)
    print(' Multiply A ', start,',', s[start][end], 'and A', s[start][end] + 1,',', end)


s = dynaminMartixMul(dim)
# print(s)
trackback(0, 5, s)
