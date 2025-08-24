from solution import make_negative

# Test 1: 正の数
assert make_negative(1) == -1, "Test 1 failed"

# Test 2: すでに負の数
assert make_negative(-5) == -5, "Test 2 failed"

# Test 3: ゼロ
assert make_negative(0) == 0, "Test 3 failed"

# Test 4: 大きな正の数
assert make_negative(123456) == -123456, "Test 4 failed"

# Test 5: 大きな負の数
assert make_negative(-999999) == -999999, "Test 5 failed"

print("All tests passed! 🎉")
