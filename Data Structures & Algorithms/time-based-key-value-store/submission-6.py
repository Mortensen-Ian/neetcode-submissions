class TimeMap:

    def __init__(self):
        self.d = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((timestamp, value))
        else:
            self.d[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        l = 0
        r = len(self.d[key]) - 1
        res = ""
        restime = 0
        while l <= r:
            m = (l + r) // 2
            t = self.d[key][m][0]
            if t <= timestamp:
                if restime <= t:
                    res = self.d[key][m][1]
                l = m + 1
            else:
                r = m - 1

        return res
