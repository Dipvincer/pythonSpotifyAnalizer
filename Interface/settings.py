import os
from tkinter import messagebox

config_path = os.path.split(os.path.abspath(__file__))[0] + '\\settings.txt'


def read_config():
    """
    Чтение файла настроек

    :return: считываемые данные настроек для программы
    """
    data = []
    with open(config_path, 'r') as f:
        for line in f:
            data.append(line)
        data = [line.rstrip() for line in data]
        f.close()
    return data


def save_settings(report, graph, font_name, back, but):
    """
    Сохранение файла настроек

    :param report: путь к текстовым отчетам
    :param graph: путь к графическим отчетам
    :param font_name: название шрифта
    :param back: цвет фона
    :param but: цвет кнопок
    """
    if (report and report.strip()) and (graph and graph.strip()) and (font_name and font_name.strip())\
            and (back and back.strip()) and (but and but.strip()):
        with open(config_path, 'w') as f:
            f.write(report + '\n')
            f.write(graph + '\n')
            f.write(font_name + '\n')
            f.write(back + '\n')
            f.write(but)
            f.close()
        messagebox.showinfo('Уведомление', 'Данные записаны!\n Перезапустите приложение.')
    else:
        messagebox.showerror('Ошибка', 'Некорректно введены данные!')


r_data = read_config()
text_path = r_data[0]
graph_path = r_data[1]
font = r_data[2]
background_color = r_data[3]
button_color = r_data[4]
