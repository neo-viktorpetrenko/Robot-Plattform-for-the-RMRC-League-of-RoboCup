import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from numpy import *
import math
import pandas as pd
import numpy as np
from matplotlib.ticker import LogLocator


lf = 72.58 # leg length
dA1 = 54 # Axis diameter for the spring attachment point on the partial axis 
dAx = 70 #x distance between the first spring attachment point on dA1 and the seccond spring attachment point on the supports 
dAy = 15 #y distance between the first spring attachment point on dA1 and the seccond spring attachment point on the supports
dAz = 15 #z distance between the first spring attachment point on dA1 and the seccond spring attachment point on the supports
# ausgang: 50 50 40

r = dA1/2 # axis radius for the spring attachment point on the partial axis 
k = 1223.5 # spring constant
dA3 = 60 # distance between pivot point and wheel"

def df_phif(start,end,resolution):
    n = int((end-start)/resolution)
    df = pd.DataFrame(columns=['x', 'y'])
    df_angleTooBig = pd.DataFrame(columns=['x', 'y'])
    
    for counter in range(n):
        x = counter*resolution
        xR_display = x*1000

        phir = np.arcsin(xR_display/dA3)
        pi = np.pi
        t1 = np.cos(phir)*r
        t2 = np.sin(phir)*r
        t3 = dAx - t2
        t4 = r + dAy - t1
        l1 = np.sqrt((t3**2)+(t4**2)+(dAz**2))
        l0 = np.sqrt(dAx**2+dAy**2+dAz**2)
        if xR_display == 0:
            l1 = l0
        phif = 2*arcsin(l1/(2*lf))*180/pi
        df = pd.concat([df, pd.DataFrame({'x': [xR_display], 'phif': [phif]})], ignore_index=True)
        print(f"phir {phir},t1 {t1},t2 {t2},t3 {t3},t4 {t4},l1 {l1}, phif {phif}")
    return df

def df_fr_new(start,end,resolution):
    n = int((end-start)/resolution)
    df = pd.DataFrame(columns=['x', 'y'])
    
    for counter in range(n):
        x = counter*resolution
        xR_display = x*1000

        phir = np.arcsin(xR_display/dA3)
        pi = np.pi
        t1 = np.cos(phir)*r
        t2 = np.sin(phir)*r
        t3 = dAx - t2
        t4 = r + dAy - t1
        l1 = np.sqrt((t3**2)+(t4**2)+(dAz**2))
        l0 = np.sqrt(dAx**2+dAy**2+dAz**2)
        phif = 2*arcsin(l1/(2*lf))
        ff = (k*(pi/2-phif))/(2*np.sqrt(lf**2-(dA1/2)**2))
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


# Create the figure and first axis
fig, ax1 = plt.subplots()

dffrxr = df_fr_new(0, xR, 0.0001)
scatter1 = ax1.scatter(dffrxr['x'], dffrxr['y'], color=(0, 0.2, 0.5), label="Fr")
mittelwert = df_fr_mittelwert(dffrxr, xR)
ax1.plot([0, xR * 1000], [mittelwert, mittelwert], color='red', linestyle='dashed')

#axis 1
ax1.set_xlabel("spring tavel of a wheel in mm")
ax1.set_ylabel("spring force in N", color=(0, 0.2, 0.5))
ax1.tick_params(axis='y', labelcolor=(0, 0.2, 0.5))

#axis 2
ax2 = ax1.twinx()

dfphif = df_phif(0, xR, 0.0001)
scatter2 = ax2.scatter(dfphif['x'], dfphif['phif'], color=(0, 0.5, 0.2), label="Phif")

ax2.set_ylabel("Phif", color=(0, 0.5, 0.2))
ax2.tick_params(axis='y', labelcolor=(0, 0.5, 0.2))

#Legend
legend_1 = mpatches.Patch(color='blue', label=f'Fr')
legend_2 = mpatches.Patch(color='green', label='Phif')
ax1.legend(handles=[legend_1, legend_2],loc='lower center')

print(f"average = {mittelwert}")

#Look of the graph
plt.grid(True, which="both", axis="both")
plt.rcParams.update({'font.size': 12})
plt.tight_layout()
plt.show()