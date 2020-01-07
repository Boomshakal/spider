import requests
import json
from tkinter import *
from tkinter.filedialog import askdirectory
import threading

root = Tk()
board = StringVar()
machine = StringVar()
results = StringVar()

def focus_cg(event, e2):
   e2.focus_set()  # 焦点移到e2

def handlerAdaptor(fun, **kwds):
   # 事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧
   return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

def clear_all():
    machine.set('')
    board.set('')

def api_post(board,machine):
    url = 'http://58.250.30.13:55599/pedicure/web/equipment/thirdAddEquipment'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    data = {
        "account": "saiyiPedicure",
        "password": "saiyi_huaan",
        "name": "SmartBidet",
        "code": board,  # 主控板条码
        "type": "2",
        "status": "4",
        "address": "",
        "model": "F1R",
        "machineCode": machine,  # 整机条码
        "provinceAgent": "",
        "cityAgent": "",
        "hotelAgent": ""
    }

    result = requests.post(url=url, json=data, headers=headers)

    if json.loads(result.text)['success']:
        clear_all()
    results.set(result.text)


Label(root, text="主板条码:").grid(row=0, column=0)
Label(root, text="整机条码:").grid(row=1, column=0)
board_entry = Entry(root, textvariable=board).grid(row=0, column=1)

machine_entry = Entry(root, textvariable=machine).grid(row=1, column=1)

Label(root, textvariable=results).grid(row=2, column=0,columnspan=3)
Button(root, text="POST", command=lambda :api_post(board.get(),machine.get())).grid(row=1, column=2)

# #绑定回车键
# board_entry.bind("<Return>", handlerAdaptor(focus_cg,e2 = machine_entry))
# machine_entry.bind("<Return>", api_post(board.get(),machine.get()))

root.mainloop()
