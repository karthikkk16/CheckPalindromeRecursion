def CheckPalindromeRecursion(s):
    if len(s)<=1:
        return 1
    if s[0]==s[-1]:
        return CheckPalindromeRecursion(s[1:-1])
    return 0
s=input()
print(CheckPalindromeRecursion(s))