

def balanced_brackets(s):
    openn = "({[<"
    close = ")}]>"

    mapp = {
        "(": ")",
        "{": "}",
        "[": "]",
        "<": ">" 
    }

    stack = []

    for char in s:
        if not stack:
            if char in openn:
                stack.append(char)
            else:
                return 0
            
        else:
            if char in close:
                if char == mapp[stack[-1]]:
                    stack.pop()

                else:
                    return 0

            elif char in openn:
                stack.append(char)

    return 1 if len(stack) == 0 else 0

print(balanced_brackets("[](){}"))
print(balanced_brackets("(h[e{l<l>o}!]~)()()())"))

        