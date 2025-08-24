def generate_pairs(n):
    result = []
    
    for a in range(n+1):
      for b in range(n+1):
        if b >= a:
         result.append([a, b])
    return result
