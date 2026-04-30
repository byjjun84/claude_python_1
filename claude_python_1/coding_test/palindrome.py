def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c for c in s if c.isalnum() or c == ' ')
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("a b a", True),
        ("a b c", False),
        ("a ba", False),
        ("12321", True),
        ("12345", False),
        ("", True),
        ("a", True),
        ("Racecar", False),   # 대소문자 구분: R != r
        ("AaA", True),        # 대소문자 구분: A-a-A
        ("AaB", False),       # 대소문자 구분: A != B
    ]

    for s, expected in test_cases:
        result = is_palindrome(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] is_palindrome({s!r}) = {result}")
