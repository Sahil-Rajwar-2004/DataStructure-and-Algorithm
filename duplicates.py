nums = [1,2,4,5,1,3,4]
sort = sorted(nums,reverse = False)
count = 0
repeat = {}

for i in sort:
    if sort.count(i) >= 1:
        repeat.update({i:sort.count(i)})
print(repeat)

