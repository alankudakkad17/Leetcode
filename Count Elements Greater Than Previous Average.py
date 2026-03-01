def countResponseTimeRegressions(responseTimes):
    if not responseTimes:
        return 0
    if len(responseTimes)==1:
        return 0
    currentsum=responseTimes[0]
    num=0
    
    for x in range(1,len(responseTimes)):
        if((currentsum/x)<responseTimes[x]):
            num+=1
            currentsum=responseTimes[x]+currentsum
        else:
            currentsum=responseTimes[x]+currentsum
            continue
    return num
