'''Given an array A of size N of integers. Your task is to find the minimum and maximum 
elements in the array.'''

def getMinMax( a, n):
    if n==1:
        return a[0]
    
    if a[0]>a[1]:
        max=a[0]
        min=a[1]
    else:
        min=a[0]
        max=a[1]
    
    for i in range(2,n):
        if a[i]>max:
            max=a[i]
        elif a[i]<min:
            min=a[i]
            
    return min,max
    
n=6
a={3,2,1,56,10000,167}
    