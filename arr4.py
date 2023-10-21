# Python program to reverse an array 
def reverse(arr,d):
    r=(arr[d:]) +(arr[:d])
    return r
if __name__ =='__main__':
    arr=[10,20,30,40,50,60]
    d=1
    print(" The reversed array is ", reverse(arr,d))