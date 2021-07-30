class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def rec(ss: str, pp: str) -> bool:
            if not pp and not ss:
                return True
            if not pp :
                return False
            ppLen = len(pp)
            ssLen = len(ss)
            if ppLen > 1 and pp[1] == '*':
                if rec(ss, pp[2:]) == True:
                    return True
                if ssLen > 0 and (ss[0] == pp[0] or pp[0] == '.'):
                    return rec(ss[1:], pp)
            else:
                if ssLen > 0 and (ss[0] == pp[0] or pp[0] == '.'):
                    return rec(ss[1:], pp[1:]) 
            return False
        return rec(s, p)
