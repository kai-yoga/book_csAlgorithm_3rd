def perm(L,current_positon,len_L):
    '''输出L的L[current_position:]全排列
    :param L:无序列表型，
    current_positon:当前所排参数位置
    len_L:L的长度
    '''
    if current_positon==len_L-1:
        print(','.join(L))
    else:
        for i in range(current_positon,len_L):
            '''将L[k]与L[i]进行交换'''
            tmp=L[i]
            L[i]=L[current_positon]
            L[current_positon]=tmp
            ####递归处理L[k+1:]之后的排列
            perm(L,current_positon+1,len_L)
            '''将L[i]与L[k]交换回来'''
            tmp=L[current_positon]
            L[current_positon]=L[i]
            L[i]=tmp
        pass

def call_exp():
    '''调用示例'''
    L=['a','c','b']
    current_postion=0
    len_L=len(L)
    perm(L=L,current_positon=current_postion,len_L=len_L)

call_exp()