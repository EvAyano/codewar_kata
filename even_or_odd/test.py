from solution import even_or_odd

# Test 1: 偶数
assert even_or_odd(2) == "Even", "Test 1 failed"

# Test 2: 奇数
assert even_or_odd(3) == "Odd", "Test 2 failed"

# Test 3: 0（偶数として扱う）
assert even_or_odd(0) == "Even", "Test 3 failed"

# Test 4: 負の偶数
assert even_or_odd(-4) == "Even", "Test 4 failed"

# Test 5: 負の奇数
assert even_or_odd(-5) == "Odd", "Test 5 failed"

print("All tests passed! 🎉")
