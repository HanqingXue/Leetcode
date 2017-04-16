# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    class Interval(object):
        def __init__(self, s=0, e=0):
            self.start = s
            self.end = e
            
    def BubbleSort(self, intervals):
        '''
        :param intervals:
        :return: sorted intervals by start
        '''
        for i in range(0, len(intervals)):
            for j in range(i, len(intervals)):
                if intervals[i].start > intervals[j].start:
                    intervals[i], intervals[j] = intervals[j], intervals[i]
                elif intervals[i].start == intervals[j].start and intervals[i].end > intervals[j].end:
                    intervals[i], intervals[j] = intervals[j], intervals[i]
                else:
                    pass
                    
        return intervals
    
    def qsort(self, intervals):
        if len(intervals) > 1:
            return self.qsort([x for x in intervals[1:] if x.start < intervals[0].start]) + [intervals[0]] + self.qsort([x for x in intervals[1:] if x.start > intervals[0].start])
        else:
            return intervals
        pass
            
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res_intervals = []
        '''
        So important
        '''
        intervals.sort(key=lambda x: x.start)
        i = 0
        
        while i < len(intervals) - 1:
            if intervals[i+1].start <= intervals[i].end <= intervals[i+1].end:
                intervals[i+1].start = intervals[i].start
            elif intervals[i+1].start <= intervals[i].end and intervals[i+1].end < intervals[i].end:
                intervals[i+1].start = intervals[i].start
                intervals[i+1].end = intervals[i].end
            else:
                pass
            i += 1
            
        intervalsDict = {}
        intervalsStart = set()
        for i in range(0, len(intervals)):
            intervalsStart.add(intervals[i].start)
                
        for start  in  intervalsStart:
            intervalsDict[start] = []
                
        for i in range(0, len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            intervalsDict[start].append(end)
        
        for start in intervalsDict:
            end = max(intervalsDict[start])
            interval = Interval(start, end)
            res_intervals.append(interval)
        
        return res_intervals