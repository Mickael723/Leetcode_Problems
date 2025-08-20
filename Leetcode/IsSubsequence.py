
def isSubsequence(s: str, t: str) -> bool:

    if s == "": return True

    sp = 0
    tp = 0

    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
            tp += 1
        else:
            tp += 1
    if sp == len(s):
        return True
    else:
        return False

if __name__=="__main__":
    print(isSubsequence('abc', 'ahbgdc'))
    print(isSubsequence('bb', 'ahbgdc'))
    print(isSubsequence('b', 'c'))
    print(isSubsequence('axc', 'ahbgdc'))
                