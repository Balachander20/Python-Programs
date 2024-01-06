class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        d = {0 : 0}
        for st, endNext, money in jobs:
            profitMax, options = 0, []
            for end, profit in d.items():
                if end <= st: profitMax = max(profitMax, profit)
                else: options.append((end, profit))
            
            options.append((st, profitMax))
            options.append((endNext, profitMax + money))
            
            options.sort(key=lambda x: (-x[1], x[0]))
            limit, d = options[0][0] + 1, {}
            for end, profit in options:
                if end < limit:
                    limit = end
                    d[end] = profit

        return options[0][1]
        