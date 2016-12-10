import time

totalRuns = 5
changeTomake = 57

def getNumWays(changeTomake, coinValueList, allowedcoinsIndex):
    
    numOfWays = 0
    # We have reached base case, empty set is a combination. So return 1
    if changeTomake == 0:
        return 1
    
    if allowedcoinsIndex <= 0:
        return 0
    
    
    if changeTomake >= coinValueList[allowedcoinsIndex - 1]:
        # Get total ways with using 1 coin of last denomination + total ways without using last denomination
        numOfWays = getNumWays(changeTomake-coinValueList[allowedcoinsIndex - 1], coinValueList, allowedcoinsIndex) \
                    + getNumWays(changeTomake, coinValueList, allowedcoinsIndex - 1)
    else:
        numOfWays = getNumWays(changeTomake, coinValueList, allowedcoinsIndex - 1)

    return numOfWays

def main():
    coinValueList = [1, 2, 5, 10, 20]
    allowedcoinsIndex = len(coinValueList)
    timeTaken = 0
    numOfWays = 0
    for iter in range(totalRuns):
        start = time.time()
        numOfWays = getNumWays(changeTomake, coinValueList, allowedcoinsIndex)
        timeTaken += (time.time() - start)
        
    print("Number of ways of coin change ", numOfWays)
    print("Total Time Taken To find Total ways of coin change for ", changeTomake,
           "Using Naive Recursion ", timeTaken/totalRuns)

main()