#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd
import numpy


fig = plt.figure(frameon=False)

plt.grid=(True)

ax1 = fig.add_subplot(1,1,1)

def animate():
    graph_data = open('log.txt','r').read()
    replaces = graph_data.replace("\n", "");
    xs = []
    ys = []
    replaces=replaces.split("\t")
    newdata=[]
    labels=replaces[0:7]
    i=0;j=7;
    for p in range(len(replaces)//7):
        newdata.append(replaces[i:j])
        i=j
        j=j+7
    del(newdata[:1])
    
    ys3=[]
    xs=[]
    
    for i in range(len(newdata)):
        xs.append(i)
        ys3.append(float(newdata[i][1]))
    

   
    ax1.clear();
    ax1.plot(xs, ys3,color="blue")
    
    plt.title("RAM")
    plt.xlabel("TIME")
    plt.ylabel("USAGE(GB)")
    plt.savefig("ramspike.png")

animate()

