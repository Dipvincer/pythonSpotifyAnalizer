#!/usr/bin/env python
# coding: utf-8

# In[146]:


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

# Здесь должна быть кнопка для выбора года
year = int(input()) 

def user_choice_table(file_path, year):
    rating = []
    rating_index = []
    list_choice = []
    value=len(list(data['Date_of_release']))
    audition_max = 2542855152 / 100
    j = 0
    for i in range(value):
        if (data['Date_of_release'][i] == year):
            rating.append(0.03*float(data["Auditions_on_the_track"][i])/float(audition_max)+float(0.07*data["Popularity"][i]))
            rating_index.append(i)
            j+=1
    dictionary = dict(zip(rating_index, rating))
    list_d = list(dictionary.items())
    list_d.sort(key = lambda i: i[1], reverse = True)
    i = 0
    while i < j:
        index = list_d[i][0]
        string = data["Artist_name"][index] + ' - ' + data["Track_name"][index]
        list_choice.append(string)
        i+=1
    f = open('D:/Python/user_choice.txt', 'w' )
    for item in list_choice:
        f.write("%s\n" % item)
    f.close()

user_choice_table(file_path, year)

def for_young_performers_table(file_path):
    countries = []
    lst = []
    list_index = []
    value=len(list(data['Date_of_release']))
    for i in range(value):
        if data['Country'][i] not in countries:
            countries.append(data['Country'][i])
    array = [[0] for elem in countries]
    for j in range(len(countries)):
        list1 = []
        for i in range(value):
            if data['Country'][i] == countries[j]:
                if data["Genre"][i] not in list1:
                    list1.append(data["Genre"][i])
        array[j].append(list1)
    for j in range(len(countries)):
        maximum = 0
        index_max = 0
        for k1 in range(len(array[j][1])):
            count = 0
            for i in range(value):
                if data['Country'][i] == countries[j]:
                    if data["Genre"][i] == array[j][1][k1]:
                        count += 1
                        array[j][1][k1] = count 
            if (array[j][1][k1]>maximum):
                maximum = array[j][1][k1]
                index_max = k1
        list_index.append(index_max)
    array = [[0] for elem in countries]
    for j in range(len(countries)):
        list1 = []
        for i in range(value):
            if data['Country'][i] == countries[j]:
                if data["Genre"][i] not in list1:
                    list1.append(data["Genre"][i])
        array[j].append(list1)
    for j in range(len(countries)):
        string = str(countries[j]) + " - " + str(array[j][1][list_index[j]])
        lst.append(string)
    f = open('D:/Python/young_performer.txt', 'w' )
    for item in lst:
        f.write("%s\n" % item)
    f.close()
    
for_young_performers_table(file_path)              
            
def best_collaborations_table(file_path):
    collab = []
    collab_index = []
    list_collab = []
    audition_max = 2542855152 / 100
    monthly_max = 83788888 / 100
    value=len(list(data['Date_of_release']))

    j = 0
    for i in range(value):
        if (data['Collaboration'][i] != "single"):
            collab.append(0.02*float(data["Popularity"][i]) + 0.04*float(data["Auditions_on_the_track"][i])/audition_max+float(0.04*data["Monthly_auditions"][i])/monthly_max)
            collab_index.append(i)
            j+=1
    dictionary = dict(zip(collab_index, collab))
    list_d = list(dictionary.items())
    list_d.sort(key = lambda i: i[1], reverse = True)
    i = 0
    while i < j:
        index = list_d[i][0]
        coll = data["Collaboration"][index]
        art = data["Artist_name"][index]
        track = data["Track_name"][index]
        string = f"{art} (feat.{coll}) - {track}"
        list_collab.append(string)
        i+=1
    f = open('D:/Python/best_collab.txt', 'w' )
    for item in list_collab:
        f.write("%s\n" % item)
    f.close()

best_collaborations_table(file_path)

#Здесь должна быть ваша кнопка
mood_modification = input()

def my_wave_table(mood_modification, file_path):
    mood = []
    mood_index = []
    loudness_max = 1.1
    bpm = 18
    length = 300
    value=len(list(data['Date_of_release']))

    for i in range(value):
            mood.append(0.4*loudness_max*int(data["Loudness"][i])+0.55*int(data["Beats_per_minute"][i])/bpm+0.05/length*float(data["Length"][i]))
            mood_index.append(i)
    dictionary = dict(zip(mood_index, mood))
    list_d = list(dictionary.items())
    list_d.sort(key = lambda i: i[1])
    list_d_rev = list(reversed(list_d))
    list_mood = []
    i = 0
    while i < 15:
        if mood_modification == "Happy":
            index = list_d[i][0]
            art = data["Artist_name"][index]
            track = data["Track_name"][index]
            string = f"{art} - {track}"
            list_mood.append(string)
            i+=1
        elif mood_modification == "Sad":
            index = list_d_rev[i][0]
            art = data["Artist_name"][index]
            track = data["Track_name"][index]
            string = f"{art} - {track}"
            list_mood.append(string)
            i+=1
    f = open('D:/Python/my_wave.txt', 'w' )
    for item in list_mood:
        f.write("%s\n" % item)
    f.close()
    
my_wave_table(mood_modification, file_path)
    
    



    
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




