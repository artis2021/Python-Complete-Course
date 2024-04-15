def sum_all(*nums):
    print(*nums)
    for i in nums:
        print(i*2)
    return sum(nums)

print(sum_all(1, 2, 3))
# print(sum_all(1,2,3,4,4))
# print(sum_all(1,3,4,4,4,4,4,4,4,4,4))
