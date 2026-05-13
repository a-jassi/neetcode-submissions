class TimeMap:

    def __init__(self):
        self.kvStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvStore:
            return ""

        vals = self.kvStore[key]
        l, r = 0, len(vals) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            ts, val = vals[m]

            if ts == timestamp:
                return val
            elif ts < timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1
        return res
        
