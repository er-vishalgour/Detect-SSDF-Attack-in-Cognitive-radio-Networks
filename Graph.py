# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show() 

import matplotlib.pyplot as plt
import numpy as np
plt.figure(1)
x1=[1,2,3,4,5,6]
y1=[2,4,1,5,2,6]
plt.plot(x1,y1,label="line 1",color='green',linestyle='dashed',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)
x2=[2,7,8]
y2=[1,3,5]
plt.plot(x2,y2,label="line 2",color='blue',linestyle='dashed',linewidth=3,marker='x',markerfacecolor='blue',markersize=12)
plt.ylim(1,8)
plt.xlim(1,8)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title(' graph')

plt.figure(2)
x1=[1,2,3,4,5,6]
y1=[2,4,1,5,2,6]
plt.plot(x1,y1,label="line 1",color='red',linestyle='dashed',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)
x2=[2,7,8]
y2=[1,3,5]
plt.plot(x2,y2,label="line 2",color='blue',linestyle='dashed',linewidth=3,marker='x',markerfacecolor='blue',markersize=12)
plt.ylim(1,8)
plt.xlim(1,8)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title(' graph')


plt.legend()
plt.show()

