import tkinter as tki
import tkinter.ttk as ttk
import tkinter.font as tf
from tkinter.ttk import Notebook, Frame, Button, Label, Treeview, Scrollbar
from tkinter import *
import os
import pandas as pd
from tkinter import messagebox
import sys
sys.path.append(os.path.split(os.path.abspath(__file__))[0] + '\\Interface')
sys.path.append(os.path.split(os.path.abspath(__file__))[0] + '\\Tables')
sys.path.append(os.path.split(os.path.abspath(__file__))[0] + '\\Graph')
from settings import *
from graph import *
from averages import *
from category import *
import table_controller as tc


def click_info():
    """Отображение информации о создателях"""
    messagebox.showinfo('Справка', 'Авторы :\n Климкин Дмитрий\n'
                                   ' Шаймарданов Эдуард\n'
                                   ' Ермаков Сергей\n'
                                   ' Бутенко Елизавета\n'
                                   ' Группа : БИВ216')


def settings_w():
    """Окно настроек"""
    root_set = tki.Toplevel(root)
    root_set.title("Настройки")
    root_set.resizable(False, False)
    root_set.configure(bg=background_color)

    tki.Label(root_set, text='Путь к текстовым отчётам:', bg=background_color,
              fg=button_color, font=font).grid(row=0, column=0, pady=1)

    path_to_report = tki.Entry(root_set, width=30)
    path_to_report.grid(row=0, column=1, columnspan=3, padx=10)
    path_to_report.insert(0, text_path)

    tki.Label(root_set, text='Путь к графическим отчётам:', bg=background_color,
              fg=button_color, font=font).grid(row=1, column=0, pady=1)

    path_to_graph = tki.Entry(root_set, width=30)
    path_to_graph.grid(row=1, column=1, columnspan=3, padx=10)
    path_to_graph.insert(0, graph_path)

    tki.Label(root_set, text='Шрифт:', bg=background_color,
              fg=button_color, font=font).grid(row=2, column=0, pady=1)

    combo_fonts = ttk.Combobox(root_set, values=list(tf.families()))
    combo_fonts.grid(row=2, column=1)
    combo_fonts.current(list(tf.families()).index(font))

    tki.Label(root_set, text='Цвет фона (HEX):', bg=background_color,
              fg=button_color, font=font).grid(row=3, column=0, pady=1)

    back_color = tki.Entry(root_set, width=30)
    back_color.grid(row=3, column=1, columnspan=3, padx=10)
    back_color.insert(0, background_color)

    tki.Label(root_set, text='Цвет кнопок:', bg=background_color,
              fg=button_color, font=font).grid(row=4, column=0, pady=1)

    but_color = tki.Entry(root_set, width=30)
    but_color.grid(row=4, column=1, columnspan=3, padx=10)
    but_color.insert(0, button_color)

    tki.Button(root_set, text='Сохранить', font=font, bg=button_color, fg='White',
               command=lambda: save_settings(path_to_report.get(),
                                             path_to_graph.get(),
                                             combo_fonts.get(),
                                             back_color.get(),
                                             but_color.get())).grid(row=5, column=4, pady=5, padx=5)


