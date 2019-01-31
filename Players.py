# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:11:12 2018

@author: Kathrine
"""
import numpy as np
import matplotlib.pyplot as plt

N=25               #Число игроков
Coins = 100             #Число монеток
times = 10000
Players=[]               #Число итераций   
CoinsOfPlayers=[]           #Массив монеток у игроков 
Remain=[]  
Taken=[]                  #Сколько монеток взяли у игрока
Transfer=[]

def DrawThis(Array, a): #Рисуем всякую графику
    dpi = 80
    plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
    plt.title('здесь могла быть ваша реклама')
    ax = plt.axes()
    ax.set_ylim( min(range(1)), max(range(350)) )
    plt.bar([x  for x in Players], Array,
        width = 0.3, color = 'red',
        zorder = 2)
    plt.savefig('zbars%d.png' % a)
    ax.clear()
    plt.close()


for i in range(N):
    CoinsOfPlayers.append(Coins)
    Players.append(i)




t=0
while t < times :
    for i in range(N):
        #xi= rnd.uniform(0.2 ,0.5)    #Генерируем случайную величину
        #xi = rnd.gauss(0,1)
        xi= np.abs(np.random.normal(0,0.27))
        #print(xi)
        Taken.append(CoinsOfPlayers[i]*xi)
        Remain.append( CoinsOfPlayers[i] - ( CoinsOfPlayers[i] * xi ))

    sum=0
    for i in range(N):
        if i != 0:
            Transfer.append(Remain[i]+Taken[i-1])
        else:
            Transfer.append(Remain[i]+Taken[N-1])
        sum=Transfer[i]+sum
    CoinsOfPlayers.clear()
    CoinsOfPlayers=Transfer[:] 
    DrawThis(CoinsOfPlayers, t)  
    Remain.clear()  
    Taken.clear()
    Transfer.clear()
    #ax.clear() 
    #print("Итерации" + str(t))
    t+=1
    
#print(Transfer)
#print(CoinsOfPlayers)
#print(Taken)    
#print(Remain)

