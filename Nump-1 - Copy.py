import array as ar
import numpy as np


# FUNCTION FOR ONE-DIMENSION ARRAY
def one_dimen():
    n=(int(input('\nGive the number of elements: ')))
    print("\nGive me  the numbers of array: ")
    arr =np.array([0 for i in range(n)])
    for i in range(n):
      arr[i]=(int(input("{i}th: ".format(i=i+1))))
    print("\nArray a is structured as follow :",arr,"\n")
    even_odd_nbr(arr,n)
    return arr

#FUNCTION FOR ODD OR EVEN NUMBER
def even_odd_nbr(arr,n):
    i=0
    h=0
    g=0
    for arr[i] in range (n):
        if (arr[i] //2==0):
            h=h+1
        else:
            g=g+1
    print("The amount of even number is : ",h)
    print("\nThe amount odd number   is : ",g)

# FUNCTION FOR TWO-DIMENSION ARRAY
def two_dimen():
    rows=int(input("\nGive me the number of rows of the array : "))
    col=int(input("\nGive me the number of columns of the array : "))
    sum=rows*col
    arr =np.array([ [0 for x in range( rows )] for y in range( col ) ])
    for i in range(rows):
         for j in range(col):
            arr[i][j]=(input("Give me the  arr[{i},{j}] : ".format(i=i+1, j=j+1)))
    pr_arr=np.arange(sum).reshape(rows,col) 
    print(pr_arr)
    print(arr)
    #arr1d = arr.reshape(-1)
    #print(arr1d) 
    return arr
    

# FUNCTION  TO  ASSORT ARRAY   
def bubble_sort(b,ch_op):
    if (ch_op==1):
         i=0 
         for i in range (len(b)):
            for j in range (0,len(b)-i-1):
                if (b[j]>b[j+1]):
                    b[j],b[j+1]=b[j+1],b[j]    
         print("\nThe array in ascending order is :",b)
    elif (ch_op==2):
        for i in range(len(b)):
            for j in range(0,len(b)-i-1):
                if (b[i][j]>b[i][j+1]):
                    b[i][j],b[i][j+1]=b[i][j+1],b[i][j] 
        print("\nThe array in ascending order is :",b)

    else:
        pass                   
    return b

#Function for greatest and smallest element
def compare_fig_one_dimen(arr):
    n = int(len(arr))
    print("\nThe greatest number of array is : ",arr[n-1])
    print("\nThe smaller  number of array is : ",arr[0])
    
#Function for choose option 
def choose_option():
    print("-Choose the dimension of array-")
    print("-Option (1): one-dimension")
    print("-Option (2): two-dimension")
    dim=int(input())
    return dim

#Function for Processing
def access_array(a):
    if (a==1):
        arr=one_dimen() 
    elif (a==2):
        arr=two_dimen()
    else:
        print("-------------Invalid Choise-------------")
        print("Please choose between the option -1- or -2-")
    return arr
    

def main():
    ch_op=choose_option()
    r=access_array(ch_op)
    r_sorted=bubble_sort(r,ch_op)
    compare_fig_one_dimen(r_sorted) 


if __name__ == "__main__":
    main()

