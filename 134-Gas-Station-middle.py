class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost): return -1
        Sum = 0
        ans = 0
        for i in range(0, len(gas)):
            left = gas[i] - cost[i]
            Sum += left
            if Sum < 0:
                ans = i + 1
                Sum = 0
        return ans