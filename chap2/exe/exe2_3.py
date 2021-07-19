'''
假定 L 已排序，x 为给定值
编写一个算法，实现
1）如果x不在L中，则返回大于x的最小值的位置和小于x的最大值的位置。
2）如果x在L中，则返回x的位置。
'''


def extendBinarySearch(L, x):
    if x <= L[0]:
        return {"left": 0,
                "right": 0}
    elif x >= L[len(L) - 1]:
        return {
            "left": len(L) - 1,
            "right": len(L) - 1
        }
    else:
        left, right = 0, len(L) - 1
        while left <= right:
            mid = (left + right) // 2
            print(left, right)
            if L[mid] == x:
                return {
                    "left": mid,
                    "right": mid
                }
            elif L[mid] < x and L[mid + 1] > x:
                return {
                    "left": mid,
                    "right": mid + 1
                }
            elif L[mid] > x and L[mid - 1] < x:
                return {
                    "left": mid - 1,
                    "right": mid
                }
            elif L[mid] < x:
                left = mid
            elif L[mid] > x:
                right = mid


L = [1, 2, 3, 4, 5, 6]
print(extendBinarySearch(L, 1.5))
