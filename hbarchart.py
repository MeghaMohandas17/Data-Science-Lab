import numpy as np
import matplotlib.pyplot as plt
x=np.array(['Java','Python','PHP','Javascript','C#','C++'])
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
colors=['Blue','Green','Orange','Red','Purple','Hotpink']
plt.barh(x,y,color=colors)
plt.title('HORIZONTAL BAR CHART')
plt.ylabel('Programming language')
plt.xlabel('Popularity')
plt.show()
