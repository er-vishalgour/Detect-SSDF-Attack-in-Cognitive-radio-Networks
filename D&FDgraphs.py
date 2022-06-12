import matplotlib.pyplot as plt
import numpy as np

plt.figure(num=None,figsize=(8.5,4.5),dpi=80,facecolor='w',edgecolor='w')


x1=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y1=[0,0,0,0,0,0,0,0,0,0,0]
plt.plot(x1,y1,label="K-means AF",color='black',linestyle='solid',linewidth=2,marker='D',markerfacecolor='black',markersize=5)

x2=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y2=[0,0,0,0,0,0,0,0,0,0,0]

plt.plot(x2,y2,label="K-means RF ",color='red',linestyle='solid',linewidth=2,marker='>',markerfacecolor='red',markersize=5)


x3=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y3=[0,0,0,0,0,0,0,0,0,0,0]
plt.plot(x3,y3,label="FC-means AF",color='blue',linestyle='dashed',linewidth=2,marker='o',markerfacecolor='black',markersize=5)

x4=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y4=[0,0,0,0,0,0,0,0,0,0,0]

plt.plot(x4,y4,label="FC-means RF ",color='green',linestyle='dashed',linewidth=2,marker='X',markerfacecolor='red',markersize=5)




plt.ylim(0,1.2)
plt.xlim(0,1)

plt.xticks(x1)
plt.legend(loc= 'upper right' )
plt.show()