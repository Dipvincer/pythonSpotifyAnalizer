import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


def plot_bar_genre_artist_count(choice, path, excel_data_df):
    """
    Cтолбчатая диаграмма жанр/кол-во треков или артист/кол-во треков

    :param choice: 'Genre' или 'Artist.Name'
    :param path: путь к сохраняемомму изображению
    :param excel_data_df: таблица data frame
    :return: глобальный путь к сохраненному изображению
    """
    genre = excel_data_df[choice]
    num = {}
    for i in genre:
        if i not in num:
            num[i] = 1
        else:
            num[i] += 1
    genre = num.keys()
    genre2 = []
    count_genre = num.values()
    for i in genre:
        genre2.append(i)
    position = np.arange(len(count_genre))
    fig, ax = plt.subplots()
    ax.barh(position, count_genre, color='#1DB954')
    ax.set_yticks(position)
    genre2 = ax.set_yticklabels(genre2,
                                fontsize=5,
                                color='#191414',
                                rotation=0,
                                verticalalignment='center')
    fig.savefig('GraphImages/' + path,bbox_inches = 'tight')
    return os.path.split(os.path.abspath(__file__))[0] + '\\GraphImages\\' + path


def pie_genre_count(path, excel_data_df):
    """
    Круговая диаграмма жанр/кол-во треков

    :param path: путь к сохраняемомму изображению
    :param excel_data_df: таблица data frame
    :return: глобальный путь к сохраненному изображению
    """
    genre = excel_data_df['Genre']
    num = {}
    for i in genre:
        if i not in num:
            num[i] = 1
        else:
            num[i] += 1
    genre = num.keys()
    count_genre = num.values()
    fig, ax = plt.subplots()
    ax.pie(count_genre,)
    ax.legend(bbox_to_anchor = (-0.16, 0.4, 0.1, 0.1), labels = genre )
    fig.savefig('GraphImages/' + path,bbox_inches = 'tight')
    return os.path.split(os.path.abspath(__file__))[0] + '\\GraphImages\\' + path


def loudness_energy(path, excel_data_df):
    """
    Пузырьковый график

    :param path: путь к сохраняемомму изображению
    :param excel_data_df: таблица data frame
    :return: глобальный путь к сохраненному изображению
    """
    loud = excel_data_df['Loudness..dB..']
    beat = excel_data_df['Beats.Per.Minute']
    fig, ax = plt.subplots()
    ax.scatter(x=loud, y=beat, marker='o', c='#1DB954', edgecolor='#191414')
    ax.set_xlabel('Громкость(db)')
    ax.set_ylabel('BPM')
    fig.savefig('GraphImages/' + path,bbox_inches = 'tight')
    return os.path.split(os.path.abspath(__file__))[0] + '\\GraphImages\\' + path


def mean_monthaud_per_genre(path, excel_data_df):
    """
    Круговая диаграмма со средним кол-вом прослушиваний в месяц по жанрам

    :param path: путь к сохраняемомму изображению
    :param excel_data_df: таблица data frame
    :return: глобальный путь к сохраненному изображению
    """
    genre = excel_data_df['Genre']
    month_aud = excel_data_df['Monthly auditions']
    num = {}
    for i in range(len(genre)):
        if genre[i] not in num:
            num[genre[i]] = month_aud[i]
        else:
            num[genre[i]] += month_aud[i]
    num2 = {}
    for i in genre:
        if i not in num2:
            num2[i] = 1
        else:
            num2[i] += 1
    m = num.values()
    numb = num2.values()
    numb2 = []
    for i in numb:
        numb2.append(i)
    newone = []
    for i in m:
        newone.append(i)
    for i in range(len(newone)):
        newone[i] = newone[i]/numb2[i]
    fig, ax = plt.subplots()
    ax.pie(newone,)
    ax.legend(bbox_to_anchor=(-0.16, 0.4, 0.25, 0.25), labels=num.keys())
    fig.savefig('GraphImages/' + path,bbox_inches = 'tight')
    return os.path.split(os.path.abspath(__file__))[0] + '\\GraphImages\\' + path


def whisker_all(path, excel_data_df):
    """
    Whisker chart

    :param path: путь к сохраняемомму изображению
    :param excel_data_df: таблица data frame
    :return: глобальный путь к сохраненному изображению
    """
    excel_data_df.plot(kind='box', subplots=True)
    plt.gcf().set_size_inches(30,30)
    plt.savefig('GraphImages/' + path,bbox_inches = 'tight')
    return os.path.split(os.path.abspath(__file__))[0] + '\\GraphImages\\' + path


def mean_len(path, excel_data_df):
    """
    Столбчатая диаграмма средняя длина по годам

    :param path: путь к сохраняемомму изображению
    :param excel_data_df: таблица data frame
    :return: глобальный путь к сохраненному изображению
    """
    years = np.array(excel_data_df['Date of release'])
    length = np.array(excel_data_df['Length.'])
    year_len = {}
    year_num = {}
    for i in range(len(years)):
        if years[i] not in year_len:
            year_len[years[i]] = length[i]
        else:
            year_len[years[i]] += length[i]
        if years[i] not in year_num:
            year_num[years[i]] = 1
        else:
            year_num[years[i]] += 1
    sorted_tuple = sorted(year_len.items(), key=lambda x: x[0])
    year_len = dict(sorted_tuple)
    sorted_tuple2 = sorted(year_num.items(), key=lambda x: x[0])
    year_plot = list(year_len.keys())
    year_num = dict(sorted_tuple2)
    full_len = list(year_len.values())
    full_num = list(year_num.values())

    mean = []
    for i in range(len(full_len)):
        mean.append(full_len[i]/full_num[i])
    fig, ax = plt.subplots()
    ax.bar(year_plot,mean)
    ax.set_xlabel('Год')
    ax.set_ylabel('Длина(сек)')
    fig.savefig('GraphImages/' + path,bbox_inches = 'tight')
    return os.path.split(os.path.abspath(__file__))[0] + '\\GraphImages\\' + path


def country_pie(path, excel_data_df):
    """
    Круговая диаграмма с количеством треков по странам

    :param path: путь к сохраняемомму изображению
    :param excel_data_df: таблица data frame
    :return: глобальный путь к сохраненному изображению
    """
    country = np.array(excel_data_df['Country '])
    dictionary = {}
    for i in country:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    fig, ax = plt.subplots()
    ax.pie(dictionary.values(),labels=dictionary.keys())
    fig.savefig('GraphImages/' + path,bbox_inches = 'tight')
    return os.path.split(os.path.abspath(__file__))[0] + '\\GraphImages\\' + path


def bar_average_length(path, data):
    """
    Гистограма длины треков по годам

    :param path: путь к сохраняемомму изображению
    :param data: таблица data frame
    :return: глобальный путь к сохраненному изображению
    """
    years = []
    sum_length = []
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
    fig, ax = plt.subplots()
    x = np.array(years)
    y = np.array(sum_length)
    plt.bar(x, y)
    ax.set_xlabel("Год")
    ax.set_ylabel("Длина трека")
    plt.savefig('GraphImages/' + path,bbox_inches = 'tight')
    return os.path.split(os.path.abspath(__file__))[0] + '\\GraphImages\\' + path
