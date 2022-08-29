# This one prints the sum of an array. No matter the length of the array.
# Like the multiply example I have a variable run the function

def sum_array(a):
    sum = 0
    for i in a:
     sum = sum + i
    return sum
a = []
ans = sum_array(a)
print(ans)
