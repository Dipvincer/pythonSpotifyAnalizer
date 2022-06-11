import pandas as pd
from tkinter import filedialog


def open_file():
    """
    Функция открытия диалогового окна для получения пути к файлу \n
    Пример: button = Button(text="Open", command=open_file)
    """
    file_path = filedialog.askopenfilename()
    return file_path


def open_folder():
    """
    ВЫбор папки для сохранения полученной таблицы \n
    Пример: button = Button(text="Open", command=open_folder)
    """
    folder_path = filedialog.askdirectory()
    return folder_path


def open_table_xlsx(file_path):
    """ Загрузка таблицы"""
    df = pd.read_excel(file_path)
    print(df.shape)
    df.rename(columns={'Track.Name': 'Track_name', 'Artist.Name': 'Artist_name', 'Date.of.release': 'Date_of_release',
                       'Beats.Per.Minute': 'Beats_per_minute', 'Loudness..dB..': 'Loudness',
                       'Monthly.auditions': 'Monthly_auditions', 'Auditions.on.the.track': 'Auditions_on_the_track'},
              inplace=True)
    print(df.dtypes)


def save_dataframe_excel(dataframe, folder_path, name_of_report):
    """Сохранение DataFrame в .xlsx таблицу по выбранному пути"""
    path_to_save = folder_path + name_of_report + '.xlsx'
    writer = pd.ExcelWriter(path_to_save)
    dataframe.to_excel(writer)
    writer.save()


df_marks = pd.DataFrame({'name': ['Somu', 'Kiku', 'Amol', 'Lini'], 'physics': [68, 74, 77, 78], 'chemistry': [84, 56, 73, 69], 'algebra': [78, 88, 82, 87]})
open_table_xlsx(open_file())
save_dataframe_excel(df_marks, open_folder(), 'test')
