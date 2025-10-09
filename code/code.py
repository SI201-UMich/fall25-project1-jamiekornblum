
import csv 

with open('data/Coffe_sales.csv', mode='r') as file: 
    #opening the csv file and reading the data
    reader = csv.DictReader(file) #reading the csv file as a dictionary
    data = [row for row in reader] #making the rows into a list of dictionaries
    for row in data:
        row['money'] = float(row['money'])
        row['Time_of_Day'] = row['Time_of_Day'].strip()
        row['Month_name'] = row['Month_name'].strip()
        row['coffee_name'] = row['coffee_name'].strip()

def calculate_coffees_sold_per_type(data):
    #Counting how many coffees of each type were sold
    coffee_counts = {}
    for row in data:
        coffee = row['coffee_name']
        if coffee not in coffee_counts:
            coffee_counts[coffee] = 0
        coffee_counts[coffee] += 1
    return coffee_counts

def add_season_column(data):
    # Add a season column to the data based on month name
    def get_season(month): #adding a season key based on month
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
    
    # for each sale find its season and adding it as a new column
    for row in data:
        month = row['Month_name']
        row['Season'] = get_season(month)
    return data

def calculate_orders_per_season(data):
    season_counts = {}
    
    for row in data:
        season = row.get('Season')  
        if season:  
            if season not in season_counts:
                season_counts[season] = 0
            season_counts[season] += 1  
    
    return season_counts
    
    return season_counts

def get_most_popular_coffee_per_season(data):
    #Finds the most ordered coffee for each season.
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
    
    # Find most popular coffee for each season and stores its count
    most_popular_by_season = {}
    for season, coffee_counts in season_coffee_counts.items():
        if coffee_counts:  
            most_popular_coffee = max(coffee_counts, key=coffee_counts.get)
            order_count = coffee_counts[most_popular_coffee]
            most_popular_by_season[season] = {
                'coffee': most_popular_coffee,
                'count': order_count,
                'all_coffees': coffee_counts
            }
    
    return most_popular_by_season

def calculate_average_coffees_sold_per_day(data):
    #Calculates average daily sales
    daily_counts = {}
    
    # Count coffees sold each day
    for row in data:
        date = row['Date']
        
        if date not in daily_counts:
            daily_counts[date] = 0
        
        daily_counts[date] += 1  
    
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
    #Count how many coffees were sold per time of day
    time_counts = {}
    
    for row in data:
        time_period = row['Time_of_Day']
        
        if time_period not in time_counts:
            time_counts[time_period] = 0
            
        time_counts[time_period] += 1  
    
    return time_counts

def calculate_total_revenue(data):
    #Calculate the total revenue from all coffee sales
    total_revenue = 0
    for row in data:
        total_revenue += row['money']
    return total_revenue

def write_results_to_txt(coffee_counts, season_order_counts, popular_coffee_data, daily_coffee_data, time_count_data, total_revenue, filename='coffee_analysis_results.txt'):
    #Write analysis results to a text file"
    with open(filename, 'w') as file:
        file.write("COFFEE SALES ANALYSIS RESULTS\n")
        
        # Coffee type results with max highlighted
        file.write("COFFEES SOLD PER TYPE:\n")
        max_coffee = max(coffee_counts, key=coffee_counts.get)
        max_coffee_count = coffee_counts[max_coffee]
        for coffee, count in coffee_counts.items():
            if coffee == max_coffee:
                file.write(f"{coffee}: {count} coffees sold (MOST ORDERED)\n")
            else:
                file.write(f"{coffee}: {count} coffees sold\n")
        
        file.write("\n")
        
        # Time of day results with max highlighted
        file.write("COFFEES SOLD PER TIME OF DAY:\n")
        max_time = max(time_count_data, key=time_count_data.get)
        max_time_count = time_count_data[max_time]
        for time, count in time_count_data.items():
            if time == max_time:
                file.write(f"{time}: {count} coffees sold (PEAK TIME)\n")
            else:
                file.write(f"{time}: {count} coffees sold\n")
        
        file.write("\n")
        
        # Season results with max highlighted
        file.write("ORDERS PER SEASON:\n")
        max_season = max(season_order_counts, key=season_order_counts.get)
        max_season_count = season_order_counts[max_season]
        for season, order_count in season_order_counts.items():
            if season == max_season:
                file.write(f"{season}: {order_count} orders (MOST ORDERS)\n")
            else:
                file.write(f"{season}: {order_count} orders\n")

        file.write("\n")
        
        # Most popular coffee per season
        file.write("MOST POPULAR COFFEE PER SEASON:\n")
        for season, data in popular_coffee_data.items():
            file.write(f" {season}: {data['coffee']} ({data['count']} orders)\n")
        file.write("\n")
        
        # Final coffee sales analysis
        file.write("FINAL COFFEE SALES ANALYSIS:\n")
        file.write(f"Average Coffees Sold Per Day: {daily_coffee_data['average_per_day']:.1f} coffees\n")
        file.write(f"Total Coffees Sold: {daily_coffee_data['total_coffees']} coffees\n")
        file.write(f"Total Days: {daily_coffee_data['total_days']} days\n")
        file.write(f"Total Revenue: ${total_revenue:.2f}\n")
    

if __name__ == "__main__":
    # Add season column to data
    data = add_season_column(data)
    
    # Calculating all results
    coffee_counts = calculate_coffees_sold_per_type(data)
    season_order_counts = calculate_orders_per_season(data)
    popular_coffee_info = get_most_popular_coffee_per_season(data)
    daily_coffee_info = calculate_average_coffees_sold_per_day(data)
    time_count_info = calculate_coffees_sold_per_time_of_day(data)
    total_revenue = calculate_total_revenue(data)
    
    # Write results to txt file 
    write_results_to_txt(coffee_counts, season_order_counts, popular_coffee_info, daily_coffee_info, time_count_info, total_revenue)
    
 
