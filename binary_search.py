def binary_search(args,target):
    lower = args[0]
    upper = args[len(args)-1]
    if args[0] == target:
        return 0
    elif args[len(args)-1] == target:
        return args[len(args)-1]
    else:
        while lower <= upper:
            mid = int((upper+lower)/2)
            if args[mid] == target:
                return mid
            elif args[mid] > target:
                upper = mid-1
            elif args[mid] < target:
                lower = mid+1
        return f"{target} is not found in {args}"
    
print(binary_search([1,2,3,4,5],3))
print(binary_search([1,2,3,4,5],6))
