def median(num_list):
    '''
    A function for calculating the median of a list of nums. 
    '''
    sortedList = sorted(num_list)
    middle = sortedList[len(num_list)//2] 
    return middle

def simple_test():
    exp = 2
    obs = median([2,3,1])
    assert exp == obs

if __name__ == "__main__":
    simple_test()