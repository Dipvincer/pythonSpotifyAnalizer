
from PIL import ImageTk, Image
import tkinter as tki
import tkinter.ttk as ttk
import os
from tkinter.ttk import Notebook , Frame ,Button ,Label
import numpy as np
import pandas as pd
from tkinter import messagebox 
from settings import cfon, cknop, font, text_path, graph_path
import service
from tkinter import colorchooser
import tkinter.filedialog as fd

root=tki.Tk()
root.title('Приложение')
root.geometry('850x500')
root.resizable(False, False)
root.iconbitmap('C:\\Users\\Admin\\Desktop\\python_sem\\spot.ico')
root.configure(bg='LimeGreen')
path = os.getcwd()
shrift= (font, 10)
def click_info():  
    messagebox.showinfo('Справка', 'Авторы : \n Климкин Дмитрий \n Шаймарданов Эдуард \n Ермаков Сергей \n Бутенко Елизавета\nГруппа : БИВ216')  

#это настройки , где можно выбрать цвета для фона и кнопок , а также места для сохранения отчетов
# def settings_window():
#     def zav1():
#         service.zav(canvas1, canvas2, combobox, entr1, entr2)
#     root2 = tki.Toplevel(root)
#     root2.title("Настройки")
#     root2.geometry('620x250+360+280')
#     root2.resizable(False, False)
#     root2.configure(bg='LimeGreen')    
#     tki.Label(root2, text='Место хранения текстовых отчётов', bg='black',
#               fg="White", bd=3, font=shrift).grid(row=0, column=0, pady=1)
#     tki.Label(root2, text='Место хранения графических отчётов', bg='black',
#               fg="White", bd=3, font=shrift).grid(row=1, column=0, pady=1)
#     tki.Label(root2, text='Шрифт', bg='black', fg="White", bd=3, font='Tahoma').grid(row=2, column=0, pady=1)
#     tki.Label(root2, text='Цвет фона', bg='black',
#               fg="White", bd=3, font=shrift).grid(row=3, column=0, pady=1)
#     tki.Label(root2, text='Цвет кнопок', bg='black',
#               fg="White", bd=3, font=shrift).grid(row=4, column=0, pady=1)
#     canvas1 = tki.Canvas(root2, width=20, height=20, bg='LimeGreen')
#     canvas1.grid(row=3, column=1, sticky='w')
#     canvas2 = tki.Canvas(root2, width=20, height=20, bg='black')
#     canvas2.grid(row=4, column=1, sticky='w')
#     def fon():
#         fon = colorchooser.askcolor()
#         root2.lift()
#         canvas1['bg'] = fon[1]

#     def knop():
#         knop = colorchooser.askcolor()
#         root2.lift()
#         canvas2['bg'] = knop[1]

#     def dialog(entry):       
#         new_path = fd.askdirectory(initialdir=os.getcwd())
#         root2.lift()
#         if new_path:
#             entry['state'] = 'normal'
#             entry.delete(0, 'end')
#             entry.insert(0, os.path.normpath(new_path))
#             entry['state'] = 'readonly'
#     def save_set():
        
#         service.save_configurations(r'.C:\Users\Admin\Desktop\python_sem',
#                                     (entr1.get(), entr2.get(), combobox.get(),
#                                       canvas1['bg'], canvas2['bg']))
#         root2.destroy()
#     tki.Button(root2, text="...", bg="Black", fg="White", bd=3,
#               font=shrift, command=lambda: dialog(entr1)).grid(row=0, column=2, padx=10)
#     tki.Button(root2, text="...", bg="Black", fg="White", bd=3,
#               font=shrift, command=lambda: dialog(entr2)).grid(row=1, column=2, padx=10)
#     tki.Button(root2, text="Выбрать цвет", bg="Black", fg="White", bd=3,
#               font=shrift, command=fon).grid(row=3, column=1, padx=10)
#     tki.Button(root2, text="Выбрать цвет", bg="Black", fg="White", bd=3,
#               font=shrift, command=knop).grid(row=4, column=1, padx=10)
#     tki.Button(root2, text="Настройки по умолчанию", bg="Black", fg="White", bd=3,
#               font=shrift, command=zav1).grid(row=5, column=0, padx=10)
#     tki.Button(root2, text="Сохранить", bg="Black", fg="White", bd=3,
#               font=shrift, command=save_set).grid(row=5, column=1, padx=10, sticky='e', pady=30)
#     entr1 = tki.Entry(root2, font='Tahoma', width=30)
#     entr1.insert(0, text_path)
#     entr1['state'] = 'readonly'
#     entr2 = tki.Entry(root2, font='Tahoma', width=30)
#     entr2.insert(0, graph_path)
#     entr2['state'] = 'readonly'

