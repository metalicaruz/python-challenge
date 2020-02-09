import csv, os, collections

file_to_load=os.path.join("Resources","budget_data.csv")
file_to_output=os.path.join("Analysis","budget_analysis.txt")

total_months=0
prev_revenue=0
net_revenue=0
revenue_change_list = []



with open(file_to_load, "r") as revenue_data:
    reader = csv.reader(revenue_data)
    reader = collections.OrderedDict(reader)
    data = list(reader.items())

tmp = []
for i in data[1:]:
    total_months += 1
    net_revenue += int(i[1])
    tmp.append(i[1])

revenue_change_list = []
revenue_data = [int(y) - int(x) for x,y in zip(tmp,tmp[1:])]
revenue_change_list.extend(revenue_data)
revenue_average = sum(revenue_change_list)/len(revenue_change_list)


revenue_change_list.insert(0, 0)
greatest_increase = max(revenue_change_list)
greatest_decrease = min(revenue_change_list)

max_index = [i for i, j in enumerate(revenue_change_list) if j == greatest_increase]
min_index = [i for i, j in enumerate(revenue_change_list) if j == greatest_decrease]

output=(
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {net_revenue}\n"
    f"Average Change: {round(revenue_average,2)}\n"
    f"Greatest Increase in Profits: " + data[max_index[0]][0] + " ($" + str(revenue_change_list[max_index[0]]) +")\n"
    f"Greatest Decrease in Profits: " + data[min_index[0]][0] + " ($" + str(revenue_change_list[min_index[0]])  +")\n"
)
print(output)

with open(file_to_output, "w") as text_file:
    text_file.write(output)

