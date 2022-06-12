import matplotlib.pyplot as plt
import numpy as np

plt.figure(num=None,figsize=(8.5,4.5),dpi=80,facecolor='w',edgecolor='w')


x1=[40,80,120,160,200,240,280,320,360,400,440,480,520,560,600]
y1=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
plt.plot(x1,y1,label="Without isolation",color='black',linestyle='dashed',linewidth=2,marker='o',markerfacecolor='black',markersize=5)

x2=[40,80,120,160,200,240,280,320,360,400,440,480,520,560,600]
y2=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

plt.plot(x2,y2,label="With isolation ",color='red',linestyle='solid',linewidth=2,marker='X',markerfacecolor='red',markersize=5)

plt.ylim(0,1.2)
plt.xlim(40,600)

plt.xlabel("window size = 40,attackers intro from 200-500, % of attackers = 40%")
plt.ylabel('TPR')
plt.title("Random Yes Attack")
plt.xticks(x1,x2)
plt.legend(loc= 'upper right' )
plt.show()