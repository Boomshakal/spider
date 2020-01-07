import tkinter

win = tkinter.Tk()
win.title("鼠标拖动事件")
win.geometry("800x600+600+100")

#<B1-Motion> 拖动左键触发事件
#<B2-Motion> 拖动中键触发事件
#<B3-Motion> 拖动右键触发事件

label=tkinter.Label(win,text="red orange yellow green cyan blue violet拖动鼠标打印")
label.pack()
def func(event):
    print(event.x,event.y)
label.bind("<B1-Motion>",func)

win.mainloop()