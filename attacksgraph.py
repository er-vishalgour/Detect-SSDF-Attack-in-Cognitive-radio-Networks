import matplotlib.pyplot as plt
import numpy as np
plt.figure(num=None,figsize=(8,6),dpi=80,facecolor='w',edgecolor='w')
x1=[10,20,30,40,50,60,70,80,90]
y1=[100,100,100,100,100,100,99.2,97,94]
plt.plot(x1,y1,label="Always Yes(DETECTION)",color='green',linestyle='solid',linewidth=3,marker='8',markerfacecolor='blue',markersize=5)
x2=[10,20,30,40,50,60,70,80,90]
y2=[100,100,100,100,100,100,100,81.6,59.2]
plt.plot(x2,y2,label="Random Yes(DETECTION)",color='black',linestyle='dashed',linewidth=3,marker='D',markerfacecolor='green',markersize=5)
# plt.ylim(0,100)
plt.xlim(0,90)
plt.xlabel('percentage of malicious SUs(P_pu=0.6,alpha=0.6,No of SUs=100)')
plt.ylabel('Detection ratio')


# plt.figure(num=None,figsize=(8,6),dpi=80,facecolor='w',edgecolor='k')
# x1=[10,20,30,40,50,]
# y1=[39,41.6,77.6,83.0,93.0,100,100,100,100,100,100]
# plt.plot(x1,y1,label="Always No(DETECTION)",color='green',linestyle='dashed',linewidth=3,marker='X',markerfacecolor='blue',markersize=8)
# x2=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
# y2=[39.6,58,60.8,74.6,97.6,100,100,100,100,100,100]
# plt.plot(x2,y2,label="Random No(DETECTION)",color='blue',linestyle='solid',linewidth=3,marker='D',markerfacecolor='blue',markersize=8)
# # plt.ylim(0,100)
# plt.xlim(0,1)
# plt.xlabel('P_pu(percentage of malicious SUs=30,alpha=0.6,No of SUs=100)')
# plt.ylabel('Detection Ratio')
# plt.title('Graph for P_pu V/S false detection ratio for Always Yes and Random Yes attacks')

# plt.figure(num=None,figsize=(8,6),dpi=80,facecolor='w',edgecolor='k')
# x1=[10,20,30,40,50,60,70,80,90]
# y1=[58,44.4,27,23,26,38.2,16,4,10]
# plt.plot(x1,y1,label="Always No(FALSE DETECTION)",color='magenta',linestyle='dashdot',linewidth=1,marker='D',markerfacecolor='black',markersize=8)
# x2=[10,20,30,40,50,60,70,80,90]
# y2=[38,48,17.8,61.6,80,57,50.6,58.6,20.0]
# plt.plot(x2,y2,label="Random No(FALSE DETECTION)",color='blue',linestyle='dotted',linewidth=1,marker='H',markerfacecolor='green',markersize=8)
# plt.ylim(0,130)
# plt.xlim(0,130)
# plt.xlabel('Percentage of malicious user')
# plt.ylabel('Percentage of detection ratio')
# plt.title('Graph for malicious user V/S detection ratio for Always No and Random No attacks')
plt.legend()
plt.show()
