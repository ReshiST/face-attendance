import tkinter  as tk
window=tk.Tk()
# add widgets here

window.title('Face Detection Project')
window.geometry("900x500")
l1=tk.Label(window,text="Name",font=(20))
cam=tk.Entry(window,width=50)
l1.grid(column=0,row=0)
cam.grid(column=1,row=0)
window.mainloop()