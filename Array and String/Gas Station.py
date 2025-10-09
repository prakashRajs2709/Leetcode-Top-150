from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        tcost = 0
        curr = 0
        for i in range(len(gas)):
            remfuel = gas[i] - cost[i]
            tcost+=remfuel
            curr+=remfuel
            if curr<0:
                start = i+1
                curr=0
        if tcost>=0:
            return start
        return -1