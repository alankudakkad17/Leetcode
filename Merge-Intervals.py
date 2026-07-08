def mergeHighDefinitionIntervals(intervals):
    # Write your code here
    if not intervals:
        return []
    intervals.sort()
    l=len(intervals)
    result=[intervals[0]]
    for x in intervals[1:l]:
        if result[-1][1]<x[0]:
            result.append(x)
        else:
            result[-1][1] = max(result[-1][1], x[1])
    return result
            
