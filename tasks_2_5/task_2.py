def sum_and_multi_nums(nums: tuple) -> tuple[int, int]:
    max_el, min_el = nums[0], nums[0]
    sum_num = 0
    for i in nums:
        if i > 0:
            sum_num += i
        if max_el < i:
            max_el = i
        elif min_el > i:
            min_el = i

    index_max_el = nums.index(max_el)
    index_min_el = nums.index(min_el)
    multip = 1

    if index_max_el - index_min_el < 0:
        index_max_el, index_min_el = index_min_el, index_max_el

    for i in range(index_min_el+1, index_max_el):
        multip *= nums[i]

    return sum_num, multip

nums = (-1, 1, 2, -4, 5, 3, 6, -3)
res = sum_and_multi_nums(nums)
print("sum positive:", res[0])
print("multiplications:", res[1])