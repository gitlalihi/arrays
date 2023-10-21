#Python Program to Split the array and add the first part to the end
def split_add_array(arr,n,k):
    
    return ( arr[k::] +(arr[:k])+ (arr[::])) 

if __name__=='__main__':
    arr = [10,20,30,40,50,60]
    n = len(arr)
    position = 2
    arr = split_add_array(arr, n, position)
    for i in range(0, n):
       print(arr[i], end=' ')