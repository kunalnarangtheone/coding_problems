T = [73, 74, 75, 71, 69, 72, 76, 73]

# To find PLE
def ple(T):
    size = len(T)
    ple_stack = []
    previous_less = [-1] * size

    for i in range(size):
        while ple_stack and T[ple_stack[-1]] > T[i]:
            ple_stack.pop()

        previous_less[i] = ple_stack[-1] if ple_stack else -1
        ple_stack.append(i)

    return previous_less

# To find NLE
def nle(T):
    size = len(T)
    nle_stack = []
    next_less = [-1] * size

    for i in range(size):
        while nle_stack and T[nle_stack[-1]] > T[i]:
            next_less[nle_stack.pop()] = i

        nle_stack.append(i)

    return next_less

print(ple(T))
