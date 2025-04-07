import array as ar
import numpy as np


 

# FUNCTION FOR ONE-DIMENSION ARRAY
def one_dimen():
    global n 
    n=(int(input('Give the number of elements:\n')))
    print("Give me the the numbers of array")
    for i in range(n):
      arr.append(int(input("{i}th: ".format(i=i+1))))
    print("\nArray a is structured as follow:\n",arr)
    return arr

# FUNCTION FOR TWO-DIMENSION ARRAY
def two_dimen():
    a=int(input("Give me the number of rows of the array : "))
    b=int(input("Give me the number of columns of the array : "))
    for i in range(a):
         for j in range(b):
            arr.append(input("Give me the [{i},{j}] element of array: ".format(i=i+1, j=j+1)))
    
# FUNCTION  TO  ASSORT ARRAY   
def bubble_sort(a):
    i=0
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]     
    print("The array in ascending order is :",arr)


def largest_fig_one_dim(b):
    i=0
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr[n-1-i])
    

def main():
    print("Hello World!")
    global arr
    global n # range of one-dimensional array
    arr=[]
    print("Choose the dimension of array")
    print("Option 1: one-dimension")
    print("Option 2: two-dimension")
    dim=int(input())
    if dim==1:
        print("\n")
        one_dimen()  
    elif (dim==2):
        print("\n")
        two_dimen()
    else:
        print("------------Invalid Choise------------")
        print("Please choose between the option -1- or -2-")
    bubble_sort(arr)

if __name__ == "__main__":
    main()

