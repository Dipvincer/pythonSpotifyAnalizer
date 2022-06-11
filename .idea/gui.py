from PIL import ImageTk, Image
import tkinter as tki
import tkinter.ttk as ttk
import os
from tkinter.ttk import Notebook , Frame ,Button ,Label , Treeview , Scrollbar
import numpy as np
import pandas as pd
from tkinter import messagebox 
from settings import cfon, cknop, font, text_path, graph_path
import service
from tkinter import colorchooser
import tkinter.filedialog as fd
from tkinter import *
from tkinter import ttk, filedialog

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
    def go_back():
        root3.withdraw()
        #root3.destroy()
        root.deiconify()
    root3 = tki.Toplevel(root)
    root3.title("Главное окно")
    root3.geometry('620x500')
    root3.resizable(False, False)
    root3.configure(bg=cfon)
    style = ttk.Style()
    style.theme_use('clam')
    frame = Frame(root3)
    frame.pack(side=BOTTOM,pady=20,padx=20,fill=BOTH)
    def option_change():
        columns=['Название','Артист','Коллаборация','Жанр','Страна','Год','Альбом','BPM','Громкость','Длина','Популярность','Прослушиваний в месяц','Прослушиваний всего','Лейбл']
        filename = 'C:\\Users\\Admin\\Desktop\\112.xlsx'
        df = pd.read_excel(filename)
        num=len(df)
        root_c=tki.Toplevel(root3)
        
        root_c.geometry('620x500')
        root_c.resizable(False, False)
        root_c.configure(bg=cfon)
        root_c.title('Изменение записи в БД')
        Lb1=tki.Label(root_c,text='Выберите номер записи для измения',font=('Times',16,'italic'),bg=cfon,fg='black')
        Lb1.place(x=10,y=10)
        value=list(range(1,num+2))
        Vibor = ttk.Combobox(root_c,values=value)
        Vibor.place(x=10,y=50)
        for i in range(len(columns)):
            tki.Label(root_c,text=columns[i],font=('Times',16,'italic'),bg=cfon,fg='black').place(x=10,y=50+30*(i+1))
        name=StringVar()
        a=StringVar()
        k=StringVar()
        g=StringVar()
        c=StringVar()
        y=StringVar()
        al=StringVar()
        bpm=StringVar()
        l=StringVar()
        dl=StringVar()
        p=StringVar()
        m=StringVar()
        vs=StringVar()
        lbl=StringVar()
        array=[name,a,k,g,c,y,al,bpm,l,dl,p,m,vs,lbl]
        for i in range(len(array)):
            tki.Entry(root_c,textvariable=array[i]).place(x=230,y=52+30*(i+1))
        change=tki.Button(root_c,text='Изменить',font=('Times',16,'italic'),bg=cfon,fg='black').place(x=400,y=250)
     def option_add():
        columns=['Название','Артист','Коллаборация','Жанр','Страна','Год','Альбом','BPM','Громкость','Длина','Популярность','Прослушиваний в месяц','Прослушиваний всего','Лейбл']
        filename = 'C:\\Users\\Admin\\Desktop\\112.xlsx'
        df = pd.read_excel(filename)
        num=len(df)
        root_c=tki.Toplevel(root3)
        
        root_c.geometry('620x500')
        root_c.resizable(False, False)
        root_c.configure(bg=cfon)
        root_c.title('Добавление записи в БД')
        for i in range(len(columns)):
            tki.Label(root_c,text=columns[i],font=('Times',16,'italic'),bg=cfon,fg='black').place(x=10,y=0+35*(i))
        name=StringVar()
        a=StringVar()
        k=StringVar()
        g=StringVar()
        c=StringVar()
        y=StringVar()
        al=StringVar()
        bpm=StringVar()
        l=StringVar()
        dl=StringVar()
        p=StringVar()
        m=StringVar()
        vs=StringVar()
        lbl=StringVar()
        array=[name,a,k,g,c,y,al,bpm,l,dl,p,m,vs,lbl]
        for i in range(len(array)):
            tki.Entry(root_c,textvariable=array[i]).place(x=230,y=2+35*(i))
        change=tki.Button(root_c,text='Добавить',font=('Times',16,'italic'),bg=cfon,fg='black').place(x=400,y=250) 
    def option_del():
        columns=['Название','Артист','Коллаборация','Жанр','Страна','Год','Альбом','BPM','Громкость','Длина','Популярность','Прослушиваний в месяц','Прослушиваний всего','Лейбл']
        filename = 'C:\\Users\\Admin\\Desktop\\112.xlsx'
        df = pd.read_excel(filename)
        num=len(df)
        root_c=tki.Toplevel(root3)
        root_c.geometry('500x100')
        root_c.resizable(False, False)
        root_c.configure(bg=cfon)
        root_c.title('Удаление записи из БД')
        Lb1=tki.Label(root_c,text='Выберите номер записи для удаления',font=('Times',16,'italic'),bg=cfon,fg='black')
        Lb1.grid(row=0,column=0)
        value=list(range(1,num+2))
        Vibor = ttk.Combobox(root_c,values=value)
        Vibor.grid(row=1,column=0)
        change=tki.Button(root_c,text='Удалить',font=('Times',16,'italic'),bg=cfon,fg='black').grid(row=1,column=1)    
    def open_file():
       filename = 'C:\\Users\\Admin\\Desktop\\112.xlsx'
       df = pd.read_excel(filename)
       clear_treeview()
       tree["column"] = list(df.columns)
       tree["show"] = "headings"
       for col in tree["column"]:
          tree.heading(col, text=col)
       df_rows = df.to_numpy().tolist()
       for row in df_rows:
           tree.insert("", "end", values=row)
       tree.pack()
       scroll = Scrollbar(frame,orient=tki.HORIZONTAL)
       scroll.pack(side = BOTTOM, fill = X,pady=5,padx=5)
       tree.config(xscrollcommand = scroll.set)
       scroll.config(command = tree.xview)
       
    def clear_treeview():
       tree.delete(*tree.get_children())
    tree = ttk.Treeview(frame)
    open_file()
    def reports_window():
        root_rep=tki.Toplevel(root3)
        root_rep.geometry('620x500')
        root_rep.title('Отчеты')
        root_rep.resizable(False, False)
        root_rep.configure(bg=cfon)
        note=ttk.Notebook(root_rep)
        note.pack()
        tab1=tki.Frame(note,height=500,width=620,bg=cfon)
        tab2=tki.Frame(note,height=500,width=620,bg=cfon)
        tab3=tki.Frame(note,height=500,width=620,bg=cfon)
        tab1.pack(fill=BOTH,expand=1)
        tab2.pack(fill=BOTH,expand=1)
        tab3.pack(fill=BOTH,expand=1)
        note.add(tab1,text='Текстовые отчеты')
        note.add(tab2,text='Графические отчеты')
        note.add(tab3,text='Средние значения')
        tki.Label(tab1,text='Виды отчетов : ',font=('Times',16,'italic')
                         , bg=cfon, fg='black').place(x=10,y=10)
        tki.Button(tab1,text='My wave',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=50)
        tki.Button(tab1,text='Young performers',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=90)
        tki.Button(tab1,text='Best collaborations',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=130)
        tki.Button(tab1,text='User`s choice',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=170)
        
        tki.Label(tab2,text='Виды отчетов : ',font=('Times',16,'italic')
                         , bg=cfon, fg='black').place(x=10,y=10)
        tki.Button(tab2,text='Жанр/кол-во треков',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=50)
        tki.Button(tab2,text='Исполнитель/кол-во треков',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=90)
        tki.Button(tab2,text='Круговая диаграмма : жанры',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=130)
        tki.Button(tab2,text='Гистограмма : громкость/BPM',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=170)
        tki.Button(tab2,text='Среднее кол-во прослушиваний по жанрам',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=210)
        tki.Button(tab2,text='Whisker Box',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=250)
        tki.Button(tab2,text='Средняя длина трека по годам',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=290)
        tki.Button(tab2,text='Гистограмма : громкость/BPM',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=330)
        tki.Button(tab2,text='Круговая диаграмма : страны',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=370)
        
        tki.Label(tab3,text='Среднее ',font=('Times',16,'italic')
                         , bg=cfon, fg='black').place(x=10,y=10)
        tki.Button(tab3,text='Средние показатели по БД',font=('Times',16,'italic')
                             , bg='black', fg='white').place(x=10,y=50)
    button_edit=tki.Button(root3,text='Редактировать запись',font=('Times',16,'italic')
                         , bg='black', fg='white',command=option_change)
    button_edit.place(x=10,y=10)
    button_add=tki.Button(root3,text='Добавить запись',font=('Times',16,'italic')
                         , bg='black', fg='white',command=option_add)
    button_add.place(x=10,y=50)
    button_del=tki.Button(root3,text='Удалить запись',font=('Times',16,'italic')
                         , bg='black', fg='white',command=option_del)
    button_del.place(x=10,y=90)
    button_report=tki.Button(root3,text='Создание отчетов',font=('Times',16,'italic')
                         , bg='black', fg='white')
    button_report.place(x=227,y=170)
    
    b=tki.Button(root3,text='Назад',font=('Times',12,'italic')
                         , bg='black', fg='white',command=go_back)
    b.place(x=550,y=10)
    

    
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