def main_window():
    """Главное окно"""
    def go_back():
        root3.withdraw()
        root.deiconify()

    root3 = tki.Toplevel(root)
    root3.title("Главное окно")
    root3.geometry('620x500')
    root3.resizable(False, False)
    root3.configure(bg=background_color)
    root.withdraw()
    style = ttk.Style()
    style.theme_use('clam')
    frame = Frame(root3)
    frame.pack(side=BOTTOM, pady=20, padx=20, fill=BOTH)

    file_name = tc.open_file()
    df = tc.open_table_xlsx(file_name)

    def option_change():
        """
        Изменение записи в базе данных
        """
        columns = ['Название', 'Артист', 'Коллаборация', 'Жанр', 'Страна', 'Год', 'Альбом', 'BPM', 'Громкость', 'Длина',
                   'Популярность', 'Прослушиваний в месяц', 'Прослушиваний всего', 'Лейбл']
        num = len(df)
        root_c = tki.Toplevel(root3)

        root_c.geometry('620x500')
        root_c.resizable(False, False)
        root_c.configure(bg=background_color)
        root_c.title('Изменение записи в БД')
        lb1 = tki.Label(root_c, text='Выберите номер записи для измения', font=('Times', 16, 'italic'),
                        bg=background_color, fg=button_color)
        lb1.place(x=10, y=10)
        value = list(range(1, num + 2))
        vibor = ttk.Combobox(root_c, values=value)
        vibor.place(x=10, y=50)
        for i in range(len(columns)):
            tki.Label(root_c, text=columns[i], font=('Times', 16, 'italic'),
                      bg=background_color, fg=button_color).place(x=10, y=50 + 30 * (i + 1))
        name = StringVar()
        a = StringVar()
        k = StringVar()
        g = StringVar()
        c = StringVar()
        y = StringVar()
        al = StringVar()
        bpm = StringVar()
        l = StringVar()
        dl = StringVar()
        p = StringVar()
        m = StringVar()
        vs = StringVar()
        lbl = StringVar()
        array = [name, a, k, g, c, y, al, bpm, l, dl, p, m, vs, lbl]
        for i in range(len(array)):
            tki.Entry(root_c, textvariable=array[i]).place(x=230, y=52 + 30 * (i + 1))
        change = tki.Button(root_c, text='Изменить', font=('Times', 16, 'italic'),
                            bg=background_color, fg=button_color).place(x=400, y=250)

    def option_add():
        """
        Добавление новых записей в таблицу
        """
        columns = ['Название', 'Артист', 'Коллаборация', 'Жанр', 'Страна', 'Год', 'Альбом', 'BPM', 'Громкость', 'Длина',
                   'Популярность', 'Прослушиваний в месяц', 'Прослушиваний всего', 'Лейбл']
        num = len(df)
        root_c = tki.Toplevel(root3)

        root_c.geometry('620x500')
        root_c.resizable(False, False)
        root_c.configure(bg=background_color)
        root_c.title('Добавление записи в БД')
        for i in range(len(columns)):
            tki.Label(root_c, text=columns[i], font=('Times', 16, 'italic'),
                      bg=background_color, fg=button_color).place(x=10, y=0 + 35 * i)
        name = StringVar()
        a = StringVar()
        k = StringVar()
        g = StringVar()
        c = StringVar()
        y = StringVar()
        al = StringVar()
        bpm = StringVar()
        l = StringVar()
        dl = StringVar()
        p = StringVar()
        m = StringVar()
        vs = StringVar()
        lbl = StringVar()
        array = [name, a, k, g, c, y, al, bpm, l, dl, p, m, vs, lbl]
        for i in range(len(array)):
            tki.Entry(root_c, textvariable=array[i]).place(x=230, y=2 + 35 * i)
        change = tki.Button(root_c, text='Добавить', font=('Times', 16, 'italic'),
                            bg=background_color, fg=button_color).place(x=400, y=250)

    def option_del():
        """
        Удаление строки из таблицы
        """
        columns = ['Название', 'Артист', 'Коллаборация', 'Жанр', 'Страна', 'Год', 'Альбом', 'BPM', 'Громкость', 'Длина',
                   'Популярность', 'Прослушиваний в месяц', 'Прослушиваний всего', 'Лейбл']
        num = len(df)
        root_c = tki.Toplevel(root3)
        root_c.geometry('500x100')
        root_c.resizable(False, False)
        root_c.configure(bg=background_color)
        root_c.title('Удаление записи из БД')
        lb1 = tki.Label(root_c, text='Выберите номер записи для удаления', font=('Times', 16, 'italic'),
                        bg=background_color, fg=button_color)
        lb1.grid(row=0, column=0)
        value = list(range(1, num + 2))
        vibor = ttk.Combobox(root_c, values=value)
        vibor.grid(row=1, column=0)
        change = tki.Button(root_c, text='Удалить', font=('Times', 16, 'italic'),
                            bg=background_color, fg=button_color).grid(row=1, column=1)

    def open_file():
        """
        Приведение таблицы .xlsx к таблице в tkinter
        """
        tree["column"] = list(df.columns)
        tree["show"] = "headings"
        for col in tree["column"]:
            tree.heading(col, text=col)
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            tree.insert("", "end", values=row)
        tree.pack()
        scroll = Scrollbar(frame, orient=tki.HORIZONTAL)
        scroll.pack(side=BOTTOM, fill=X, pady=5, padx=5)
        tree.config(xscrollcommand=scroll.set)
        scroll.config(command=tree.xview)

    def show_plot(window_name, plot_name):
        """
        Отображение графика в приложении

        :param window_name: название окна родителя
        :param plot_name: вид графика
        """
        root_show = tki.Toplevel(window_name)
        root_show.geometry('620x500')
        root_show.resizable(False, False)
        root_show.configure(bg=background_color)
        if plot_name == 'Жанр/кол-во треков':
            im = PhotoImage(file=plot_bar_genre_artist_count('Genre', 'genre_count.png', df))
            l = Label(root_show, image=im)
            l.pack()
        elif plot_name == 'Исполнитель/кол-во треков':
            im = PhotoImage(file=plot_bar_genre_artist_count('Artist.Name', 'artist_count.png', df))
            l = Label(root_show, image=im)
            l.pack()
        elif plot_name == 'Круговая диаграмма : жанры':
            im = PhotoImage(file=pie_genre_count('genre.png', df))
            l = Label(root_show, image=im)
            l.pack()
        elif plot_name == 'Гистограмма : громкость/BPM':
            im = PhotoImage(file=loudness_energy('energy.png', df))
            l = Label(root_show, image=im)
            l.pack()
        elif plot_name == 'Среднее кол-во прослушиваний по жанрам':
            im = PhotoImage(file=mean_monthaud_per_genre('month.png', df))
            l = Label(root_show, image=im)
            l.pack()
        elif plot_name == 'Whisker Box':
            im = PhotoImage(file=whisker_all('whisker.png', df))
            l = Label(root_show, image=im)
            l.pack()
        elif plot_name == 'Средняя длина трека по годам':
            im = PhotoImage(file=mean_len('len.png', df))
            l = Label(root_show, image=im)
            l.pack()
        elif plot_name == 'Круговая диаграмма : страны':
            im = PhotoImage(file=country_pie('mean.png', df))
            l = Label(root_show, image=im)
            l.pack()

    def show_report(window_name, report_name, df):
        """
        Отображение текстовых отчетов

        :param window_name: название окна родителя
        :param report_name: тип отчета
        :param df: таблица data frame
        """
        root_show = tki.Toplevel(window_name)
        root_show.geometry('620x500')
        root_show.title(report_name)
        root_show.resizable(False, False)
        root_show.configure(bg=background_color)
        tki.Label(root_show, text='Отчет ' + report_name, font=('Times', 16, 'italic'),
                  bg=background_color, fg='black').pack()
        if report_name == 'My wave':
            value = ['Happy', 'Sad']
            curr = tki.StringVar()
            vibor = ttk.Combobox(root_show, values=value, textvariable=curr)
            vibor.pack()

            def func(event):
                curr = vibor.get()

            vibor.bind("<<ComboboxSelected>>", func)
            text = open(my_wave_table(curr, 'my_wave.txt', df), encoding='utf-8').readlines()
            text = ''.join(text)
            textline = Text(root_show)
            textline.insert(1.0, text)
            textline.configure(state='disabled')
            textline.pack(side=BOTTOM, padx=10, pady=10)
            scroll = Scrollbar(command=textline.yview)
            scroll.pack(side=LEFT, fill=Y)
            textline.config(yscrollcommand=scroll.set)

        if report_name == 'User`s choice':
            value = list(set(list(df['Date of release'])))
            value.sort()
            curr = tki.StringVar()
            vibor1 = ttk.Combobox(root_show, state='readonly', values=value, textvariable=curr)
            vibor1.pack()

            def func(event):
                curr = vibor1.get()

            vibor1.bind("<<ComboboxSelected>>", func)
            text = open(user_choice_table('user_choice.txt', curr, df), encoding='utf-8').readlines()
            text = ''.join(text)
            textline = Text(root_show)
            textline.insert(1.0, text)
            textline.configure(state='disabled')
            textline.pack(side=BOTTOM, padx=10, pady=10)
            scroll = Scrollbar(command=textline.yview)
            scroll.pack(side=LEFT, fill=Y)
            textline.config(yscrollcommand=scroll.set)
        if report_name == 'Young performers':
            text = open(for_young_performers_table('for_young.txt', df), encoding='utf-8').readlines()
            text = ''.join(text)
            textline = Text(root_show)
            textline.insert(1.0, text)
            textline.configure(state='disabled')
            textline.pack(side=BOTTOM, padx=10, pady=10)
            scroll = Scrollbar(command=textline.yview)
            scroll.pack(side=LEFT, fill=Y)
            textline.config(yscrollcommand=scroll.set)
        if report_name == 'Best collaborations':
            text = open(best_collaborations_table('best_collab.txt', df), encoding='utf-8').readlines()
            text = ''.join(text)
            textline = Text(root_show)
            textline.insert(1.0, text)
            textline.configure(state='disabled')
            textline.pack(side=BOTTOM, padx=10, pady=10)
            scroll = Scrollbar(command=textline.yview)
            scroll.pack(side=LEFT, fill=Y)
            textline.config(yscrollcommand=scroll.set)
    tree = ttk.Treeview(frame)
    open_file()

    def reports_window():
        """Окно отчетов"""
        root_rep = tki.Toplevel(root3)
        root_rep.geometry('620x500')
        root_rep.title('Отчеты')
        root_rep.resizable(False, False)
        root_rep.configure(bg=background_color)
        note = ttk.Notebook(root_rep)
        note.pack()
        tab1 = tki.Frame(note, height=500, width=620, bg=background_color)
        tab2 = tki.Frame(note, height=500, width=620, bg=background_color)
        tab3 = tki.Frame(note, height=500, width=620, bg=background_color)
        tab1.pack(fill=BOTH, expand=1)
        tab2.pack(fill=BOTH, expand=1)
        tab3.pack(fill=BOTH, expand=1)
        note.add(tab1, text='Текстовые отчеты')
        note.add(tab2, text='Графические отчеты')
        note.add(tab3, text='Средние значения')
        tki.Label(tab1, text='Виды отчетов : ', font=('Times', 16, 'italic')
                  , bg=background_color, fg=button_color).place(x=10, y=10)
        tki.Button(tab1, text='My wave', font=('Times', 16, 'italic'),
                   bg=button_color, fg='white',
                   command=lambda: show_report(root_rep, 'My wave', df)).place(x=10, y=50)
        tki.Button(tab1, text='Young performers', font=('Times', 16, 'italic'),
                   bg=button_color, fg='white',
                   command=lambda: show_report(root_rep, 'Young performers', df)).place(x=10, y=90)
        tki.Button(tab1, text='Best collaborations', font=('Times', 16, 'italic'),
                   bg=button_color, fg='white',
                   command=lambda: show_report(root_rep, 'Best collaborations', df)).place(x=10, y=130)
        tki.Button(tab1, text='User`s choice', font=('Times', 16, 'italic'),
                   bg=button_color, fg='white',
                   command=lambda: show_report(root_rep, 'User`s choice', df)).place(x=10, y=170)

        tki.Label(tab2, text='Виды отчетов : ', font=('Times', 16, 'italic'),
                  bg=background_color, fg=button_color).place(x=10, y=10)
        tki.Button(tab2, text='Жанр/кол-во треков', font=('Times', 16, 'italic'),
                   bg=button_color, fg='white',
                   command=lambda: show_plot(root_rep, 'Жанр/кол-во треков')).place(x=10, y=50)
        tki.Button(tab2, text='Исполнитель/кол-во треков', font=('Times', 16, 'italic'),
                   bg=button_color, fg='white',
                   command=lambda: show_plot(root_rep, 'Исполнитель/кол-во треков')).place(x=10, y=90)
        tki.Button(tab2, text='Круговая диаграмма : жанры', font=('Times', 16, 'italic'),
                   bg=button_color,
                   fg='white', command=lambda: show_plot(root_rep, 'Круговая диаграмма : жанры')).place(x=10, y=130)
        tki.Button(tab2, text='Гистограмма : громкость/BPM', font=('Times', 16, 'italic'),
                   bg=button_color, fg='white',
                   command=lambda: show_plot(root_rep, 'Гистограмма : громкость/BPM')).place(x=10, y=170)
        tki.Button(tab2, text='Среднее кол-во прослушиваний по жанрам', font=('Times', 16, 'italic'),
                   bg=button_color, fg='white',
                   command=lambda: show_plot(root_rep, 'Среднее кол-во прослушиваний по жанрам')).place(x=10, y=210)
        tki.Button(tab2, text='Whisker Box', font=('Times', 16, 'italic'),
                   bg=button_color, fg='white',
                   command=lambda: show_plot(root_rep, 'Whisker Box')).place(x=10, y=250)
        tki.Button(tab2, text='Средняя длина трека по годам', font=('Times', 16, 'italic'),
                   bg=button_color, fg='white',
                   command=lambda: show_plot(root_rep, 'Средняя длина трека по годам')).place(x=10, y=290)

        tki.Button(tab2, text='Круговая диаграмма : страны', font=('Times', 16, 'italic'),
                   bg=button_color, fg='white',
                   command=lambda: show_plot(root_rep, 'Круговая диаграмма : страны')).place(x=10, y=330)

        tki.Label(tab3, text='Среднее ', font=('Times', 16, 'italic')
                  , bg=background_color, fg=button_color).place(x=10, y=10)
        tki.Button(tab3, text='Средние показатели по БД', font=('Times', 16, 'italic')
                   , bg=button_color, fg='white').place(x=10, y=50)

    button_edit = tki.Button(root3, text='Редактировать запись', font=('Times', 16, 'italic')
                             , bg=button_color, fg='white', command=option_change)
    button_edit.place(x=10, y=10)
    button_add = tki.Button(root3, text='Добавить запись', font=('Times', 16, 'italic')
                            , bg=button_color, fg='white', command=option_add)
    button_add.place(x=10, y=50)
    button_del = tki.Button(root3, text='Удалить запись', font=('Times', 16, 'italic')
                            , bg=button_color, fg='white', command=option_del)
    button_del.place(x=10, y=90)
    button_report = tki.Button(root3, text='Создание отчетов', font=('Times', 16, 'italic')
                               , bg=button_color, fg='white', command=reports_window)
    button_report.place(x=227, y=170)

    b = tki.Button(root3, text='Назад', font=('Times', 12, 'italic')
                   , bg=button_color, fg='white', command=go_back)
    b.place(x=550, y=10)
   

