import statistics

list_of_nums = [1, 5, 6, 77, 86]

x = statistics.kde_random(list_of_nums, h=1.5)

print(x)
