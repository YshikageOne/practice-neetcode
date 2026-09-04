class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result  = {} #stores charCount to the list of words that share charCount

        for string in strs:
            count = [0] * 26 #one for each letter a-z

            for currentChar in string:
                count[ord(currentChar) - ord("a")] += 1

            key = tuple(count)

            if key not in result:
                result[key] = []
            result[key].append(string)

        return list(result.values())