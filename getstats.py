import os
import datetime
import csv
import pandas

directory = "fixtures"
string_to_search = "asdf"


data = {'Filepath':[], 'Stat':[]}

for subdir, dirs, files in os.walk(directory):
    for file in files:
        filepath = subdir + os.sep + file
        print(str(file))
        read_file = open(filepath)
        for position, line in enumerate(read_file):
            if string_to_search in line:
                    print("found it! 2")
                    stat_line_index = position + 6 - 1
                    print(str(stat_line_index))
                    lines = read_file.readlines()
                    stat_line_content = lines[stat_line_index]
                    data['Filepath'].append(filepath)
                    data['Stat'].append(stat_line_content)

print(data)
df = pandas.DataFrame(data)
df.to_csv(str(datetime.datetime.now()) + '.csv')