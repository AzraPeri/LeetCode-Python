class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S, T = len(s), len(t)
        if S == 0:
            return True
        if S > T:
            return False

        j = 0  # s içinde aranan konum
        for i in range(T):
            if t[i] == s[j]:
                j += 1
                if j == S:   # s’nin tüm karakterleri bulundu
                    return True
        return False          # t bitti ama s tamamlanamadı