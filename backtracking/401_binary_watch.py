from itertools import combinations
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]

        def backtrack(hours_took):

            if hours_took > turnedOn:
                return

            minutes_took = turnedOn - hours_took

            for curr_hours in combinations(hours, hours_took):

                sum_hours = sum(curr_hours)

                if sum_hours >= 12:
                    continue

                for curr_minutes in combinations(minutes, minutes_took):

                    sum_minutes = sum(curr_minutes)

                    if sum_minutes >= 60:
                        continue

                    ans.append("%d:%02d" % (sum_hours, sum_minutes))

            backtrack(hours_took + 1)

        ans = []

        backtrack(0)
        return ans