from solution import find_average

# Test 1
assert find_average([1, 2, 3]) == 2.0, "Test 1 failed"
# Test 2
assert find_average([5, 10]) == 7.5, "Test 2 failed"
# Test 3
assert find_average([]) == 0, "Test 3 failed"
# Test 4
assert find_average([0, 0, 0]) == 0.0, "Test 4 failed"

print("All tests passed! 🎉")
