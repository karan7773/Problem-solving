def substring(s):
    substring=""
    n=len(s)
    for i in range(1,n//2+1):
        if n%i==0:
            substring=s[:i]
            if substring*(n//i)==s:
                return True
    return False

s="ababab"
print(substring(s))
print(substring("abcabcabc"))
print(substring("aaabcc"))