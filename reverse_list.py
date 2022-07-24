def do_reverse(args:list,begin,end):

    while begin < end:
        args[begin],args[end] = args[end],args[begin]
        begin += 1
        end -= 1
    return args

print(do_reverse([1,2,3,4,5],0,4))