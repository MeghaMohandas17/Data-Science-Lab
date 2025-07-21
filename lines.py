import numpy as np 
import matplotlib.pyplot as plt
x=np.array([1,2,6,18])
y=np.array([3,10,12,20])
plt.plot(x,y,marker='o',linestyle='dotted',color='red',mfc='green')
plt.title('LINE DIAGRAM')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
