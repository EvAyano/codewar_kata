from solution import solution

# Test 1: 通常の文字列
assert solution("world") == "dlrow", "Test 1 failed"

# Test 2: 短い文字列
assert solution("word") == "drow", "Test 2 failed"

# Test 3: 1文字
assert solution("a") == "a", "Test 3 failed"

# Test 4: 空文字列
assert solution("") == "", "Test 4 failed"

# Test 5: 数字や記号を含む
assert solution("123!abc") == "cba!321", "Test 5 failed"

print("All tests passed! 🎉")
