from cmath import sqrt
from multiprocessing.util import is_abstract_socket_namespace
from random import randint, random
from re import T
from tkinter import *
import math
win=Tk()

w = 1100
h = 1100
screen_resolution = str(w)+'x'+str(h)
win.geometry(screen_resolution)
canvas=Canvas(win, width= w-90, height=h-90)
canvas.pack(padx=10,pady=10)
fn = []
step = 0
count = 10
o = 0
for k in range(1,h-100):
	is_prime = True
	step += 1
	l = k*10
	if step == 100:
		step = 0
		count += 10
		o += 1
		canvas.create_text(((l-(o*1000))+10),count, text=0)
	else:
		canvas.create_text(((l-(o*1000))+10),count, text=0)
	print(l-(o*1000))
	for j in range(2,int(k/2)):
		if k%j==0:  
			is_prime= False
			break
	if k == 4:
		is_prime = False	
	if is_prime:
		fn.append(k) 
		canvas.create_text(l-(o*1000)+10,count, text=X)
	def draw(element):
		if is_prime == True:
			text = '1'
		else:
			text = '0'
print(fn)
	
	

win.mainloop()