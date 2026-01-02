def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    found = False

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            print(f"Naive      → Pattern found at index {i}")
            found = True

    if not found:
        print("Naive      → Pattern not found")


def rabin_karp(text, pattern, d=256, q=101):
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q

    p_hash = 0
    t_hash = 0
    found = False

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                print(f"Rabin-Karp → Pattern found at index {i}")
                found = True

        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            t_hash = (t_hash + q) % q

    if not found:
        print("Rabin-Karp → Pattern not found")


# -------- MAIN --------
text = input("Enter the text string: ")
pattern = input("Enter the pattern string: ")

print("\n--- Naive String Matching ---")
naive_string_match(text, pattern)

print("\n--- Rabin–Karp Algorithm ---")
rabin_karp(text, pattern)