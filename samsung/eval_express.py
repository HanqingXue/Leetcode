#coding=utf-8
from stack import Stack

class EvalExpress(object):
	"""docstring for EvalExpress"""
	def __init__(self, express):
		super(EvalExpress, self).__init__()
		self.express = express
		self.symbol = {'+': 0, '-': 1, '*': 2, '/': 3, '(': 4, ')': 5, '#': 6}
		self.data = Stack()
		self.oper = Stack()
		self.priorMatrix = [
            [2,2,1,1,1,2,2],    #用来进行比较运算符优先级的矩阵,3代表'=',2代表'>',1代表'<',0代表不可比*/  
            [2,2,1,1,1,2,2],  
            [2,2,2,2,1,2,2],  
            [2,2,2,2,1,2,2],  
            [1,1,1,1,1,3,0],  
            [2,2,2,2,0,2,2],  
            [1,1,1,1,1,0,3] 
		]

	def prior(self, oper1, oper2):
		pass

	
	def eval(self):
		isNumber = 0 
		for alpha in  self.express:
			topOper = oper.top()
			if alpha.isdigit():
				self.data.push(alpha)
			
			elif alpha in self.symbol and self.oper.isEmpty():
				self.oper.push(alpha)

			elif self.priorMatrix[self.symbol[alpha]][self.symbol[topOper]] == 2:
				numTop = self.data.top()
				self.data.pop()
				secTop = self.data.top()
				self.data.pop()
				self.data.push( int(numTop) + int(secTop))

			elif alpha == '(':
				self.oper.push(alpha)


				
if __name__ == '__main__':
	 solution = EvalExpress('h1llo');
	 solution.eval()
