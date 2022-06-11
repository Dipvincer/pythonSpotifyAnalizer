# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 22:33:49 2022

@author: Admin
"""

import sys
import os
import tkinter as tk
import tkinter.messagebox as mb
from settings import font

shrift = (font, 10)

os.chdir(os.path.abspath(os.path.join(os.getcwd(), '..')))
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'Library'))

def vibor(notebook1, notebook2):
    
    if notebook1.curselection():
        str_num = notebook1.curselection()[0]
        stroka = notebook1.get(str_num)
        notebook2.insert('end', stroka)
        notebook1.delete(str_num)

def vibor2(notebook1, notebook2, columns):
    
    if notebook2.curselection():
        str_num = notebook2.curselection()[0]
        stroka = notebook2.get(str_num)
        notebook1.insert(0, stroka)
        new_columns = notebook1.get(0, 8)
        new_columns = [[columns.index(x), x] for x in new_columns]
        new_columns.sort()
        new_columns = [x[1] for x in new_columns]
        notebook1.delete(0, 8)
        for column in new_columns:
            notebook1.insert('end', column)
        notebook2.delete(str_num)

def system_error():
    
    mb.showerror('Ошибка', 'Приложение не может быть запущено в данной системе')
    sys.exit()


def zav(canvas1, canvas2, combobox, entr1, entr2):
    
    canvas1['bg'] = "LimeGreen"
    canvas2['bg'] = "Black"
    combobox.set('Tahoma')
    entr1['state'] = 'normal'
    entr1.delete(0, tk.END)
    entr1.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'Output')))
    entr1['state'] = 'readonly'
    entr2['state'] = 'normal'
    entr2.delete(0, tk.END)
    entr2.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'Graphics')))
    entr2['state'] = 'readonly'

def check_num(s, k):
    
    k = int(k)
    try:
        float(s)
    except ValueError:
        x = not bool(s)
    else:
        if float(s) < 0 or float(s) > 15*k:
            x = False
        else:
            x = True
    return x

def save_configurations(path, configurations):
   
    with open(path, 'w', encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('# pylint: disable=C0103\n')
        f.write('"""\nФайл с настройками\n"""')
        f.write(f'\ntext_path = r"{configurations[0]}"')
        f.write(f'\ngraph_path = r"{configurations[1]}"')
        f.write(f'\nfont = "{configurations[2]}"')
        f.write(f'\ncfon = "{configurations[3]}"')
        f.write(f'\ncknop = "{configurations[4]}"\n')

def check_system():
    
    ver = sys.version_info
    return sys.platform == 'win32' and ver.major == 3 and ver.minor == 7