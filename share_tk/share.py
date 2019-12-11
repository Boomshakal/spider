import os


from tkinter import *
from tkinter.filedialog import askdirectory
import threading

root = Tk()
path = StringVar()
port = StringVar()
def selectPath():
    path_dir = askdirectory()
    path.set(path_dir)


def share(path,port):
    os.chdir(path)
    os.system('python -m http.server {port}'.format(port=port))

def exec_share(path,port):
    th=threading.Thread(target=share,args=(path,port,))
    th.setDaemon(False)
    th.start()

def stop_server(server):
    server.sorket.close()

Label(root, text="目标路径:").grid(row=0, column=0)
Label(root, text="端口号:").grid(row=1, column=0)
Entry(root, textvariable=path).grid(row=0, column=1)
Entry(root, textvariable=port).grid(row=1, column=1)
Button(root, text="路径选择", command=selectPath).grid(row=0, column=2)
Button(root, text="共享", command=lambda :exec_share(path.get(),port.get())).grid(row=1, column=2)
# Button(root, text="停止", command=lambda :stop_server()).grid(row=1, column=2)

root.mainloop()