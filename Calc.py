# Basic calculator using functions and lambda

def division(x,y):
	try:
		result = x/y
		return result
	except ZeroDivisionError:
		print ('Err: Cannot divide by zero !!!!!')
		return 'Err'

print ('---Welcome to my first calculator---')
print ('This calculator does the following: \n \
	1. Addition \n \
	2. Subtraction \n \
	3. Multiplication \n \
	4. Division \n ')

n1 = int(input('Enter first number:'))
n2 = int(input('Enter second number:'))
action = input('Select action from 1 or 2 or 3 or 4:')

if action == '1':
	print (n1,'+',n2,'=',(lambda x,y: x+y)(n1,n2))
elif action == '2':
	print (n1,'-',n2,'=',(lambda x,y: x-y)(n1,n2))
elif action == '3':
	print (n1,'*',n2,'=',(lambda x,y: x*y)(n1,n2))
elif action == '4':
	print (n1,'/',n2,'=',division(n1,n2))
else:
	print ('Wrong input !!!!!')
