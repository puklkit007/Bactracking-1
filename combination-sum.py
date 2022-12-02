import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Normal recursion with backtracking
        self.res = []
        
        def combinations(index, sumLeft, arr):
            if index >= len(candidates):
                return
            
            if sumLeft == 0:
                # As we are using a single list arr, the Backtrack step removes elements and ultimately arr will be empty. So we need to copy it and append to result
                copyArr = copy.deepcopy(arr)
                self.res.append(copyArr)
                return
            elif sumLeft < 0:
                return
             
            # Not choose index
            combinations(index+1, sumLeft, arr)
            
            # Choose index
            # Action
            arr.append(candidates[index])
            # Recurse
            combinations(index, sumLeft - candidates[index], arr)
            # Backtracking
            arr.pop()
            
            
        combinations(0, target, list())
        return self.res
      
       # For loop recursion with backtracking
        self.res = []
        
        def combinations(index, sumLeft, arr):
            
            if sumLeft == 0:
                # As we are using a single list arr, the Backtrack step removes elements and ultimately arr will be empty. So we need to copy it and append to result
                copyArr = copy.deepcopy(arr)
                self.res.append(copyArr)
                return
            elif sumLeft < 0:
                return
            
            
            for i in range(index, len(candidates)):
                # Action
                arr.append(candidates[i])
                # Recurse
                combinations(i, sumLeft - candidates[i], arr)
                # Backtrack
                arr.pop()
                
        combinations(0, target, list())
        return self.res
