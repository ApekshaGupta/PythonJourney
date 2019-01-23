# Simple GUI calculator using tkinter

import tkinter

expression = "" #global variable

# Functions here
def press(val):
	global expression
	expression = expression + str(val)
	eqn.set(expression)

def clear():
	global expression
	expression = ""
	eqn.set("")

def calculate():
	try:
		global expression
		expression = str(eval(expression))
		eqn.set(expression)
		expression = ""
	except:
		eqn.set("error")
		expression = ""	

# Driver module
if __name__ == "__main__":
	# Parent window configuration
	root = tkinter.Tk() 	# root is the main window object
	root.title('Simple Calculator')
	root.configure(background='green')
	root.geometry('370x150')

	# widgets below
	eqn = tkinter.StringVar()
	expression_textfield = tkinter.Entry(root, textvariable=eqn)
	expression_textfield.grid(columnspan=4, ipadx=100)
	eqn.set('Enter your expression here:')
	#Row1
	b1 = tkinter.Button(root, text='1', fg='black', bg='red', command=lambda : press(1),height=1, width=7)
	b1.grid(row=2,column=0)
	b2 = tkinter.Button(root, text='2', fg='black', bg='red', command=lambda : press(2),height=1, width=7)
	b2.grid(row=2,column=1)
	b3 = tkinter.Button(root, text='3', fg='black', bg='red', command=lambda : press(3),height=1, width=7)
	b3.grid(row=2,column=2)
	add = tkinter.Button(root, text='+', fg='black', bg='red', command=lambda : press('+'),height=1, width=3)
	add.grid(row=2,column=3)
	#Row2
	b4 = tkinter.Button(root, text='4', fg='black', bg='red', command=lambda : press(4),height=1, width=7)
	b4.grid(row=3,column=0)
	b5 = tkinter.Button(root, text='5', fg='black', bg='red', command=lambda : press(5),height=1, width=7)
	b5.grid(row=3,column=1)
	b6 = tkinter.Button(root, text='6', fg='black', bg='red', command=lambda : press(6),height=1, width=7)
	b6.grid(row=3,column=2)
	sub = tkinter.Button(root, text='-', fg='black', bg='red', command=lambda : press('-'),height=1, width=3)
	sub.grid(row=3,column=3)
	#Row3
	b7 = tkinter.Button(root, text='7', fg='black', bg='red', command=lambda : press(7),height=1, width=7)
	b7.grid(row=4,column=0)
	b8 = tkinter.Button(root, text='8', fg='black', bg='red', command=lambda : press(8),height=1, width=7)
	b8.grid(row=4,column=1)
	b9 = tkinter.Button(root, text='9', fg='black', bg='red', command=lambda : press(9),height=1, width=7)
	b9.grid(row=4,column=2)
	mul = tkinter.Button(root, text='x', fg='black', bg='red', command=lambda : press('*'),height=1, width=3)
	mul.grid(row=4,column=3)
	#Row4
	bc = tkinter.Button(root, text='Clear', fg='black', bg='red', command=clear ,height=1, width=7)
	bc.grid(row=5,column=0)
	b0 = tkinter.Button(root, text='0', fg='black', bg='red', command=lambda : press(0),height=1, width=7)
	b0.grid(row=5,column=1)
	be = tkinter.Button(root, text='=', fg='black', bg='red', command=calculate, height=1, width=7)
	be.grid(row=5,column=2)
	div = tkinter.Button(root, text='/', fg='black', bg='red', command=lambda : press('/'),height=1, width=3)
	div.grid(row=5,column=3)
	# widgets above

	root.mainloop() 	# to run the application

