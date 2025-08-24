def solution(string):
    
    #return string[::-1]でいけるやん
    
    array = list(string)
    
    print(array)
    rev_ary = array[::-1]
    
    
    result = ''.join(rev_ary)
    
    return result