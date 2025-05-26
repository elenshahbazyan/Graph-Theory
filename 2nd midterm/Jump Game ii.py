import ast

def Jump(nums):
  jumps = 0
  current_end =0
  farthest = 0

  for i in range(len(nums)-1):
    farthest = max(farthest,i +nums[i])
    if i == current_end:
      jumps +=1
      current_end = farthest
  return jumps

nums_input = input("Enter the list:")
nums = ast.literal_eval(nums_input)

print(Jump(nums))