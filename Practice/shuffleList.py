def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    output=[None for i in range(0,len(nums))]
    pos=0
    prev=nums[0]
    result = zip(nums[:n],nums[n:])
    # for i in range(0,len(nums)-1):
    #     # output[pos] = nums[i]
    #     # output[pos+1] = nums[i+n]
    #     # pos+=2
    #     nums[i]=prev
    #     prev = nums[i+1]
    #     if i<n:
    #         nums[i+1]= nums[i-1+n]
    # print(nums)

if __name__ == '__main__':
    nums = [2,5,1,3,4,7]
    n = 3
    shuffle(nums,n)