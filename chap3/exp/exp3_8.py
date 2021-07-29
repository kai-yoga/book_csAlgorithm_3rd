'''
电路布线
'''
'''
input:
    dim=[7,6,3,1,4,0,8,2,9,5]
    top, down = len(dim), max(dim) + 1
output:
    [(8, 9), (6, 8), (4, 4), (2, 3)]
'''
def mNS(top,down,dim=[]):
    '''
    :param dim:上线柱从小到大依次接到下线柱的位置，如L=[1,2,3,4,5,6]
    :return:
    '''
    top, down = top,down
    s = [[0 for i in range(down)] for i in range(top)]
    for i in range(dim[0], down):
        s[0][i] = 1
    for i in range(1, top):
        for j in range(dim[i]):
            s[i][j] = s[i - 1][j]
        for j in range(dim[i], down):
            s[i][j]=max(
                s[i-1][j],
                s[i-1][dim[i]]+1
            )
    for ele in s:
        print(ele)
    return s

def track(s,dim,top,down):
    '''输出电路布线的最佳方式'''
    pass
    L=[]
    rows,j=top-1,down-1
    for i in range(rows,0,-1):
        if s[i][j]!=s[i-1][j]:
            j=dim[i]
            L.append((i,j))
        else:
            pass
    print(L)


# dim = [0,1,2,3,4,5,6]
# dim=[1,0]
# dim=[0,8,7,4,2,5,1,9,3,10,6]
dim=[7,6,3,1,4,0,8,2,9,5]
top, down = len(dim), max(dim) + 1
s=mNS(top,down,dim)
track(s,dim,top,down)
# for ele in mNS(dim):
#     print(ele)
