#include <iostream>
#include <cstring>
#include <string>
#include <stack>
using namespace std;

template <class T>
void StackClear(stack<T> &s)			
{
	while (!s.empty())
		s.pop();
}


int IsOperator(char c)
{
	switch (c)
	{
	case '+':
	case '-':
	case '*':
	case '/':
	case '(':
	case ')':
	case '=':
		return 1;
		break;
	default:
		return 0;
		break;
	}
}


int Priority(char oper1, char oper2)
{
	int pri;
	switch (oper2)
	{
	case '+':
	case '-':
		if (oper1 == '(' || oper1 == '=')
			pri = -1;
		else
			pri = 1;
		break;

	case '*':
	case '/':
		if (oper1 == '*' || oper1 == '/' || oper1 == ')')
			pri = 1;
		else
			pri = -1;
		break;

	case '(':
		if (oper1 == ')')		
		{
			cout << "Invalid expression\n";
			return 0;
		}
		else
			pri = -1;
		break;

	case ')':
		if (oper1 == '(')
			pri = 0;		 
		else
			pri = 1;
		break;

	case '=':
		if (oper1 == '(')
		{
			cout << "Invalid expression\n";
			return 0;
		}
		else if (oper1 == '=')
			pri = 0;	
		else
			pri = 1;
		break;
	}
	return pri;
}


double calculate(double a, int oper, double b)
{
	switch (oper)
	{
	case '+': return a + b;
	case '-': return a - b;
	case '*': return a*b;
	case '/':
		if (b != 0)
			return a / b;
		else
		{
			cout << "Invalid expression\n";
			return 0;
		}
	}
}


double NumberSplicing(char ch[])
{
	int dot = 0; 	
	double temp = 0;
	static int len = 10;

	for (int n = 0; n<strlen(ch); n++)
	{
		char c = ch[n];
		if (c == '.')
			dot = 1;	
		else
		{
			c -= '0';		
			if (dot == 0)
				temp = temp * 10 + c;
			else
			{
				temp = temp + (double)c / len;  
				len *= 10;					  
											  
			}
		}

	}



	return temp;
}


double CalcExp(string express)
{
	express += "=";
	double a, b;			
	char opera;				
	char c;					
	char x;					
	stack<char> oper;
	stack<double> data;	
	char tempNum[20];		
	int j = 0;

	int i = 0, flag = 0;		

	oper.push('=');			

	c = express[i++];
	double num = 0;


	while (c != '=' || x != '=')			
	{
		if (IsOperator(c))	
		{
			if (flag)		
			{
				tempNum[j] = 0;
				j = 0;
				num = NumberSplicing(tempNum);	
												
				data.push(num);			
				num = 0; 				
				flag = 0;				
			}

			switch (Priority(x, c))
			{
			case -1:	
				oper.push(c);		
				c = express[i++];		
				break;

			case 0:					
				oper.pop();			
				c = express[i++];		
				break;

			case 1:						
				opera = oper.top();		
				oper.pop();				

				b = data.top();
				data.pop();
				a = data.top();
				data.pop();				
				double t = calculate(a, opera, b);	
				data.push(t);		
				break;
			}
		}

		else if (c >= '0' && c <= '9' || c == '.')	
		{
			tempNum[j++] = c;
			flag = 1; 				
			c = express[i++];
		}
		else
		{
			cout << "Invalid expression\n";
			return 0;
		}

		x = oper.top();		
							
	}

	num = data.top();

	StackClear(oper);
	StackClear(data);		
							

	return 	num;	

}

bool is_express_valid(string express)
{
	long len = express.length();
	int flag = -1;
	int lb_num = 0;

	for (int i = 0; i < len; i++)
	{
		if (express[i] >= '0'&&express[i] <= '9')//是数字
		{
			if (flag != -1 && flag == 2)
			{
				return false;
			}
			flag = 0;
		}
		else if (express[i] == '(')//是左括号
		{
			if (flag != -1 && (flag == 0 || flag == 2))
			{
				return false;
			}
			flag = 1;
			lb_num++;

		}
		else if (express[i] == ')')//是右括号
		{
			if (flag != -1 && (flag == 1 || flag == 3))
			{
				return false;
			}
			flag = 2;
			lb_num--;
			if (lb_num < 0)
			{
				return false;
			}
		}
		else if (express[i] == '+' || express[i] == '-' || express[i] == '*' || express[i] == '/')//是操作符
		{
			if (flag != -1 && (flag == 1 || flag == 3))
			{
				return false;
			}
			flag = 3;
		}
		else
		{

			return false;
		}
	}

	if (lb_num > 0)
	{
		return false;
	}

	return true;

}



int main()
{
	string express;
	cin >> express;
	if (!is_express_valid(express)) 
	{
		cout << "Invalid expression\n";
	}
	cout << CalcExp(express) << endl;
	return 0;
}