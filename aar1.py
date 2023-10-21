# Given an array of integers, find the sum of its elements.

def sum_of_array(num):
    sum= 0
    for i in num:
        sum= sum+ i
    return sum

if __name__=='__main__':
    num=[10,20,30]
    n=len(num)
    ans=sum_of_array(num)
    print(" The sum of the numbers in this array is ", ans)

