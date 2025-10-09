
import unittest
import csv

class TestCoffeeSalesCalculations(unittest.TestCase):
    
    def setUp(self):
        self.full_data = []
        
        with open('Coffe_sales.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                row['money'] = float(row['money'])
                self.full_data.append(row)
        
        # Test data subsets
        self.sample_data = self.full_data[:10]
        self.empty_data = []

    def test_average_per_coffee_type_general_case(self):
        # Calculate expected results manually from sample data
        coffee_totals = {}
        coffee_counts = {}
        
        for row in self.sample_data:
            coffee_name = row['coffee_name']
            price = row['money']
            
            if coffee_name not in coffee_totals:
                coffee_totals[coffee_name] = 0
                coffee_counts[coffee_name] = 0
            
            coffee_totals[coffee_name] += price
            coffee_counts[coffee_name] += 1
        
        expected = {coffee: coffee_totals[coffee] / coffee_counts[coffee] 
                   for coffee in coffee_totals}
        
        # Test the function (uncomment when you implement it)
        # result = calculate_average_sale_per_coffee_type(self.sample_data)
        # self.assertEqual(result, expected)
        
        

    def test_average_per_coffee_type_edge_case(self):
        """Test 2: Average sale per coffee type with empty data"""
        
        expected = {}
    
        # Test the function (uncomment when you implement it)
        # result = calculate_average_sale_per_coffee_type(self.empty_data)
        # self.assertEqual(result, expected)

        
    def test_average_per_time_of_day_general_case(self):
        time_totals = {}
        time_counts = {}
        
        for row in self.sample_data:
            time_period = row['Time_of_Day']
            price = row['money']
            
            if time_period not in time_totals:
                time_totals[time_period] = 0
                time_counts[time_period] = 0
            
            time_totals[time_period] += price
            time_counts[time_period] += 1
        
        expected = {time: time_totals[time] / time_counts[time] 
                   for time in time_totals}
        
        # result = calculate_average_sale_per_time_of_day(self.sample_data)
        # self.assertEqual(result, expected)
        

    def test_average_per_season_general_case(self):
        def get_season(month_name):
            month_to_season = {
                'Mar': 'Spring', 'Apr': 'Spring', 'May': 'Spring',
                'Jun': 'Summer', 'Jul': 'Summer', 'Aug': 'Summer', 
                'Sep': 'Fall', 'Oct': 'Fall', 'Nov': 'Fall',
                'Dec': 'Winter', 'Jan': 'Winter', 'Feb': 'Winter'
            }
            return month_to_season.get(month_name, 'Unknown')
        
        season_totals = {}
        season_counts = {}
        
        for row in self.sample_data:
            season = get_season(row['Month_name'])
            price = row['money']
            
            if season not in season_totals:
                season_totals[season] = 0
                season_counts[season] = 0
            
            season_totals[season] += price
            season_counts[season] += 1
        
        expected = {season: season_totals[season] / season_counts[season] 
                   for season in season_totals}
        
        # Test the function (uncomment when you implement it)
        # result = calculate_average_sale_per_season(self.sample_data)
        # self.assertEqual(result, expected)
        
      

if __name__ == '__main__':
    # Run the tests to show expected values
    test_instance = TestCoffeeSalesCalculations()
    test_instance.setUp()

    test_instance.test_average_per_coffee_type_general_case()
    print()
    test_instance.test_average_per_coffee_type_edge_case()
    print()
    test_instance.test_average_per_time_of_day_general_case()
    print()
    test_instance.test_average_per_season_general_case()
    