# sets

nums = {1,2,2,3,3,4,5}

print(nums)  # sets do not allow duplicate values, so the output will be {1, 2, 3, 4, 5}

nums.add(6)  # add 6 to the set
nums.remove(2)  # remove 2 from the set
print(nums)

# tuples

nums_tuple = (1, 2, 3, 4, 5)
print(nums_tuple)  # tuples are immutable, so the output will be (1, 2, 3, 4, 5)

# tuples values cannot be changed, but we can access them using indexing
print(nums_tuple[0])  # print the first element of the tuple, output will be
