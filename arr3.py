#Python Program for Array Rotation by left
def rotatationbyleft(arr,d,n):
    temp=[]
    i=0
    while(i<d):
            temp.append(arr[i])
            i=i+1
    i=0
    while(d<n):
            arr[i]=arr[d]
            i= i+1
            d=d+1
    arr[:]=arr[:i] + temp
    return arr

if __name__ == '__main__' :
    arr = [10,20,30,40,50,60,70,80]
    print("Array after left rotation is: ", rotatationbyleft(arr, len(arr),2))

            
