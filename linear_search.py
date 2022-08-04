def linear_search(args,target):
    for i in range(0, len(args)):
        if args[i] == target:
            return i
    else:
        return f"{target} is not in {args}"

print(linear_search([1,2,3,4,5],4))