# This variant uses two different functions then prints the result of the average.

your_points = [44]
class_points = [55,16,19,24,97,100]

def better_than_average(class_points, your_points):
    amt = len(class_points) + 1
    total = sum(class_points)
    total2 = sum(your_points)
    total3 = total + total2
    final = total3 / amt
    return final

def mypoints(your_points):
    convert = sum(your_points)
    return convert

if mypoints(your_points) > better_than_average(class_points, your_points):
    print(True)
else:
    print(False)
