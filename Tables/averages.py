import pandas as pd
import numpy as np
import os


def average_in_year(file_path, data):
    """
    Среднее количество прослушиваний по годам

    :param file_path: имя файла
    :param data: открытая таблица .xlsx
    """
    years = []
    sum_years = []
    lst = []
    value = len(list(data['Date_of_release']))
    for i in range(value):
        if data["Date_of_release"][i] not in years:
            years.append(data["Date_of_release"][i])
    years.sort()
    for j in range(len(years)):
        count = 0
        summa = 0
        for i in range(value):
            if data["Date_of_release"][i] == years[j]:
                summa += data["Auditions_on_the_track"][i]
                count += 1
        sum_years.append(summa//count)
    for i in range(len(years)):
        string = str(years[i]) + "    " + str(sum_years[i])
        lst.append(string)
    lst.append("Total" + "   " + str(round(sum(sum_years)/len(years))))
    f = open(os.path.split(os.path.abspath(__file__))[0] + '\\Reports\\' + file_path, 'w')
    for item in lst:
        f.write("%s\n" % item)
    f.close()
    return os.path.split(os.path.abspath(__file__))[0] + '\\Reports\\' + file_path


def average_length(file_path, data):
    """
    Средняя длина трека

    :param file_path: имя файла
    :param data: открытая таблица .xlsx
    """
    years = []
    sum_length = []
    lst = []
    value = len(list(data['Date_of_release']))
    for i in range(value):
        if data["Date_of_release"][i] not in years:
            years.append(data["Date_of_release"][i])
    years.sort()
    for j in range(len(years)):
        count = 0
        summa = 0
        for i in range(value):
            if data["Date_of_release"][i] == years[j]:
                summa += data["Length"][i]
                count += 1
        sum_length.append(summa//count)
    for i in range(len(years)):
        string = str(years[i]) + "    " + str(sum_length[i])
        lst.append(string)
    lst.append("Total" + "   " + str(round(sum(sum_length)/len(years))))
    f = open(os.path.split(os.path.abspath(__file__))[0] + '\\Reports\\' + file_path, 'w')
    for item in lst:
        f.write("%s\n" % item)
    f.close()
    return os.path.split(os.path.abspath(__file__))[0] + '\\Reports\\' + file_path


def average_genre(file_path, data):
    """
    Среднее по жанрам

    :param file_path: имя файла
    :param data: открытая таблица .xlsx
    """
    genre = []
    sum_genre = []
    lst = []
    value = len(list(data['Date_of_release']))
    for i in range(value):
        if data["Genre"][i] not in genre:
            genre.append(data["Genre"][i])
    genre.sort()
    for j in range(len(genre)):
        count = 0
        summa = 0
        value = len(list(data['Date_of_release']))
        for i in range(value):
            if data["Genre"][i] == genre[j]:
                summa += data["Auditions_on_the_track"][i]
                count += 1
        sum_genre.append(summa//count)
    for i in range(len(genre)):
        string = str(genre[i]) + " " * (20-len(genre[i])) + str(sum_genre[i])
        lst.append(string)
    lst.append("Total" + " " * 15 + str(round(sum(sum_genre)/len(genre))))
    f = open(os.path.split(os.path.abspath(__file__))[0] + '\\Reports\\' + file_path, 'w')
    for item in lst:
        f.write("%s\n" % item)
    f.close()
    return os.path.split(os.path.abspath(__file__))[0] + '\\Reports\\' + file_path



