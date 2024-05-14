import tkinter as tk
from tkinter import ttk
master=tk.Tk()

def inp_by_column():
   columns=[]
   for column in range(0,5):
      columns.append([])
      for row in range(0,3):
         inp=inputobjects[row][column].get()
         if inp=='':
            inp=0
         columns[column].append(int(inp))
   return columns

def get_inputs():
    rows=[]
    for row in range (0,3):
          rows.append([])
          for column in range (0,5):
             rows[row].append(0)
             inp=inputobjects[row][column].get()
             rows[row][column]=inp
def tocolumns(rows):
   columns=[]
   for column in range(0,5):
      columns.append([])
      for row in range(0,3):
         columns[column].append(rows[row][column])
   return columns
def calculate(columns):
   newcolumns=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
   for columnnum in range(0,5):
      origcolumn=columns[columnnum]
      inorder=sorted(origcolumn)

      newcolumns[columnnum][0]=inorder[2]- inorder[1]
      newcolumns[columnnum][1]=inorder[1]-inorder[0]
      newcolumns[columnnum][2]=inorder[0]
         
   return newcolumns
         
def display(columns):
   for row in range (0,3):
      for column in range (0,5):
         out=columns[column][row]
         if out==0:
            out=''
         outputobjects[row][column].configure(text=out)



master.title("Key Master")
inputobjects=[]
outputobjects=[]

inlabel = tk.Label(text="- - input - -")
inlabel.grid(row=0,column=3)
outlabel = tk.Label(text="- - output - -")
outlabel.grid(row=4,column=3)

a = tk.Label(text="Master 1")
a.grid(row=1,column=0)
b = tk.Label(text="Master 2")
b.grid(row=2,column=0)
f = tk.Label(text="specific")
f.grid(row=3,column=0)
c = tk.Label(text="key pin 3")
c.grid(row=5,column=0)
d = tk.Label(text="key pin 2")
d.grid(row=6,column=0)
e = tk.Label(text="key pin 1")
e.grid(row=7,column=0)


for row in range (0,3):
   inputobjects.append([])
   for column in range (0,5):
      r=row+1
      c=column+1
      inputobjects[row].append(tk.Entry(master))
      inputobjects[row][column].grid(row=r,column=c)
      
for row in range (0,3):
   outputobjects.append([])
   for column in range (0,5):
      r=row+5
      c=column+1
      outputobjects[row].append(tk.Label(master,text="?", bg="white"))
      outputobjects[row][column].grid(row=r,column=c)
      



while 1:
   

   
   master.update()
   w=inp_by_column()
   x=calculate(w)
   display(x)

 
