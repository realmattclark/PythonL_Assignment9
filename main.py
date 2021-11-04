import csv
read_in_file('CrimeDataVS.csv')
file_csv = cvs.reader(file)

for line in file_csv:
    print(type(line))
    print(len(line))
    print(line[0])
    print(line)
