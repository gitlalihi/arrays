'''Given an array A containing n integers. The task is to check 
whether the array is Monotonic or not. An array is monotonic if it is
 either monotone increasing or monotone decreasing. An array A is monotone 
 increasing if for all i <= j, A[i] <= A[j]. 

An array A is monotone decreasing if for all i <= j, A[i] >= A[j]. 
'''

def is_monotone(numlist) -> bool:
    for i in range(len(numlist) - 1):
        if numlist[i] > numlist[i + 1]:
            return False
    return True

numlist = [20, 289, 100, 56]
result = is_monotone(numlist)
print(result)

    


