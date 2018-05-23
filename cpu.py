#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd
import numpy


fig3 = plt.figure(frameon=False)

plt.grid=(True)

ax4 = fig3.add_subplot(1,1,1)

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
        ys3.append(float(newdata[i][6]))
    
    if(len(xs)>100):
        xs=xs[-100:]
        ys3=ys3[-100:]
   
    ax4.clear();
    ax4.plot(xs, ys3,color="red")
    
    plt.title("CPU")
    plt.xlabel("TIME")
    plt.ylabel("USAGE(%)")
    plt.savefig("cpuspike.png")

animate()





