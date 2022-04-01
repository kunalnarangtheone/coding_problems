def isOdd(num):
    if num%2==0:
        return False
    else:
        return True

def someRecursive(arr, cb):

    if len(arr) == 0:
        return False
    elif len(arr) == 1:
        return cb(arr[0])
    elif cb(arr[-1]):
        return True
    else:
        return someRecursive(arr.pop(), cb)

print(someRecursive([], isOdd))