#     #Раскрывающийся список
#     combobox = ttk.Combobox(root2, state='readonly', width=28, font=shrift)
#     combobox['values'] = ['Tahoma', 'Calibri', 'Times New Roman', 'Arial']
#     combobox.set(font)

#     entr1.grid(row=0, column=1)
#     entr2.grid(row=1, column=1)
#     combobox.grid(row=2, column=1)
    
    
def settings_w():
    root_set = tki.Toplevel(root)
    root_set.title("Настройки")
    root_set.geometry('620x250')
    root_set.resizable(False, False)
    root_set.configure(bg='LimeGreen')    
    tki.Label(root_set, text='Место хранения текстовых отчётов', bg='black',
                  fg="White", bd=3, font=shrift).grid(row=0, column=0, pady=1)
    tki.Label(root_set, text='Место хранения графических отчётов', bg='black',
                  fg="White", bd=3, font=shrift).grid(row=1, column=0, pady=1)
    tki.Label(root_set, text='Шрифт', bg='black', fg="White", bd=3, font='Tahoma').grid(row=2, column=0, pady=1)
    tki.Label(root_set, text='Цвет фона', bg='black',
                  fg="White", bd=3, font=shrift).grid(row=3, column=0, pady=1)
    tki.Label(root_set, text='Цвет кнопок', bg='black',
                  fg="White", bd=3, font=shrift).grid(row=4, column=0, pady=1)
    
    
def mainWindow():
    root3 = tki.Toplevel(root)
    root3.title("Главное окно")
    root3.geometry('620x500')
    root3.resizable(False, False)
    root3.configure(bg=cfon)
    def data_base():
        root_db=tki.Toplevel(root3)
        root_db.title("Работа с базой данных")
        root_db.geometry('620x500')
        root_db.resizable(False, False)
        root_db.configure(bg=cfon)
        
    but_bd=tki.Button(root3,text='Работа с базой данных',font=('Times',12,'italic')
                         , bg='black', fg='white',command=data_base).grid(row=0,column=0)
    # tabs_control=Notebook(root3,height=400,width=500,padding=(10,10,10))
    # tab1=Frame(tabs_control)
    # tabs_control.add(tab1,text="Работа с базой данных")
    # tabs_control.grid(row=0,column=0)

    # tab2=Frame(tabs_control)
    # tabs_control.add(tab2,text="Работа с отчетами")
    # #tabs_control.grid(row=0,column=1)
    
    # tab3=Frame(tabs_control)
    # tabs_control.add(tab3,text="Работа с графиками")
    # #tabs_control.grid(row=0,column=2)
    # # Button(tab1,text='Кнопка 1',font=('Times',12,'italic')
    # #                       , bg='black', fg='white').pack()
    # # Button(tab1,text='Кнопка 2',font=('Times',12,'italic')
    # #                       , bg='black', fg='white').grid(row=1,column=0)
    # # Button(tab1,text='Кнопка 3',font=('Times',12,'italic')
    # #                       , bg='black', fg='white').grid(row=2,column=0)
    
    # root.withdraw()
    # but_edit = Button(tab1,text="Изменить ")

    # but_edit.grid(column=1,
    #         row=1,
    #         padx=40,
    #         pady=40)
    # but_add = Button(tab1,text="Добавить")

    # but_add.grid(column=1,
    #         row=3,
    #         padx=40,
    #         pady=40)
    # but_del = Button(tab1,text="Удалить")

    # but_del.grid(column=1,
    #         row=5,
    #         padx=40,
    #         pady=40)
    def go_back():
        root3.withdraw()
        #root3.destroy()
        root.deiconify()
    b=tki.Button(root3,text='Назад',font=('Times',12,'italic')
                         , bg='black', fg='white',command=go_back)
    b.grid(row=0,column=1)
   
    

    
btn_start=tki.Button(root,text='Начать',font=('Times',16,'italic')
                     , bg='black', fg='white',command=mainWindow)
btn_start.place(x=390,y=200)
btn_set=tki.Button(root,text='Настройки',font=('Times',16,'italic')
                     , bg='black', fg='white',command=settings_w)
btn_set.place(x=372,y=250)
btn_info=tki.Button(root,text='Информация',font=('Times',16,'italic')
                     , bg='black', fg='white',command=click_info)
btn_info.place(x=362,y=300)
btn_close=tki.Button(root,text='Выйти',font=('Times',16,'italic')
                     , bg='black', fg='white',command=root.destroy)
btn_close.place(x=620+137,y=500-50)


root.mainloop()
