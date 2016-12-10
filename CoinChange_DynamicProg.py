import time

totalRuns = 5
changeTomake = 1023473

def main():
    coinValueList = [1, 2, 5, 10, 20]
    allowedcoinsIndex = len(coinValueList)
    timeTaken = 0
    
    for iter in range(totalRuns):
        start = time.time()
        dpArray = [[0 for y in range(changeTomake+1)] for x in range(allowedcoinsIndex+1)]
        
        #Base case
        for i in range(1, allowedcoinsIndex+1):
            dpArray[i][0] = 1
    
        for i in range(1, allowedcoinsIndex+1):
            for j in range(1, changeTomake+1):
                if(coinValueList[i-1] <= j):
                    dpArray[i][j] = dpArray[i][j - coinValueList[i-1]] + dpArray[i-1][j]
                else:
                    dpArray[i][j] = dpArray[i-1][j]
        
        timeTaken += (time.time() - start)
        
    print("Number of ways of coin change ",dpArray[allowedcoinsIndex][changeTomake])
    print("Total Time Taken To find Total ways of coin change for ", 
          changeTomake, "Using Dynamic Programming ", timeTaken/totalRuns)

main()