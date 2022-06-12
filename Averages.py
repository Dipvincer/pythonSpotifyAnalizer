#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np

data = pd.read_excel("D:/Python/123.xlsx") 
data.rename(columns={'Track.Name': 'Track_name', 'Artist.Name': 'Artist_name', 'Date.of.release': 'Date_of_release',
                       'Beats.Per.Minute': 'Beats_per_minute', 'Loudness..dB..': 'Loudness',
                       'Monthly.auditions': 'Monthly_auditions', 'Auditions.on.the.track': 'Auditions_on_the_track'}, inplace=True)
data.isnull().sum()
data.fillna(0)

# Здесь должен быть путь к файлу
file_path = "D:/Python/123.xlsx"

def average_in_year(file_path):
    years = []
    sum_years = []
    lst = []
    for i in range(49):
        if data["Date_of_release"][i] not in years:
            years.append(data["Date_of_release"][i])
    years.sort()
    for j in range(len(years)):
        count = 0
        summa = 0
        for i in range(49):
            if data["Date_of_release"][i] == years[j]:
                summa += data["Auditions_on_the_track"][i]
                count += 1
        sum_years.append(summa//count)
    for i in range(len(years)):
        string = str(years[i]) + "    " + str(sum_years[i])
        lst.append(string)
    lst.append("Итого" + "   " + str(round(sum(sum_years)/len(years))))
    f = open('D:/Python/average_in_year.txt', 'w' )
    for item in lst:
        f.write("%s\n" % item)
    f.close()
           
average_in_year(file_path)

def average_length():
    years = []
    sum_length = []
    lst = []
    for i in range(49):
        if data["Date_of_release"][i] not in years:
            years.append(data["Date_of_release"][i])
    years.sort()
    for j in range(len(years)):
        count = 0
        summa = 0
        for i in range(49):
            if data["Date_of_release"][i] == years[j]:
                summa += data["Length"][i]
                count += 1
        sum_length.append(summa//count)
    for i in range(len(years)):
        string = str(years[i]) + "    " + str(sum_length[i])
        lst.append(string)
    lst.append("Итого" + "   " + str(round(sum(sum_length)/len(years))))
    f = open('D:/Python/average_length.txt', 'w' )
    for item in lst:
        f.write("%s\n" % item)
    f.close()

average_length()

def average_genre(file_path):
    genre = []
    sum_genre = []
    lst = []
    for i in range(49):
        if data["Genre"][i] not in genre:
            genre.append(data["Genre"][i])
    genre.sort()
    for j in range(len(genre)):
        count = 0
        summa = 0
        for i in range(49):
            if data["Genre"][i] == genre[j]:
                summa += data["Auditions_on_the_track"][i]
                count += 1
        sum_genre.append(summa//count)
    for i in range(len(genre)):
        string = str(genre[i]) + " " * (20-len(genre[i])) + str(sum_genre[i])
        lst.append(string)
    lst.append("Итого" + " " * 15 + str(round(sum(sum_genre)/len(genre))))
    f = open('D:/Python/average_genre.txt', 'w' )
    for item in lst:
        f.write("%s\n" % item)
    f.close()
           
average_genre(file_path)
    


# In[ ]:




