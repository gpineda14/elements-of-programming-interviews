def is_palindromic(s):
    # s[~i] == s[-(i + 1)]
    return all(s[i] == s[~i] for i in range(len(s) // 2))
