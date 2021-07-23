'''
矩阵连乘
'''

A=[
    [1,2,3],
    [4,5,6]
]

B=[
    [1,1],
    [1,1],
    [1,1]
]

def twoMul(A,B):
    '''返回两个矩阵相乘需要的总次数'''
    row_a=len(A)
    col_a=len(A[0])
    row_b=len(B)
    col_b=len(B[0])
    assert col_a==row_b
    # res=[[0 for i in range(col_b)] for i in range(row_a)]
    # print(res)
    clac=row_a*row_b*col_b
    # print(clac)
    # if col_a==row_b:
    #     for row in range(row_a):
    #         for col in range(col_b):
    #             sum=A[row][0]*B[0][col]
    #             for k in range(1,row_b):
    #                 sum=sum+A[row][k]*B[k][col]
    #             res[row][col]=sum
    # else:
    #     print('martix not mul')
    return clac

def dynaminMartixMul(dim):
    '''返回矩阵相乘最优的分解顺序
    :param: dim=[(row,col),(row.col),...]
    '''
    ele_num=len(dim)
    clacMarix=[[0 for i in range(ele_num)] for i in range(ele_num)]
    for r in range(1,ele_num):
        for i in range(ele_num-r):
            j=i+r-1
            clacMarix[i][j]=clacMarix[i][j-1]


def clacMartixMul(dim):
    '''返回breakPoint位置时，需要计算的次数
    :param: dim=[(row,col),(row.col),...]
    '''
    sum=0
    if len(dim)>1:
        sum=dim[0][0]*dim[0][1]*dim[1][1]
        t=(dim[0][0],dim[1][1])
        # print(t,sum)
        for i in range(2,len(dim)):
            sum=sum+t[0]*t[1]*dim[i][1]
            t=(dim[0][0],dim[i][1])
            # print(t,sum)
    return sum

print(clacMartixMul([(3,4),(4,5)]))
# print(twoMul(A,B))