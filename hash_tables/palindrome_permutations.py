def can_form_palindrome(s):
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1
