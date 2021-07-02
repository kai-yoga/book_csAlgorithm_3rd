from chap2 import base

def buble(L):
    len_L=len(L)
    for i in range(len_L):
        for j in range(i+1,len_L):
            if L[i]>L[j]:
                tmp=L[j]
                L[j]=L[i]
                L[i]=tmp
    return L

# print(base.const_L)
# print(buble(base.const_L))