
import csv 

with open('coffee_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
    for row in data:
        row['money'] = float(row['money'])
        row['Time_of_Day'] = row['Time_of_Day'].strip()
        row['Month_name'] = row['Month_name'].strip()
        row['coffee_name'] = row['coffee_name'].strip()

def calculate_average_sale_per_coffee_type(data):
    #Calculate average sale amount for each coffee type
    count = {} 
    total = {}
    for row in data:
        coffee = row['coffee_name']
        money = row['money']
        if coffee not in count:
            count[coffee] = 0
            total[coffee] = 0
        count[coffee] += 1
        total[coffee] += money
        for coffee in total:
            total[coffee] /= count[coffee]
    return total

def calculate_average_sale_per_time_of_day(data):
    #Calculate average sale amount for each time period
    pass

def calculate_average_sale_per_season(data):
    #Calculate average sale amount for each season
    pass
