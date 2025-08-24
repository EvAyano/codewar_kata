from solution import generate_pairs

assert generate_pairs(0) == [[0, 0]], "Test n=0 failed"
assert generate_pairs(2) == [[0,0],[0,1],[0,2],[1,1],[1,2],[2,2]], "Test n=2 failed"
assert generate_pairs(3) == [[0,0],[0,1],[0,2],[0,3],[1,1],[1,2],[1,3],[2,2],[2,3],[3,3]], "Test n=3 failed"

print("All tests passed! 🎉")
