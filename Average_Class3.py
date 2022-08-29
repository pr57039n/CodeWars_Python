your_points = 96
class_points = [11,55,15,69,22,100,52]

def better_than_average(class_points, your_points):
    length = len(class_points) + 1
    total_sum = sum(class_points) + your_points
    final = total_sum / length
    return print(your_points > final)
better_than_average(class_points, your_points)
