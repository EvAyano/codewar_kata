def find_average(numbers):

    if numbers == []:
        return 0
    
    result = 0
    total = 0
    num_count = len(numbers)
    
    for num in numbers:
        total += num
    result = total/num_count
    
    return result