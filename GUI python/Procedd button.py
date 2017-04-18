from tkinter import *
import tkinter.messagebox as box
window = Tk()
window.title('test 2')
def dialog():
	var = box.askyesno('Message Box', 'proced?')
	if var == 1:
		box.showing('yes box', 'procedding')
	else:
		box.showwarning('no box', 'canceling')
btn = Button(window, text = 'click', command=dialog)
btn.pack(padx = 150 , pady = 50)
window.mainloop()