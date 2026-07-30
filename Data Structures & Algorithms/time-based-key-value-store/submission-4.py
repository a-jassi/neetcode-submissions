class TimeMap:

    def __init__(self):
        self.kvStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvStore:
            self.kvStore[key] = []

        self.kvStore[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvStore:
            return ""
        
        vals = self.kvStore[key]
        l, r = 0, len(vals) - 1
        resI, resTime = -1, -1

        while l <= r:
            mid = (l + r) // 2
            
            val, time = vals[mid]
            if time == timestamp:
                return val
            elif time > timestamp:
                r = mid - 1
            else:
                if time > resTime:
                    resI = mid
                    resTime = time
                l = mid + 1
        
        return vals[resI][0] if resI != -1 else ""

