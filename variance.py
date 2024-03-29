arr = [3, 8 , 9, 10 , 11]

arrlength = len(arr)

def getMean(arr):
    mean = 0
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    mean = total/ arrlength
    print("The mean is:")
    print(mean)
    return mean

def getVariance(arr):
    mean = getMean(arr)
    total = 0
    result = 0
    result2 = 0
    storeResult = []
    storeSquared = []
    finalVariance = 0
    for i in range(len(arr)):
        result = arr[i] - mean
        storeResult.append(result)
    print(storeResult)
    for i in range(len(arr)):
        result2 = storeResult[i] ** 2
        storeSquared.append(result2)
        total += storeSquared[i]
    finalVariance = total / mean
    print(storeSquared)
    print(total)
    print(finalVariance)
    
    
    
        
      
    
getVariance(arr)