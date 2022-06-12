#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("D:/Python/123.xlsx") 
data.rename(columns={'Track.Name': 'Track_name', 'Artist.Name': 'Artist_name', 'Date.of.release': 'Date_of_release',
                       'Beats.Per.Minute': 'Beats_per_minute', 'Loudness..dB..': 'Loudness',
                       'Monthly.auditions': 'Monthly_auditions', 'Auditions.on.the.track': 'Auditions_on_the_track'}, inplace=True)
data.isnull().sum()
data.fillna(0)

# Здесь должен быть путь к файлу
file_path = "D:/Python/123.xlsx"

def bar_average_length(file_path):
    years = []
    sum_length = []
    value=len(list(data['Date_of_release']))
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
    plt.savefig('D:/Python/length_per_years.png', dpi = 800)

bar_average_length(file_path)




# In[ ]:




