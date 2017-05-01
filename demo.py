#coding=utf-8
import math
import numpy
import pylab as pl
#画原始图
def drawGraph(x,y):
	pl.figure(1)
	pl.subplot(131) #1
	pl.title("ConvexHull-GrahamScan")
	pl.xlabel("x axis")
	pl.ylabel("y axis")
	pl.plot(x,y,'ro')
	pl.subplot(132) #2
	pl.title("ConvexHull-BruteForce")
	pl.xlabel("x axis")
	pl.ylabel("y axis")
	pl.plot(x,y,'ro')
	pl.subplot(133) #3
	pl.title("ConvexHull-DivideConquer")
	pl.xlabel("x axis")
	pl.ylabel("y axis")
	pl.plot(x,y,'ro')
#画凸包
def drawCH(CHQ):
	x,y=[],[]
	for p in CHQ:
		x.append(p[0])
		y.append(p[1])
	pl.plot(x,y,color='blue',linewidth=2)
	pl.plot(x[-1],y[-1],x[0],y[0])
	lastx=[x[-1],x[0]]
	lasty=[y[-1],y[0]]
	pl.plot(lastx,lasty,color='blue',linewidth=2)   #画最后一条封闭线
#存点的矩阵,每行一个点,列0->x坐标,列1->y坐标,列2->代表极角
def matrix(rows,cols):
	cols=3
	mat = [[0 for col in range (cols)]
			  for row in range(rows)]
	return mat
#Graham用的叉积
def crossMut(stack,p3):
	p2=stack[-1]
	p1=stack[-2]
	vx,vy=(p2[0]-p1[0],p2[1]-p1[1])
	wx,wy=(p3[0]-p1[0],p3[1]-p1[1])
	return (vx*wy-vy*wx)
#Graham扫描法O(nlogn),mat是经过极角排序的点集
def GrahamScan(x,y):
	#print mat
	max_num=len(x)
	mat = matrix(max_num,3) #根据点数申请矩阵,mat[i][2]代表极角
	minn = 300
	for i in range(max_num):	#存点集
		mat[i][0],mat[i][1]=x[i],y[i]
		if y[i]<minn: #(x[tmp],y[tmp])-->y轴最低坐标
			minn=y[i]
			tmp = i
	d = {}  #利用字典的排序
	for i in range(max_num):	#计算极角
		if (mat[i][0],mat[i][1])==(x[tmp],y[tmp]):mat[i][2]=0
		else:mat[i][2]=math.atan2((mat[i][1]-y[tmp]),(mat[i][0]-x[tmp]))
		d[(mat[i][0],mat[i][1])]=mat[i][2]
	lst=sorted(d.items(),key=lambda e:e[1]) #按极角由小到大排序
	for i in range(max_num):	#更新mat为排序后的矩阵
		((x,y),eth0)=lst[i]
		mat[i][0],mat[i][1],mat[i][2]=x,y,eth0
	points=len(mat) #点数
	stack=[]
	stack.append((mat[0][0],mat[0][1])) #push p0
	stack.append((mat[1][0],mat[1][1])) #push p1
	stack.append((mat[2][0],mat[2][1])) #push p2
	for i in range(3,points):
		#print stack
		p3=(mat[i][0],mat[i][1])
		while crossMut(stack,p3)<0:stack.pop()
		stack.append(p3)
	return stack
#蛮力法判断叉积，返回ABxAC的向量中j的系数
def Product(A,B,C):
	return (B[0]-A[0])*(C[1]-A[1])-(C[0]-A[0])*(B[1]-A[1])
#判断P是否在三角形ABC中
def isInTriangle(A,B,C,P):
	if Product(A,B,P)>=0 and Product(B,C,P)>=0 and Product(C,A,P)>=0:
		return 1
	return 0
#凸包蛮力算法
def BruteForce(x,y):
	max_num=len(x)
	mat = matrix(max_num,3) #根据点数申请矩阵,mat[i][2]代表访问标记
	for i in range(max_num):	#存点集
		mat[i][0],mat[i][1],mat[i][2]=x[i],y[i],1
	#任选4个,即C(10,4)的功能
	for a in range(0,max_num-3):
		for b in range(a+1,max_num-2):
			for c in range(b+1,max_num-1):
				for d in range(c+1,max_num):
					#如果在三角形中,则删除内部的点
					#if 0 in (mat[a][2],mat[b][2],mat[c][2],mat[d][2]):continue
					if isInTriangle(mat[b],mat[c],mat[d],mat[a]):mat[a][2]=0	#顺时针算一类
					if isInTriangle(mat[b],mat[d],mat[c],mat[a]):mat[a][2]=0	#逆时针算另一类					
					if isInTriangle(mat[a],mat[c],mat[d],mat[b]):mat[b][2]=0
					if isInTriangle(mat[a],mat[d],mat[c],mat[b]):mat[b][2]=0
					if isInTriangle(mat[a],mat[b],mat[d],mat[c]):mat[c][2]=0
					if isInTriangle(mat[a],mat[d],mat[b],mat[c]):mat[c][2]=0
					if isInTriangle(mat[a],mat[b],mat[c],mat[d]):mat[d][2]=0
					if isInTriangle(mat[a],mat[c],mat[b],mat[d]):mat[d][2]=0
	#后处理,按极角排序,以便输出图形
	#print mat
	newmat = matrix(max_num,3)  #newmat[i][2]是极角,和mat[i][2]不同
	pos = 0 #记录newmat行数
	minn = 300
	for i in range(len(mat)):
		if mat[i][2]==1:
			if mat[i][1]<minn: #(mat[tmp][0],mat[tmp][1])-->y坐标最低的点
				minn=mat[i][1]
				tmp = i
			newmat[pos][0],newmat[pos][1]=mat[i][0],mat[i][1]
			pos+=1
	d={}	#排序字典
	for i in range(pos):	#计算极角
		#print newmat[i][0],newmat[i][1],newmat[i][2]
		if (newmat[i][0],newmat[i][1])==(mat[tmp][0],mat[tmp][1]):newmat[i][2]=0
		else:newmat[i][2]=math.atan2((newmat[i][1]-mat[tmp][1]),(newmat[i][0]-mat[tmp][0]))
		d[(newmat[i][0],newmat[i][1])]=newmat[i][2]
	lst=sorted(d.items(),key=lambda e:e[1]) #按极角由小到大排序
	#print lst
	stack=[]
	for i in range(pos):	#更新mat为排序后的矩阵
		((x,y),eth0)=lst[i]
		stack.append((x,y))
	return stack
#凸包分治算法
def DivideConquer(x,y):
	max_num=len(x)
	d={}
	for i in range(max_num):
		d[(x[i],y[i])]=x[i]
	#print d
	lst=sorted(d.items(),key=lambda e:e[1]) #首先将点集按x坐标排序
	#for k in lst:print k
	#print
	left=len(lst)/2  #左边的个数
	right=len(lst)-left #右边的个数
	#print left,right
	x,y=[],[]   #画左半部分
	for i in range(left):   
		((xi,yi),noUse)=lst[i]
		x.append(xi)
		y.append(yi)
	CHQ_L=GrahamScan(x,y)
	#print CHQ_L
	x,y=[],[]   #画右半部分
	for i in range(right):  
		((xi,yi),noUse)=lst[left+i]
		x.append(xi)
		y.append(yi)
	CHQ_R=GrahamScan(x,y)
	for i in range(len(CHQ_R)): #找到y最高的位置high
		if i==len(CHQ_R)-1 or CHQ_R[i][1]>CHQ_R[i+1][1]:
			high = i
			break
	#将右半部分分成两个序列
	sq2=[]
	for i in range(high+1):
		sq2.append((CHQ_R[i][0],CHQ_R[i][1]))
	#print sq2
	sq3=[]
	for i in range(len(CHQ_R)-1,high,-1):
		sq3.append((CHQ_R[i][0],CHQ_R[i][1]))
	#print sq3
	merge = CHQ_L+sq2+sq3   #合并操作，应该按顺序来merge
	#print merge
	x,y=[],[]   #画左半部分
	for i in range(len(merge)):   
		((xi,yi))=merge[i]
		x.append(xi)
		y.append(yi)
	CHQ=GrahamScan(x,y)
	return CHQ
#main
max_num = 30 #最大点数
x=100*numpy.random.random(max_num)#[0,100)
y=100*numpy.random.random(max_num)
drawGraph(x,y)  #原始图
CHQ=GrahamScan(x,y)
pl.subplot(131)
drawCH(CHQ)	 #Graham凸包
CHQ=BruteForce(x,y)
pl.subplot(132)
drawCH(CHQ)	 #BruteForce凸包
CHQ=DivideConquer(x,y)
pl.subplot(133)
drawCH(CHQ)	 #DivideConquer凸包
pl.show()
