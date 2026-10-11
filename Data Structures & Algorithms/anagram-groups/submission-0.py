class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Sort each string and throw it into a dictionary.
        Anagrams = dict()
        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString in Anagrams:
                Anagrams[sortedString].append(s)
            else:
                Anagrams[sortedString] = [s]
        return list(Anagrams.values())