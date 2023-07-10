class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checked = {}
        for value in strs:
            valuesorted = ''.join(sorted(value))
            if valuesorted in checked:
                checked[valuesorted].append(value)
            else:
                checked[valuesorted] = [value]
        return list(checked.values())
