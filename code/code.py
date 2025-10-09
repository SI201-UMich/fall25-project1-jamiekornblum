
import csv 

with open('data/Coffe_sales.csv', mode='r') as file: 
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
    
    # Calculate averages after collecting all data
    averages = {}
    for coffee in total:
        averages[coffee] = total[coffee] / count[coffee]
    return averages

def calculate_coffees_sold_per_type(data):
    """Calculate the number of coffees sold for each coffee type"""
    coffee_counts = {}
    for row in data:
        coffee = row['coffee_name']
        if coffee not in coffee_counts:
            coffee_counts[coffee] = 0
        coffee_counts[coffee] += 1
    return coffee_counts

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
    
    # Calculate averages AFTER collecting all data
    averages = {}
    for time in total:
        averages[time] = total[time] / count[time]
    return averages

def add_season_column(data):
    # Add a season column to the data based on month name
    def get_season(month):
        if month in ['Dec', 'Jan', 'Feb']:
            return 'Winter'
        elif month in ['Mar', 'Apr', 'May']:
            return 'Spring'
        elif month in ['Jun', 'Jul', 'Aug']:
            return 'Summer'
        elif month in ['Sep', 'Oct', 'Nov']:
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

def calculate_orders_per_season(data):
    """Calculate the number of orders per season"""
    season_counts = {}
    
    for row in data:
        season = row['Season']
        if season:  # Make sure season exists
            if season not in season_counts:
                season_counts[season] = 0
            season_counts[season] += 1  # Count each order
    
    return season_counts

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

def calculate_average_coffees_sold_per_day(data):
    """Calculate the average number of coffees sold per day"""
    daily_counts = {}
    
    # Count coffees sold each day
    for row in data:
        date = row['Date']
        
        if date not in daily_counts:
            daily_counts[date] = 0
        
        daily_counts[date] += 1  # Count each coffee sale
    
    # Calculate average
    if daily_counts:
        total_coffees = sum(daily_counts.values())
        total_days = len(daily_counts)
        average_per_day = total_coffees / total_days
        
        return {
            'average_per_day': average_per_day,
            'total_coffees': total_coffees,
            'total_days': total_days,
            'daily_counts': daily_counts
        }
    else:
        return {
            'average_per_day': 0,
            'total_coffees': 0,
            'total_days': 0,
            'daily_counts': {}
        }

def calculate_coffees_sold_per_time_of_day(data):
    """Calculate how many coffees were sold per time of day"""
    time_counts = {}
    
    for row in data:
        time_period = row['Time_of_Day']
        
        if time_period not in time_counts:
            time_counts[time_period] = 0
            
        time_counts[time_period] += 1  # Count each coffee sale
    
    return time_counts

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

def write_results_to_txt(coffee_counts, time_results, season_order_counts, highest_season_data, popular_coffee_data, daily_coffee_data, time_count_data, filename='coffee_analysis_results.txt'):
    #Write analysis results to a text file"
    with open(filename, 'w') as file:
        file.write("COFFEE SALES ANALYSIS RESULTS\n")
        
        # Coffee type results
        file.write("COFFEES SOLD PER TYPE:\n")
        for coffee, count in coffee_counts.items():
            file.write(f"{coffee}: {count} coffees sold\n")
        
        file.write("\n")
        
        # Time of day results  
        file.write("COFFEES SOLD PER TIME OF DAY:\n")
        for time, count in time_count_data.items():
            file.write(f"{time}: {count} coffees sold\n")
        
        file.write("\n")
        
        # Season results
        file.write("ORDERS PER SEASON:\n")
        for season, order_count in season_order_counts.items():
            file.write(f"{season}: {order_count} orders\n")
        
        file.write("\n")
        
        # Highest sales season
        highest_season, highest_amount, all_season_totals = highest_season_data
        file.write("SEASON WITH HIGHEST TOTAL SALES:\n")
        if highest_season:
            file.write(f"{highest_season}: ${highest_amount:.2f} total sales\n\n")
            file.write("All Season Totals:\n")
            for season, total in all_season_totals.items():
                file.write(f"  {season}: ${total:.2f}\n")
        else:
            file.write("No season data available\n")
        
        file.write("\n")
        
        # Most popular coffee per season
        file.write("MOST POPULAR COFFEE PER SEASON:\n")
        for season, data in popular_coffee_data.items():
            file.write(f" {season}: {data['coffee']} ({data['count']} orders)\n")
        file.write("\n")
        
        # Overall coffee sales analysis
        file.write("OVERALL COFFEE SALES ANALYSIS:\n")
        file.write(f"Average Coffees Sold Per Day: {daily_coffee_data['average_per_day']:.1f} coffees\n")
        file.write(f"Total Coffees Sold: {daily_coffee_data['total_coffees']} coffees\n")
        file.write(f"Total Days: {daily_coffee_data['total_days']} days\n")
    

if __name__ == "__main__":
    # Add season column to data
    data = add_season_column(data)
    
    # Calculating all results
    coffee_counts = calculate_coffees_sold_per_type(data)
    time_averages = calculate_average_sale_per_time_of_day(data)
    season_order_counts = calculate_orders_per_season(data)
    highest_season_info = get_highest_sales_season(data)
    popular_coffee_info = get_most_popular_coffee_per_season(data)
    daily_coffee_info = calculate_average_coffees_sold_per_day(data)
    time_count_info = calculate_coffees_sold_per_time_of_day(data)
    
    # Write results to txt file 
    write_results_to_txt(coffee_counts, time_averages, season_order_counts, highest_season_info, popular_coffee_info, daily_coffee_info, time_count_info)
    
 
