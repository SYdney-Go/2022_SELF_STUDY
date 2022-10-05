class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check = ""
        for i in t:
            print(i)
            if i in s:
                print(i, s)
                check += i
                print("check", check)
        # if s in checkand:
        #     return True
        # return False
            
solution = Solution()
print(solution.isSubsequence("abe", "abbe"))