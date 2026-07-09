# Complete the 'countSubarraysWithSumAndMaxAtMost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. LONG_INTEGER k
#  3. LONG_INTEGER M
#
from collections import defaultdict
def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    # Write your code here
    n = len(nums)
    ans = 0
    i = 0

    while i<n:
        while i<n and nums[i]>M:
            i=i+1
        if i==n:
            break
        j=i
        while j<n and nums[j]<=M:
            j += 1

        # Prefix Sum on nums[i:j]
        prefix = defaultdict(int)
        prefix[0] = 1

        prefix_sum = 0

        for num in nums[i:j]:
            prefix_sum += num

            need = prefix_sum - k

            ans += prefix[need]

            prefix[prefix_sum] += 1

        i = j
    return ans

    print(result)
