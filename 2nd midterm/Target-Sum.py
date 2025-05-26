import ast

def findTargetSumWays(nums, target):
    memo = {}

    def dfs(index, total):
        if index == len(nums):
            return 1 if total == target else 0

        if (index, total) in memo:
            return memo[(index, total)]
        plus = dfs(index + 1, total + nums[index])
        minus = dfs(index + 1, total - nums[index])

        memo[(index, total)] = plus + minus
        return memo[(index, total)]

    return dfs(0, 0)

nums_input = input("Enter numbers list: ")
target = int(input("Enter target sum: "))

nums = ast.literal_eval(nums_input)

result = findTargetSumWays(nums, target)
print(result)