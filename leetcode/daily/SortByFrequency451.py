class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = {}
        for char in s:
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1
        sorted_freq_map = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        res = ""
        for char in sorted_freq_map:
            count = char[1]
            while count != 0:
                res += char[0]
                count -= 1
        return res
