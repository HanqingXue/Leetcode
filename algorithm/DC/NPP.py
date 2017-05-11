#Nearesr Point Pair Problem
import random

def NNP(points, start, end):
	if len(points) == 2:
		return points

	points.sort()
	mid = int((start + end)/2)
	left = points[:mid]
	right = points[mid:]
	leftNNP = NNP(left, start, mid)
	rightNNP = NNP(right, mid, end)

	distance_left = leftNNP[1] - leftNNP[0]
	distance_right = rightNNP[1] - rightNNP[0]
	distance_mid = right[0] - left[1]
	min_dis = [distance_left, distance_right, distance_mid]
	if distance_left == min_dis:
	 	return left
	elif distance_right == min_dis:
	 	return right
	else:
	 	return [left[1], right[0]]


if __name__ == '__main__':
	points = random.sample(range(0, 100), 30)
	print points
	NNP(points, 0, 29)
	pass

