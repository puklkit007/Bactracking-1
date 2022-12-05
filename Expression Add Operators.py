class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
     
        self.res = []
        
        
        def helper(num, target, index, calc, tail, path):
            
            if index == len(num):
                if calc == target:
                    self.res.append(path)
                return
            
            for i in range(index, len(num)):
                if index != i and num[index] == '0': continue
                curr = int(num[index: i+1])
                strCurr = str(curr)
                
                if index == 0:
                    helper(num, target, i+1, curr, curr, strCurr+path)
                else:
                    # add +
                    helper(num, target, i+1, calc + curr, curr, path + "+" + strCurr)
                    # add -
                    helper(num, target, i+1, calc - curr, -curr, path + "-" + strCurr)
                    # add *
                    helper(num, target, i+1, calc - tail + tail * curr, tail * curr, path + "*" + strCurr)
            
            
            
        helper(num, target, 0, 0, 0, '')
        return self.res
