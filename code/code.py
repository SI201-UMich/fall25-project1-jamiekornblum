
import csv 

with open('coffee_data.csv', mode='r') as file: 
    #reading the data
    reader = csv.DictReader(file)
    data = [row for row in reader]
    for row in data:
        row['money'] = float(row['money'])
        row['Time_of_Day'] = row['Time_of_Day'].strip()
        row['Month_name'] = row['Month_name'].strip()
        row['coffee_name'] = row['coffee_name'].strip()

def calculate_average_sale_per_coffee_type(data):
    #Calculating average sale amount for each coffee type
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
    #Calculating average sale amount for each time period
    count = {}
    total = {}
    for row in data:
        time = row['Time_of_Day']
        money = row['money']
        if time not in count:
            count[time] = 0
            total[time] = 0
        count[time] += 1
        total[time] += money
        for time in total:
            total[time] /= count[time]
    return total

def add_season_column(data):
    # Add a season column to the data based on month name
    def get_season(month):
        if month in ['December', 'January', 'February']:
            return 'Winter'
        elif month in ['March', 'April', 'May']:
            return 'Spring'
        elif month in ['June', 'July', 'August']:
            return 'Summer'
        elif month in ['September', 'October', 'November']:
            return 'Fall'
        else:
            return 'Unknown'
    
    # Add season column to each row
    for row in data:
        month = row['Month_name']
        row['Season'] = get_season(month)
    return data

def calculate_average_sale_per_season(data):
    #Calculating average sale amount for each season using the Season column
    season_count = {}
    season_total = {}
    for row in data:
        season = row['Season']  # Use the new Season column directly
        money = row['money']
        if season:  # Make sure season exists
            if season not in season_count:
                season_count[season] = 0
                season_total[season] = 0
            season_count[season] += 1
            season_total[season] += money
    for season in season_total:
        season_total[season] /= season_count[season]
    return season_total

def get_highest_sales_season(data):
    #Find which season has the highest total sales
    season_totals = {}
    
    # Calculate total sales for each season
    for row in data:
        season = row['Season']
        money = row['money']
        if season:
            if season not in season_totals:
                season_totals[season] = 0
            season_totals[season] += money
    
    # Find the season with highest total sales
    if season_totals:
        highest_season = max(season_totals, key=season_totals.get)
        highest_amount = season_totals[highest_season]
        return highest_season, highest_amount, season_totals
    else:
        return None, 0, {}

def get_most_popular_coffee_per_season(data):
    #Find which coffee is ordered the most during each season"
    season_coffee_counts = {}
    
    # Count coffee orders for each season
    for row in data:
        season = row['Season']
        coffee = row['coffee_name']
        
        if season:
            if season not in season_coffee_counts:
                season_coffee_counts[season] = {}
            
            if coffee not in season_coffee_counts[season]:
                season_coffee_counts[season][coffee] = 0
                
            season_coffee_counts[season][coffee] += 1
    
    # Find most popular coffee for each season
    most_popular_by_season = {}
    for season, coffee_counts in season_coffee_counts.items():
        if coffee_counts:  # Make sure there are coffees for this season
            most_popular_coffee = max(coffee_counts, key=coffee_counts.get)
            order_count = coffee_counts[most_popular_coffee]
            most_popular_by_season[season] = {
                'coffee': most_popular_coffee,
                'count': order_count,
                'all_coffees': coffee_counts
            }
    
    return most_popular_by_season

def calculate_average_revenue_per_day(data):
    #Calculate the average total revenue per day
    daily_revenues = {}
    
    # Sum up revenue for each day
    for row in data:
        date = row['Date']  # Assuming there's a Date column
        money = row['money']
        
        if date not in daily_revenues:
            daily_revenues[date] = 0
        
        daily_revenues[date] += money
    
    # Calculate average revenue per day
    if daily_revenues:
        total_revenue = sum(daily_revenues.values())
        total_days = len(daily_revenues)
        average_revenue_per_day = total_revenue / total_days
        
        return {
            'average_per_day': average_revenue_per_day,
            'total_revenue': total_revenue,
            'total_days': total_days,
            'daily_revenues': daily_revenues
        }
    else:
        return {
            'average_per_day': 0,
            'total_revenue': 0,
            'total_days': 0,
            'daily_revenues': {}
        }

