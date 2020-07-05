#calculation.py

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวน Beam')
GUI.geometry('500x500')
####################################

def math_additional():
	GUI2 = Toplevel()
	GUI2.title('หน้าต่างคณิตศาสตร์')
	GUI2.geometry('500x400')

	def Add():
		messagebox.showinfo('การบวก','ตัวอย่าง: 1 + 1 = 2')

	img_beam = PhotoImage(file='beam.png')
	logo = ttk.Label(GUI2,text='Beam',image=img_beam)
	logo.pack()
	B = ttk.Button(GUI2,text='ตัวอย่างการบวกเลข',command=Add).pack(ipadx=20,ipady=10)

	GUI2.mainloop()



####################################
menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label='Exit',command=GUI.quit)
menubar.add_cascade(label='File',menu=filemenu)

mathmenu = Menu(menubar,tearoff=0)
mathmenu.add_command(label='การบวก',command=math_additional)
mathmenu.add_command(label='การลบ')
mathmenu.add_command(label='การคูณ')
mathmenu.add_command(label='การหาร')

menubar.add_cascade(label='คณิตศาสตร์',menu=mathmenu)

################TAB#################
Tab = ttk.Notebook(GUI)

T1 = Frame(Tab) #แท็บที่ 1
T2 = Frame(Tab)
T3 = Frame(Tab)

Tab.pack(fill=BOTH, expand=1)

Tab.add(T1,text='Beam')
Tab.add(T2,text='Column')
Tab.add(T3,text='Electricitty')
################TAB#################
# นี่คือรูปที่ใช้แสดงผล
img_beam = PhotoImage(file='beam.png')

logo = ttk.Label(T1,text='Beam',image=img_beam)
logo.pack()


F1 = Frame(T1)
F1.pack()

value1 = StringVar()
value2 = StringVar()
value3 = StringVar()

FONT1 = ('TH Sarabun New',15,'bold')
FONT2 = ('TH Sarabun New',20,'bold')

L = ttk.Label(F1,text='(1) ความกว้าง',font=FONT1)
L.grid(row=0,column=0)
E1 = ttk.Entry(F1,textvariable=value1)
E1.grid(row=0,column=1,pady=10)
############
L = ttk.Label(F1,text='(2) ความสูง',font=FONT1)
L.grid(row=1,column=0)
E2 = ttk.Entry(F1,textvariable=value2)
E2.grid(row=1,column=1,pady=10)
############
L = ttk.Label(F1,text='(3) ความยาว',font=FONT1)
L.grid(row=2,column=0,pady=10)
E3 = ttk.Entry(F1,textvariable=value3)
E3.grid(row=2,column=1,pady=10)

def Calc():
	v1 = float(value1.get()) #.get() ดึงค่ามา
	v2 = float(value2.get())
	v3 = float(value3.get())
	cal = v1 * v2 * v3
	textshow = 'คานคอนกรีตชิ้นนี้มีปริมาตร: {:,.2f} ลบ.ม.'.format(cal)
	v_result.set(textshow) #.set() สั่งให้เปลี่ยนข้อความเป็น textshow


B1=ttk.Button(T1,text='Calculate',command=Calc)
B1.pack(pady=10,ipadx=20,ipady=10)

v_result = StringVar()
v_result.set('----------Result-----------')

Result = ttk.Label(T1,textvariable=v_result,foreground='green',font=FONT2)
Result.pack()

GUI.mainloop()