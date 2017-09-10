



#coding = utf-8 

def replace(s):
	i = 0 
	blankSpace = 0 

	for i in range(0, len(s)):
		if s[i] == ' ':
			blankSpace += 1
			pass
	start = len(s) -1 
	
	for i in range(0, blankSpace*2):
		s += '*'
	end = len(s) 
 	
 	j = len(s) -1 
 	s = list(s)
	while start >= 0 and end > start:
		if s[start] == ' ':
			s[end-1] = '0'
			s[end-2] = '2'
			s[end-3] = '%'
			end -= 3
		else:
			end -= 1
			curItem = s[start]
			print curItem
			s[end] = curItem

		start -= 1
	
	return str(s)

if __name__ == "__main__":
	print replace("hello world")