import csv
with open("C:\Users\Administrator\Documents\marks.csv.xlsx",'r')as csvfile:
  csvFile = csv.reader(csvfile)
  for lines in csvFile:
        print(lines)