import random
nums = [str(num) for num in random.sample(range(69), 6)]
print("Numbers: {}\nPowerball: {}".format(", ".join(nums[0:5]), nums[5]))