from tkinter import *
window = Tk()
window.title('Button Test')
btn_end = Button(window , text = 'close' , command=exit)
def tog():
	if window.cget('bg') == 'blue':
		window.configure(bg = 'gray')
	else:
		window.configure(bg ='blue')
	
btn_tog = Button(window , text = 'switch' , command=tog)
btn_end.pack(padx = 150 , pady = 20)
btn_tog.pack(padx = 250 , pady = 70)
window.mainloop()