# coding =utf-8
import numpy as np
import matplotlib.pylab as plt
import random

class Point(object):
    """docstring for point"""
    
    def __init__(self, x, y):
        super(Point, self).__init__()
        self.x = x
        self.y = y

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
    
    def force(self, points):
        plt.figure()
        plt.title('Convex of {} points'.format(len(points)))
        ans = []
        boundpoint = set([])
        points_set = set(points)
        for i in range(0, len(points)):
            for j in range(i, len(points)):
                if i == j: continue
                line_point = set([points[i], points[j]])
                candidate = list(points_set - line_point)
                if self.same_side(points[i], points[j], candidate):
                    boundline = line(points[i], points[j])
                    ans.append(boundline)
                    boundpoint.add(points[i])
                    boundpoint.add(points[j])
                    pass
        
        plt.scatter([points[i].x for i in range(0, len(points))], [points[i].y for i in range(0, len(points))])
        for item in ans:
            plt.plot([item.start.x, item.end.x], [item.start.y, item.end.y], "--")
        plt.show()
        return boundpoint
        
if __name__ == '__main__':
    '''
    p1 = Point(0, 2)
    p2 = Point(1, 3)
    p3 = Point(2, 0)
    p4 = Point(0, -4)
    p5 = Point(-1.2, 0)
    '''
    convex = Convex()
    #print(convex.same_side(p1, p2, [p3, p4]))
    point = convex.get_points(100)
    convex.force(point)
