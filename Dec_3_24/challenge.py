def color_invert(arr):
    return [255-arr[0],255-arr[1],255-arr[2]]


# The following code is to test all possible combinations it will take a couple of seconds to run due to the time complexity being O(n^3)
count = 0
for i in range(256):
    for j in range(256):
        for k in range(256):
            if color_invert(color_invert([i,j,k])) == [i,j,k]:
                count += 1
if count == 256**3:
    print("All possible combinations work!!")