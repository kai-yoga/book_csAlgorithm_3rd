'''
**************最邻近点对问题***********
****给定平面上一系列点point_i={(x_i,y_i)|1<=i<=n},*****
****找出distance=min(sqrt((x_i-x_j)**2+(y_i-y_j)**2))*
***所对应的point_i,point_j***************************
****算法的大致思路******
1.find the media point;
2.diver the point set by media point then get two suber point sets,
assume P1,P2 and the point in P1 if point.x_i<media point.x_y,
else the point in P2
3.get the min distance min_d=min(the points in P1,the points in P2)
3.find the border point where point.x_i=media point.x_y and the point
in P2 's distance border_min_d
4 if the border_min_d less than min_d then min_d=border_min_d
'''
import math



class Point:
    def __init__(self, x, y):
        self._x, self._y = x, y

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def getDistance(self, other):
        '''返回两点之间的欧式距离'''
        return math.sqrt(
            (self._x - other._x) ** 2 + (self._y - other._y) ** 2
        )

