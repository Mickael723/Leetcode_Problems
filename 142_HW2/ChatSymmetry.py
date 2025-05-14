def min_cost_to_make_palindrome(s, prices):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i + 1][j] + prices[s[i]],
                    dp[i][j - 1] + prices[s[j]]
                )
    return dp[0][n - 1]

if __name__ == "__main__":
    n, k = map(int, input().split())

    # Read costs
    prices = {}
    for i in range(k):
        ch = chr(ord('a') + i)
        prices[ch] = int(input())

    s = input()
    print(min_cost_to_make_palindrome(s, prices))