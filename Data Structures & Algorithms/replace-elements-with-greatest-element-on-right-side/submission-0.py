class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            try:
                arr[i] = max(arr[i+1:])
            except ValueError:
                arr[len(arr)-1] = -1

        return arr
