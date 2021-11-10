def get_lps(s):
    m = len(s)
    lps = [0] * m
    i = 1
    l = 0 # matched length
    
    while i < m:
        if s[i] == s[l]:
            l += 1
            lps[i] = l
            i += 1
           
        else:
            if l != 0:
                l = lps[l - 1]
                
            else:
                i += 1
    return lps
def kmp(haystack, needle):
    if needle == '':
        return 0
    n = len(haystack)
    m = len(needle)
    lps = get_lps(needle)
    i = 0
    j = 0
    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
           
            if j == m:
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1
        
    
