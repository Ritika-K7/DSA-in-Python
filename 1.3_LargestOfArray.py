'''Given an array A[] of size n. The task is to find the largest element in it.'''

def largest( arr, n):
    largest=arr[0]
    for elem in arr :
        if(elem>largest):
            largest=elem
    return largest   


n=5
arr={1,8,7,56,90}
    

