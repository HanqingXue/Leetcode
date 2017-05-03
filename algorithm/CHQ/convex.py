# coding =utf-8
import numpy as np
import random
import math
import time
import stack
import point
import line
class line(object):
    def __init__(self, start=object, end=object):
        super(line, self).__init__()
        self.start = start
        self.end = end

class Convex(object):
    """docstring for ClassName"""
    
    def __init__(self):
        super(Convex, self).__init__()
    
    def get_points(self, n=int):
        points = []
        for i in range(0, n):
            x = random.uniform(0, 100)
            y = random.uniform(0, 100)
            p = Point(x, y)
            points.append(p)
        return points
    
    @staticmethod
    def same_side(start_point, end_point, candidate_points):
        '''
        :param start_point:
        :param end_point:
        :param candidatePoint:
        :return: bool if candidatePoints in same side.
        '''
        np.seterr(invalid='ignore')
        
        op = ['null' for i in range(0, len(candidate_points))]
        matrix = np.matrix([[start_point.x, start_point.y, 1],
                            [end_point.x, end_point.y, 1],
                            [candidate_points[0].x, candidate_points[0].y, 1]])
        op[0] = '+' if np.linalg.det(matrix) > 0 else '-'
        
        
        for i in range(1, len(candidate_points) ):
            matrix = np.matrix([[start_point.x, start_point.y, 1],
                                [end_point.x, end_point.y, 1],
                                [candidate_points[i].x, candidate_points[i].y, 1]])
            if np.linalg.det(matrix) > 0:
                op[i] = '+'
            
            else:
                op[i] = '-'
                
            if op[i - 1] == op[i]:
                continue
            else:
                return False

        return True
    
    def get_polar(self, point_base, point_select):
        if point_base.x == point_select.x and point_select.y == point_select.y:
            return 0
        else:
            return math.atan2(point_select.y - point_base.y, point_select.x - point_base.x)

    def cross(self, top, next_top, p3):
        vx, vy = (top.x - next_top.x, top.y - next_top.y)
        wx, wy = (p3.x - next_top.x, p3.y - next_top.y)
        return (vx * wy - vy * wx)
        
    def force(self, points):
        ans = []
        boundpoint = set([])
        points_set = set(points)
        for i in range(0, len(points)):
            for j in range(i, len(points)):
                print 'i' + str(i) 
                print 'j' + str(j)
                if i == j: continue
                line_point = set([points[i], points[j]])
                candidate = list(points_set - line_point)
                if self.same_side(points[i], points[j], candidate):
                    boundline = line(points[i], points[j])
                    ans.append(boundline)
                    boundpoint.add(points[i])
                    boundpoint.add(points[j])
                    pass
        return boundpoint, ans

    def graham(self, points):
        points.sort(key=lambda point: point.y)
        point_base = points[0]
        origin_point = Point(0, 0)
        for item in points:
            polar = self.get_polar(point_base, item)
            item.set_polar(polar)
        
        points.sort(key=lambda point: point.polar)
        stack = Stack()
        stack.push(points[0])
        stack.push(points[1])
        stack.push(points[2])
        
        for i in range(3, len(points)):
            point = points[i]
            while self.cross(stack.top(), stack.nextTotop(), point) < 0:
                stack.pop()
            stack.push(point)
               
        return stack
    
    def divideConquer(self, points):
        points.sort(key=lambda point: point.x)
        middle = int(len(points)/2)
        left = points[:middle]
        right = points[middle:]
        CHQ_L = self.graham(left)
        CHQ_R = self.graham(right)
        
        for i in range(0, len(CHQ_R.stack) -1):
            if CHQ_R.stack[i].y > CHQ_R.stack[i+1].y:
                high = i
                break
        sq2 = CHQ_R.stack[:high]
        sq1 = CHQ_R.stack[high:]
        merge = sq1 + sq2 + CHQ_L.stack
        CHQ = self.graham(merge)
        return CHQ