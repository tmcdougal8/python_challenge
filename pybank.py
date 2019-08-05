import csv
import os

csvpath = "budget_data.csv"

with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)


        months = 0
        RevDiffTotal=0
        lastRevenue=0
        currentRevenue=0
        RevDiff=0
        MaxRevChange=0
        MinRevChange=0
        TotalRevenue=0

        for row in csvreader:
            
            
            months=months+1
            TotalRevenue=float(TotalRevenue)+float(row[1])
            currentRevenue=row[1]
            RevDiff=float(currentRevenue)-float(lastRevenue)
            RevDiffTotal=RevDiffTotal+RevDiff
            lastRevenue=row[1]

            if RevDiff>MaxRevChange:
                MaxRevChange=RevDiff
                MaxRevMonth=row[0]
            if RevDiff<MinRevChange:
                MinRevChange=RevDiff
                MinRevMonth=row[0]

        AvgRevChange = RevDiffTotal/months

        print()
        print()
        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {months}")
        print(f"Total Revenue: ${round(TotalRevenue,2)}")
        print(f"Average Revenue Change: ${round(AvgRevChange,2)}")
        print(f"Greatest Increase in Revenue: {MaxRevMonth} ${round(MaxRevChange,2)}")
        print(f"Greatest Decrease in Revenue: {MinRevMonth} ${round(MinRevChange,2)}")
        print()