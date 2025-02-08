class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        string_hash = {}
        for string in strs:
            order_string = "".join(sorted(string))
            if string_hash.get(order_string):
                string_hash.get(order_string).append(string)
                continue
            string_hash[order_string] = [string]
        
        return list(string_hash.values())