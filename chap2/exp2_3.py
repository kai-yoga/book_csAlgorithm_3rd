def binnarySearch(L,x):
    '''二分搜索，
    :param L,有序
    x: 搜索值'''
    # res=None
    max_postion=len(L)
    postion=max_postion//2
    while postion<max_postion:
        if L[postion]==x:
            # res=postion
            return postion
        elif L[postion]<x:
            add=len(L[postion+1:])//2 if len(L[postion+1:])//2>0 else 1
            # print
            postion=postion+add
            # print(postion)
        elif L[postion]>x:
            add=len(L[postion+1:])//2 if len(L[postion+1:])//2>0 else 1
            postion=postion-add
            max_postion=postion
        else:
            pass
    return -1

L=[i for i in range(1,11)]
# print(L)
print(binnarySearch(L,0.5))
print(binnarySearch(L,11))