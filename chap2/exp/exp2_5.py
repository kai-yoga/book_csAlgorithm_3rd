def div_int(n,m):
    '''计算n可以拆分为每个证书不大于m的整数之和的种类
    :param n:待拆分整数
    m:拆分的整数中最大值'''
    if n<1 or m<1:
        return 0
    if m==1:
        return 1
    if m==n:
        return 1+div_int(n,m-1)
    if n>m:
        return div_int(n,m-1)+div_int(n-m,m)##这一步有点疑问
    else:
        return div_int(n,n)
    # else:
    #     return div_int(n,m-1)
    # # return div_int(n,m-1)+div_int(n-m,m)

# print(div_int(3,3))
