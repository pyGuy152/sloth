def num_split(num):
    num = str(num)
    negative = False
    if (num[0] == "-"):
        negative = True
        num = num[1:]
    out = []
    for i in range(len(num)-1,-1,-1):
        if negative:
            out.append(int("-"+num[0]+("0"*i)))
        else:
            out.append(int(num[0]+("0"*i)))
        num = num[1:]
    return out

# ----------------Testing----------------

test_case = [39,-434,100,-3290,-200,4309,249378,-62837]
count = 0
print(f"Test:\toutput:")
for i in test_case:
    arr = num_split(i)
    num = 0
    for r in arr:
        num += r
    if num == i:
        count += 1
    print(f"{i}\t{arr}")
if count == len(test_case):
    print("All test cases passed")