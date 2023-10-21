#Python Program for Find remainder of array multiplication divided by n

def remainder_array(arr):
   i= 0
   x=1
   n=11
   for  i in range (len(arr)):
      x = (x *(arr[i] % n )) % n
   print(x%n)

if __name__=='__main__':
   arr=[10,20,30,40]
   remainder_array(arr)