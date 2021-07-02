
# from chap2 import  exp2_8 as quickSort
# import math
# L=quickSort.input_L
#
# def linerSearch(L,left,right,k):
#     if right-left<=75:
#         return quickSort.quickSort(L)[left+k-1]
#     else:
#         # left=0
#         # right=len(L)-1
#         groups=math.ceil((right-left)/5)
#         print(L)
#         res=[]
#         for g in range(groups):
#             ####将每组排序
#             # print(quickSort.quickSort(L[left + g * 5:left + (g + 1) * 5]))
#             # print('g=>',g,'left=>',left+g*5,'right=>',left+(g+1)*5,
#             #       'mid',min(left+g*5+2,right)
#             #       )
#             # print(quickSort.quickSort(L[left + g * 5:left + (g + 1) * 5]))
#             # L[min(2, right - left - g * 5)]=L[left+g*5]
#             # tmp=quickSort.quickSort(L[left + g * 5:left + (g + 1) * 5])[min(2,right-left-g*5)]
#             # L[min(2, right - left - g * 5)]=L[left+g*5]
#             # L[left + g * 5]=tmp
#             L[left+g*5:min(right,left+(g+1)*5)]=quickSort.quickSort(L[left + g * 5:min(right,left+(g+1)*5)])
#             tmp=L[min(2, right - left - g * 5)+left+g*5]
#             L[min(2, right - left - g * 5)+left+g*5]=L[left+g*5]
#             L[left + g * 5]=tmp
#
#
#             # L[min(2,right-left-g*5)]=tmp
#             res.append({
#                 'value':quickSort.quickSort(L[left + g * 5:left + (g + 1) * 5])[min(2,right-left-g*5)],
#                 'pos':left+5*g
#             })
#         media=linerSearch(L,left,)
#         # media_list=[key for key in res]
#         # media=linerSearch(media_list,k//2)
#
#         print(res)
#         print("quickSort=>",L)
#
#     # res=res+quickSort.quickSort(L[left + g * 5:left + (g + 1) * 5])[min(left+g*5+2,right)]
#           # 'media=>',math.ceil((min(right,left+(g+1)*5)-(left+g*5))/5)+left+g*5
#     # print(
#     #     math.ceil(
#     #         (min(right,left+(g+1)*5)-left*g)/5+left*g
#     #     )
#     # )
#     # res=res+quickSort.quickSort(L[left+g*5:left+(g+1)*5])[math.ceil((min(right,left+(g+1)*5)-left*g)/5)]
#
#     # print('res=>',res)
