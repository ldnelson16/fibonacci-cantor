def main():
  num_nums = input("How many fibonacci numbers do you want? ")

  if num_nums.isnumeric():
    num_nums=int(num_nums)-2
    nums = [0,1]
    while num_nums>0:
      num_nums-=1
      nums.append(nums[-2]+nums[-1])
    for num in nums: 
      print(num)
  else: 
    print("Incorrect input, try again")
    main()

main()
