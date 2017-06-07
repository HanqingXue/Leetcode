import sys 



def LIS(num=list):
	Sum = [sys.maxint]*len(num)
	Sum[0] = num[0]
	for i in range(1, len(num)):
		if num[i] > Sum[i-1]:
			Sum[i-1] = 0 
		Sum[i] = max(Sum[i-1], Sum[i-1] + num[i])

	return Sum[-1]


def maxSubSeq(num=list):
	thisSum , maxSum = 0, 0

	for j in range(0, len(num)):
		thisSum += num[j]
		
		if thisSum > maxSum:
			maxSum = thisSum
		
		elif thisSum < 0:
			thisSum =0 

	return maxSum

if __name__ == '__main__':
	a = LIS([-2, 11, -4, 13, -5, 2])
	b = maxSubSeq([-2, 11, -4, 13, -5, 2])
	print a
	print b
