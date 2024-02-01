class TimeMap:
    map = {}

    def __init__(self):
        return

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = self.map[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        for i in self.map[key]:
            if i[0] == timestamp:
                return i[1]
        return self.map[key][-1][1]
