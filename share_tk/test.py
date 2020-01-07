# # _*_ coding:utf-8_*_
# # from Tkinter import *
# from tkinter import *
# def submit(ev = None):
#    p.set(u.get())
#
# root = Tk()
# root.title("测试")
# frame = Frame(root)
# frame.pack(padx=8, pady=8, ipadx=4)
# lab1 = Label(frame, text="获取:")
# lab1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
# #绑定对象到Entry
# u = StringVar()
# ent1 = Entry(frame, textvariable=u)
# ent1.grid(row=0, column=1, sticky='ew', columnspan=2)
# lab2 = Label(frame, text="显示:")
# lab2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
# p = StringVar()
# ent2 = Entry(frame, textvariable=p)
# ent2.grid(row=1, column=1, sticky='ew', columnspan=2)
# button = Button(frame, text="输入", command=submit, default='active')
# button.grid(row=2, column=1)
# lab3 = Label(frame, text="")
# lab3.grid(row=2, column=0, sticky=W)
# button2 = Button(frame, text="退出", command=quit)
# button2.grid(row=2, column=2, padx=5, pady=5)
# #以下代码居中显示窗口
# root.update_idletasks()
# x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
# y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
# root.geometry("+%d+%d" % (x, y))
# #以下代码把回车绑定到对象Entry,这样输入完后按回车键就可以看到文字出现在另一个文本框中了。
# ent1.bind("<Return>", submit) #注意这里是Return而不是Enter
# #root.bind("<Return>", submit) #这句把回车绑定到窗口,无论光标在哪按回车会把文本复制
#
# root.mainloop()
#
# rt = Tk()
# ent = Entry(rt)
# ent.pack()
# rt.mainloop()

from tkinter import *


#####################################
###--------------tk----------------
class App:
   def __init__(self, master):
      frame = Frame(master)
      frame.pack(expand=1)
      self.e1 = Entry(frame)
      self.e1.pack()
      self.e2 = Entry(frame)
      self.e2.pack()

      self.e1.bind("<Return>", handlerAdaptor(focus_cg, e2=self.e2))  # tk类不能直接传递参数，需要lambda


def focus_cg(event, e2):
   e2.focus_set()  # 焦点移到e2


def handlerAdaptor(fun, **kwds):
   # 事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧
   return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


if __name__ == '__main__':
   root = Tk()
   app = App(root)
   root.mainloop()

