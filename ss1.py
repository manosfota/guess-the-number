from matplotlib import pyplot as plt
import numpy as np
#x=np.random.random(5)*10
#y=np.random.random(5)*10
#plt.scatter(x,y)
#print(x,y)
#plt.show()
fig, ax = plt.subplots(figsize=(40, 25), layout='constrained')
x=[1,2,3,4]
y=[11,22,33,44]
y2=[1,2,3,4]
plt.subplot(2,1,1)
plt.plot(x,y)
ax.set_xlim([0,5])
plt.subplot(2,1,2)
plt.plot(x,y2)
plt.show()



fig=plt.figure()
ax = fig.add_subplot()
plt.show()
fig = plt.figure()
ax = fig.add_axes([1, 1, 1, 1])
ax.plot(x, y)
#fig=plt.figure()
#ax=fig.add_axes([5,5,5,45])
#ax.plot(x,y)


