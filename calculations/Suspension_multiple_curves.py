import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from numpy import *
import math
import pandas as pd
import numpy as np
from matplotlib.ticker import LogLocator


l0 = 70 #distance between partial axis, wheels sit parallel to each other
lf = 50 # leg length
dA1 = 50 # Achsdurchmesser für Befesstigung Feder 30 bis 80 
# ausgang: 50 50 40

r = dA1/2 # axis radius for the spring attachment point on the partial axis 
k = 1849.8 # spring constant
dA3 = 80 # distance between pivot point and wheel


def phif(phir):
    phir_bog =  phir*math.pi/180
    z1 = 1/(2*(lf**2))
    z2 = (l0-np.sin(phir_bog)*r)**2
    z3 = r**2*(1-np.cos(phir_bog)**2)
    val = float(np.arccos(1- z1 * (z2 + z3)))
    return val*180/np.pi

def df_phif(start,end,resolution):
    n = int((end-start)/resolution)
    df = pd.DataFrame(columns=['x', 'y'])
    for counter in range(n):
        x = counter*resolution
        y = phif(x)
        df = pd.concat([df, pd.DataFrame({'x': [x], 'y': [y]})], ignore_index=True)
    
    return df


def fr(phir):
    phir_bog =  phir*math.pi/180
    z1 = 1/(2*(lf**2))
    z2 = (l0-np.sin(phir_bog)*r)**2
    z3 = r**2*(1-np.cos(phir_bog)**2)
    z4 = float(np.arccos(1- z1 * (z2 + z3)))
    n1 = 2*np.sqrt(lf**2-(l0/2)**2)
    val = dA1/(2*dA3)*(k*(np.pi/2 -z4))/n1
    return val


def df_fr(start,end,resolution):
    n = int((end-start)/resolution)
    df = pd.DataFrame(columns=['x', 'y'])
    for counter in range(n):
        x = counter*resolution
        y = fr(x)
        df = pd.concat([df, pd.DataFrame({'x': [x], 'y': [y]})], ignore_index=True)
    
    return df

def df_arbeit(start,end,resolution):
    n = int((end-start)/resolution)
    df = pd.DataFrame(columns=['x', 'y'])
    cumulation = 0
    for counter in range(n):
        x = counter*resolution

        phir = np.arcsin(x/dA3)*180/np.pi
        cumulation += fr(phir)*x
        y = cumulation
        df = pd.concat([df, pd.DataFrame({'x': [x], 'y': [y]})], ignore_index=True)
    
    return df

def df_fr_von_xr(start,end,resolution):
    n = int((end-start)/resolution)
    df = pd.DataFrame(columns=['x', 'y'])
    
    for counter in range(n):
        x = counter*resolution
        xR_display = x*1000

        phir = np.arcsin(x/dA3)*180/np.pi
        y= fr(phir)
        df = pd.concat([df, pd.DataFrame({'x': [xR_display], 'y': [y]})], ignore_index=True)
    
    return df

def df_fr_new(start,end,resolution):
    n = int((end-start)/resolution)
    df = pd.DataFrame(columns=['x', 'y'])
    
    for counter in range(n):
        x = counter*resolution
        xR_display = x*1000

        phir = np.arcsin(xR_display/dA3)
        pi = np.pi
        t1 = np.sin(phir)*dA1
        a = np.cos(-phir/2)*t1
        t2 = np.sin(-phir/2)*t1
        l1 = np.sqrt((l0-a)**2+t2**2)
        phif= 2*arcsin(l1/(2*lf))
        ff = (k*(pi-phif))/(2*np.sqrt(lf**2-(dA1/2)**2))
        fr = ff*dA1/2/dA3

        y= fr
        df = pd.concat([df, pd.DataFrame({'x': [xR_display], 'y': [y]})], ignore_index=True)
    
    return df

def df_fr_Integriert(df_fr,length):
    summe = 0
    step_amount = length/len(df_fr)
    for index, row in df_fr.iterrows():
        summe += row["y"]*step_amount
    
    return summe

def df_fr_mittelwert(df_fr, length):
    integriert = df_fr_Integriert(df_fr,length)
    return integriert/length

x1, y1 = [0.5, 0.5], [10, 10]
xR = dA3*np.sin(20*np.pi/180)/1000
dffr = df_fr(0,40,0.1)
dfphif = df_phif(0,40,0.1)
dfarbeit = df_arbeit(0,0.032,0.0001)

n = 10
selected = "dA1"

for i in range(n):

    valuelist = {
        "l0": {
            "min": 60,
            "max": 100,
        },
        "dA1": {
            "min": 30,
            "max": 80,
        },
        "lf": {
            "min": 30,
            "max": 90,
        }
    }
    plotrange = valuelist[selected]["max"]-valuelist[selected]["min"]
    div = plotrange/n
    dA1 = valuelist[selected]["min"]+(i+1)*div
    dffrxr = df_fr_new(0,xR,0.0001)
    plt.scatter(dffrxr['x'],dffrxr['y']).set_color((i*1/n, 0.2, 0.5))
    mittelwert = df_fr_mittelwert(dffrxr,xR)
    #plt.scatter(-2/2, mittelwert, marker='x', s=100).set_color((i*1/n, 0.2, 0.5))

#Look of the Graph
plt.grid(True,which="both",axis="both")



#Legend
plt.rcParams.update({'font.size': 12})
plt.xlabel("Spring travel of a wheel in mm")
plt.ylabel("spring force in N")
vareiert = (valuelist[selected]["min"],valuelist[selected]["max"])
if selected == "l0":
    l0 = f"varied from {vareiert[0]} to {vareiert[1]}"
elif selected == "lf":
    lf = f"varied from {vareiert[0]} to {vareiert[1]}"
elif selected == "dA1":
    dA1 = f"varied from {vareiert[0]} to {vareiert[1]}"
schrittweite = (vareiert[1] - vareiert[0])/n
legend_1 = mpatches.Patch(color='blue', label=f'Fr with \nl0 = {l0} mm\nlf = {lf} mm\ndA1 = {dA1} mm\nstep size = {schrittweite} mm')
plt.legend(handles=[legend_1])


plt.show() 