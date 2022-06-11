import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pandas.plotting import scatter_matrix

#import squarify as sq
path=''
excel_data_df = pd.read_excel("C:\\Users\Admin\\Desktop\\112.xlsx")

def plot_bar_genre_artist_count(choice):
    """ столбчатая диаграмма жанр/кол-во треков или артист/кол-во треков
    на вход: 'Genre' или 'Artist.Name'
    """
    genre=excel_data_df[choice]
    num={}
    for i in genre:
        if i not in num:
            num[i]=1
        else:
            num[i]+=1
    genre=num.keys()
    genre2=[]
    count_genre=num.values()
    for i in genre:
        genre2.append(i)
    position = np.arange(len(count_genre))
    fig, ax = plt.subplots()
    ax.barh(position, count_genre,color='LimeGreen')
    ax.set_yticks(position)
    genre2 = ax.set_yticklabels(genre2,
                   fontsize = 5,   
                   color = 'black',    
                   rotation = 0,    
                   verticalalignment =  'center')
    #fig.show()
#plot_bar_genre_artist_count('Genre')
def pie_genre_count():
    """круговая диаграмма жанр/кол-во треков"""
    genre=excel_data_df['Genre']
    num={}
    for i in genre:
        if i not in num:
            num[i]=1
        else:
            num[i]+=1
    genre=num.keys()
    count_genre=num.values()
    plt.pie(count_genre,)
    plt.legend(bbox_to_anchor = (-0.16, 0.4, 0.25, 0.25), labels = genre )
def loudness_energy():
    """пузырьковый график"""
    loud=excel_data_df['Loudness..dB..']
    beat=excel_data_df['Beats.Per.Minute']
    plt.scatter(x=loud,y=beat,marker='o', c='LImeGreen', edgecolor='black')
def mean_monthaud_per_genre():
    """круговая диаграмма со средним кол-вом прослушиваний в месяц по жанрам"""
    genre=excel_data_df['Genre']
    month_aud=excel_data_df['Monthly auditions']
    num={}
    
    for i in range(len(genre)):
        if genre[i] not in num:
            num[genre[i]]=month_aud[i]
        else :
            num[genre[i]]+=month_aud[i]
    num2={}
    for i in genre:
        if i not in num2:
            num2[i]=1
        else:
            num2[i]+=1
    m=num.values()
    numb=num2.values()
    numb2=[]
    for i in numb :
        numb2.append(i)
    newone=[]
    for i in m :
        newone.append(i)
    for i in range(len(newone)):
        newone[i]=newone[i]/numb2[i]
    plt.pie(newone,)
    plt.legend(bbox_to_anchor = (-0.16, 0.4, 0.25, 0.25), labels = num.keys() )
    print(num)
    
def whisker_all():
    """whisker chart """
    excel_data_df.plot(kind='box', subplots=True)
    plt.gcf().set_size_inches(30,30)
def mean_len():
    """столбчатая диаграмма средняя длина по годам"""
    years=np.array(excel_data_df['Date of release'])
    length=np.array(excel_data_df['Length.'])
    year_len={}
    year_num={}
    for i in range(len(years)):
        if years[i] not in year_len:
            year_len[years[i]]=length[i]
        else:
            year_len[years[i]]+=length[i]
        if years[i] not in year_num:
            year_num[years[i]]=1
        else:
            year_num[years[i]]+=1
            
    sorted_tuple = sorted(year_len.items(), key=lambda x: x[0])        
    year_len=dict(sorted_tuple)     
    sorted_tuple2 = sorted(year_num.items(), key=lambda x: x[0])    
    year_plot=list(year_len.keys())
    year_num=dict(sorted_tuple2)  
    full_len=list(year_len.values())
    full_num=list(year_num.values())
    
    print(full_len)
    mean=[]
    for i in range(len(full_len)):
        mean.append(full_len[i]/full_num[i])
    print(year_len)
    print(year_num)
    print(mean)
    plt.bar(year_plot,mean)
mean_len()  
