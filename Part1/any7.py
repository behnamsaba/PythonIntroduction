def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    x = 0

    # YOUR CODE HERE
    for i in nums:
        if i == 7:
            x += 1
    
    if x > 0:
        return True
    else:
        return False
    

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

