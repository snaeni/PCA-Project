import time

coinDen = []
totalRuns = 5
changeTomake = 1023473

"""
CoinChangeExt'() function
CoinChangeExt'(i, amount, rExt) = Array [CoinChangeExt(i+1, j) j from 0 to amount] 
    Where rExt = Array [CoinChangeExt(i, j) j from 0 to amount] 
"""
def cnchngExt_(i, amount, rExt):
    global coinDen
    rExt_ = [0 for u in range(amount+1)]
    rExt_[0] = 1
    for c in range(1, amount+1):
        if(c >= coinDen[i]):
            rExt_[c] = rExt_[c-coinDen[i]] + rExt[c]
        else:
            rExt_[c] = rExt[c]

    return rExt_


"""
CoinChangeExt() function
    CoinChangeExt(i, amount)
Returns NumOfWays to make change of amount using 
    first i coin denoms in coinDen
"""
def cnchngExt(numCnDenoms, amount):
    global coinDen
    
    rExt = [0 for u in range(amount+1)]
    i = 0
    while i != numCnDenoms:
        rExt = cnchngExt_(i, amount, rExt)
        i+=1
    
    return rExt[amount]
    

def main():
    global coinDen
    coinDen = [1, 2, 5, 10, 20]
    amount = changeTomake
    totalNumWays = 0
    numCnDenoms = len(coinDen)
    timeTaken = 0

    for iter in range(totalRuns):
        start = time.time()
        if(amount > 0 and numCnDenoms > 0):
            totalNumWays = cnchngExt(numCnDenoms, amount)
        
        timeTaken += (time.time() - start)
        
    print("Number of ways of coin change ", totalNumWays)
    print("Total Time Taken To find Total ways of coin change for ", amount, 
          "Using Optimized Systematic method Implementation ", timeTaken/totalRuns)

main()