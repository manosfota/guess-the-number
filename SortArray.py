import numpy as np
a=np.array([1,2,3,4])
d=np.array([9,10,11,12,13,14,15,16])
#print(np.concatenate((b,d)))
#print(b.ndim)
#print(b.shape)
#print(a.itemsize)
#print(b.size)
#print(b[0,1:-1:2])

#b[:,4]=[15,27]#sos
#print(b[1,:3]
#print(b[1:,2])
#b[1,5]=30
#b[:,2]=[77,44]
#print(b)

c=np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
#print(c[2,1,1])
c[:,1,:]=[[4,4],[3,3],[9,9]]
#print(c)
#print(np.zeros((3,3,3,2)))
#print(4,2,2)
#print(np.full((2,2),99))
#print(np.random.rand(4,2))
s3=np.array([[[1,2,3],
            [4,5,6],
            [7,8,9]],
            [[10,11,12],
            [13,14,15],
            [16,17,18]]])
#print(s3[0:,1,0:2])
print(type(s3))

import pandas as pd
df=pd.DataFrame(b)
#print(df)

#CREATING ARRAYS
ones=np.ones((2,2))
#print(ones)
random_ar=np.random.random((3,3))
#print(random_ar)
random_ar_1=np.random.rand(5,3)

#SOS
r_a=np.random.randint(0,10,size=(3,5))
#print(r_a)

r_a_1=np.random.randint(3,size=(1,3,4,5))
#print(r_a_1)
print("***********************")
#print(r_a_1[0:1,0:,2])
b=np.array([[1,2,3,4],[9,10,11,12]])
#m=r_a_1.reshape(2,4,6,5)
np.random.seed(0)
mat1=np.random.randint(10,,size=(5,3))

print(m)




