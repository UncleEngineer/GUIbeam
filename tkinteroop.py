#tkinteroop.py

from tkinter import *
from tkinter import ttk

class MyButton:

	def __init__(self,gui,text,command=None):
		self.text = text
		self.gui = gui
		self.command = command
		self.BT()

	def BT(self):
		B = ttk.Button(self.gui,text=self.text)
		if self.command != None:
			B.configure(command=self.command)
		B.pack()


class MyLabel:
	def __init__(self,gui,text,row,column,fontSize=15,foreground='red'):
		self.text = text
		self.gui = gui
		E = ttk.Label(self.gui,text=self.text,font=('Angsana New',fontSize),foreground=foreground)
		E.grid(row=row,column=column)

	

GUI = Tk()
GUI.geometry('500x300')

def Sawatdee():
	print('สวัสดีครับ')

B1 = MyButton(GUI,'Hello1',Sawatdee)
B3 = MyButton(GUI,'Hello1')

B2 = ttk.Button(GUI,text='Hello2',command=Sawatdee)
B2.pack()

############LABEL###########
F1 = Frame()
F1.pack()

L1 = MyLabel(F1,'ข้อความ 1',0,0)
L1 = MyLabel(F1,'ข้อความ 2',0,1,20)
L1 = MyLabel(F1,'ข้อความ 3',1,0,25)
L1 = MyLabel(F1,'ข้อความ 4',1,1,30)

GUI.mainloop()