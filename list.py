nums = [1, 2, 3, 4, 5]

nums[0] = 0   # change the first element of the list to 0

nums.append(1)  # add 1 at the end of the list

nums.remove(3) # remove 3 from the list

print(nums)

print(len(nums))  # print the length of the list

print(nums[1:4])  # print the elements from index 1 to 3 (4 is exclusive)

print(nums[::-1])  # print the list in reverse order

# loop concept

for num in nums :
    print(num)
