from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_of_anagrams = defaultdict()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in map_of_anagrams:
                map_of_anagrams[sorted_word] = []

            map_of_anagrams[sorted_word].append(word)
        return list(map_of_anagrams.values())
