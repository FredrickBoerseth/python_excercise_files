import csv

# write these to a csv file, each list in row, each item separated by comma
the_list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on fire", "Flight"]]

with open("movies.txt", "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(the_list[0])
    w.writerow(the_list[1])
    w.writerow(the_list[-1])
