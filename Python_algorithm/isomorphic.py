class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def count_alpha(l):
            num = ""
            r_dict = {}
            for i, each in enumerate(l):
                if each not in r_dict:
                    r_dict[each] = i
                num += " " + str(r_dict[each])
            return num
        
        s_num = count_alpha(s)
        t_num = count_alpha(t)
        if s_num == t_num:
            return True
        else:
            return False