root = tki.Tk()
root.title('Spotify analyzer')
root.geometry('850x500')
root.resizable(False, False)
# root.iconbitmap('C:\\Users\\Admin\\Desktop\\python_sem\\spot.ico')
root.configure(bg=background_color)
path = os.getcwd()
shrift = (font, 10)

img = tki.PhotoImage(file=os.path.split(os.path.abspath(__file__))[0] + "\\Interface\\Images\\Spot_logo.png")
spotify_logo = tki.Label(root, image=img)
spotify_logo.place(x=250, y=10)

y_corrective = 10

btn_start = tki.Button(root, text='Начать', font=(font, 16),
                       bg=button_color, fg='white', command=main_window)
btn_start.place(x=397, y=200 + y_corrective)

btn_set = tki.Button(root, text='Настройки', font=(font, 16),
                     bg=button_color, fg='white', command=settings_w)
btn_set.place(x=380, y=255 + y_corrective)

btn_info = tki.Button(root, text='Информация', font=(font, 16),
                      bg=button_color, fg='white', command=click_info)
btn_info.place(x=367, y=310 + y_corrective)

btn_close = tki.Button(root, text='Выйти', font=(font, 16),
                       bg=button_color, fg='white', command=root.destroy)
btn_close.place(x=620+137, y=500-60)

root.mainloop()
