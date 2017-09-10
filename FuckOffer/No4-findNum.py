#coding = utf-8

def find(A, num):
	col = len(A[0]) - 1
	row = 0
	while col >=0 and row < len(A[0]):
		select  =  A[row][col]
		if select == num:
			return True
		elif select > num:
			col -= 1 
		else:
			row +=1 

	return False
if __name__ == "__main__":
	print find([[1, 2, ], [4, 5, 6]], 7)