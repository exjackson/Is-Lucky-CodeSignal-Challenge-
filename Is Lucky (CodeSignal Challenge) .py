def solution(n):
    x = []
    first_half = 0
    second_half = 0
    nums = list(str(n))
    for i in range(0,len(nums)//2):
        first_half += int(nums[i])
    for j in range(len(nums)//2,len(nums)):
        second_half += int(nums[j])
    if first_half == second_half:
        print(first_half,second_half)
        return(True)
    else:
        print(first_half,second_half)
        return(False)


