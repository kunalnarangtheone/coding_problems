st = "aaaabbbccd"

def run_length_encoding(s):
    if len(s) == 0:
        return ""
    
    if len(s) == 1:
        return 1 * s[0]

    encoding = ""
    counter = 1
    n = len(s)

    for i in range(1, n):
        if i == n - 1:
            if s[i] == s[i - 1]:
                encoding+=f"{counter + 1}{s[i - 1]}"

            else:
                encoding+=f"{counter}{s[i - 1]}"
                encoding+=f"1{s[i]}"
            
        else:
            if s[i] == s[i - 1]:
                counter+=1

            else:
                encoding+=f"{counter}{s[i - 1]}"
                counter = 1

        print(i, counter)

    return encoding

print(run_length_encoding(st))



