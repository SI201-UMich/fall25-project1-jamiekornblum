
import unittest
from code import *

class TestCoffeeSalesCalculations(unittest.TestCase):
    
    def setUp(self):
        #Created a sample dataset with NA/null values for testing
        self.sample_data = [
            {'hour_of_day': '10', 'cash_type': 'card', 'money': 38.7, 'coffee_name': 'Latte', 'Time_of_Day': 'Morning', 'Weekday': 'Fri', 'Month_name': 'Mar', 'Date': '2024-03-01', 'Season': 'Spring'},
            {'hour_of_day': '12', 'cash_type': 'card', 'money': 38.7, 'coffee_name': 'Hot Chocolate', 'Time_of_Day': 'Afternoon', 'Weekday': 'Fri', 'Month_name': 'Mar', 'Date': '2024-03-01', 'Season': 'Spring'},
            {'hour_of_day': '13', 'cash_type': 'card', 'money': 28.9, 'coffee_name': 'Americano', 'Time_of_Day': 'Afternoon', 'Weekday': 'Fri', 'Month_name': 'Mar', 'Date': '2024-03-01', 'Season': 'Spring'},
            {'hour_of_day': '15', 'cash_type': 'card', 'money': 33.8, 'coffee_name': 'Americano with Milk', 'Time_of_Day': 'Afternoon', 'Weekday': 'Fri', 'Month_name': 'Mar', 'Date': '2024-03-01', 'Season': 'Spring'},
            {'hour_of_day': '18', 'cash_type': 'card', 'money': 33.8, 'coffee_name': 'Americano with Milk', 'Time_of_Day': 'Night', 'Weekday': 'Fri', 'Month_name': 'Mar', 'Date': '2024-03-01', 'Season': 'Spring'},
            {'hour_of_day': '19', 'cash_type': 'card', 'money': 38.7, 'coffee_name': 'Cocoa', 'Time_of_Day': 'Night', 'Weekday': 'Fri', 'Month_name': 'Mar', 'Date': '2024-03-01', 'Season': 'Spring'},
            # Data with NA/null values for edge case testing
            {'hour_of_day': '14', 'cash_type': 'cash', 'money': 25.5, 'coffee_name': '', 'Time_of_Day': 'Afternoon', 'Weekday': 'Mon', 'Month_name': 'Jan', 'Date': '2024-01-15', 'Season': 'Winter'},
            {'hour_of_day': '9', 'cash_type': 'card', 'money': 30.0, 'coffee_name': 'Latte', 'Time_of_Day': '', 'Weekday': 'Tue', 'Month_name': 'Jan', 'Date': '2024-01-16', 'Season': 'Winter'},
            {'hour_of_day': '11', 'cash_type': 'card', 'money': 0.0, 'coffee_name': 'Espresso', 'Time_of_Day': 'Morning', 'Weekday': 'Wed', 'Month_name': '', 'Date': '2024-01-17', 'Season': ''},
            {'hour_of_day': '', 'cash_type': 'cash', 'money': 35.2, 'coffee_name': 'Cappuccino', 'Time_of_Day': 'Morning', 'Weekday': 'Thu', 'Month_name': 'Dec', 'Date': '', 'Season': 'Winter'},
        ]
    
    def test_calculate_coffees_sold_per_type_general_1(self):
        #Test 1: General case - regular data with various coffee types
        result = calculate_coffees_sold_per_type(self.sample_data)
        # Sample data contains: Latte (2), Hot Chocolate (1), Americano (1), Americano with Milk (2), Cocoa (1), Espresso (1), Cappuccino (1)
        self.assertGreater(len(result), 0)
        self.assertIn('Latte', result)
        self.assertEqual(result['Latte'], 2)

    def test_calculate_coffees_sold_per_type_general_2(self):
        #Test 2: General case - subset of data  
        subset_data = self.sample_data[:4]  # First 4 items
        result = calculate_coffees_sold_per_type(subset_data)
        expected = {'Latte': 1, 'Hot Chocolate': 1, 'Americano': 1, 'Americano with Milk': 1}
        self.assertEqual(result, expected)

    def test_calculate_coffees_sold_per_type_edge_1(self):
        #Test 3: Edge case with empty data
        result = calculate_coffees_sold_per_type([])
        expected = {}
        self.assertEqual(result, expected)

    def test_calculate_coffees_sold_per_type_edge_2(self):
        #Test 4: Edge case - Data with empty coffee names (filtering NA values)
        data_with_empty = [item for item in self.sample_data if item['coffee_name'] == '']
        result = calculate_coffees_sold_per_type(data_with_empty)
        expected = {'': 1}  # The function counts empty strings as a valid coffee type
        self.assertEqual(result, expected)


    def test_add_season_column_general_1(self):
        #Test 1: General case - using sample data subset
        data = [item for item in self.sample_data if item['Month_name'] in ['Mar', 'Jan', 'Dec']]
        result = add_season_column(data)
        # March = Spring, Jan = Winter, Dec = Winter
        seasons = [r['Season'] for r in result]
        self.assertIn('Spring', seasons)
        self.assertIn('Winter', seasons)

    def test_add_season_column_general_2(self):
        #Test 2: General case - specific month check
        march_data = [item for item in self.sample_data if item['Month_name'] == 'Mar']
        result = add_season_column(march_data)
        for item in result:
            self.assertEqual(item['Season'], 'Spring')

    def test_add_season_column_edge_1(self):
        #Test 3: Edge case with empty month name
        data = [item for item in self.sample_data if item['Month_name'] == '']
        result = add_season_column(data)
        for item in result:
            self.assertEqual(item['Season'], 'Unknown')

    def test_add_season_column_edge_2(self):
        #Test 4: Edge case with empty data
        result = add_season_column([])
        self.assertEqual(result, [])

    def test_calculate_orders_per_season_general_1(self):
        #Test 1: General case - using sample data with seasons
        result = calculate_orders_per_season(self.sample_data)
        # Sample data has Spring and Winter seasons
        self.assertIn('Spring', result)
        self.assertIn('Winter', result)
        self.assertGreater(result['Spring'], 0)
        self.assertGreater(result['Winter'], 0)

    def test_calculate_orders_per_season_general_2(self):
        #Test 2: General case - subset with single season
        spring_data = [item for item in self.sample_data if item['Season'] == 'Spring']
        result = calculate_orders_per_season(spring_data)
        expected = {'Spring': len(spring_data)}
        self.assertEqual(result, expected)

    def test_calculate_orders_per_season_edge_1(self):
        #Test 3: Edge case with empty season values
        data_with_empty_season = [item for item in self.sample_data if item['Season'] == '']
        result = calculate_orders_per_season(data_with_empty_season)
        self.assertLessEqual(len(result), 1)  # May have empty string as key or be empty

    def test_calculate_orders_per_season_edge_2(self):
        #Test 4: Edge case with empty data
        result = calculate_orders_per_season([])
        expected = {}
        self.assertEqual(result, expected)


    def test_get_most_popular_coffee_per_season_general_1(self):
        #Test 1: General case - using sample data
        result = get_most_popular_coffee_per_season(self.sample_data)
        # Should have results for Spring and Winter seasons
        self.assertIn('Spring', result)
        self.assertIn('Winter', result)
        self.assertIn('coffee', result['Spring'])
        self.assertIn('count', result['Spring'])

    def test_get_most_popular_coffee_per_season_general_2(self):
        #Test 2: General case - subset with known result
        winter_data = [item for item in self.sample_data if item['Season'] == 'Winter']
        result = get_most_popular_coffee_per_season(winter_data)
        if 'Winter' in result:
            self.assertGreater(result['Winter']['count'], 0)

    def test_get_most_popular_coffee_per_season_edge_1(self):
        #Test 3: Edge case - empty data
        result = get_most_popular_coffee_per_season([])
        self.assertEqual(result, {})

    def test_get_most_popular_coffee_per_season_edge_2(self):
        #Test 4: Edge case - data with empty coffee names
        data_with_empty = [item for item in self.sample_data if item['coffee_name'] == '']
        result = get_most_popular_coffee_per_season(data_with_empty)
        # Should handle empty coffee names gracefully
        self.assertIsInstance(result, dict)


    def test_calculate_average_coffees_sold_per_day_general_1(self):
        #Test 1: General case - using sample data
        result = calculate_average_coffees_sold_per_day(self.sample_data)
        self.assertIn('average_per_day', result)
        self.assertIn('total_days', result)
        self.assertGreater(result['average_per_day'], 0)
        self.assertGreater(result['total_days'], 0)

    def test_calculate_average_coffees_sold_per_day_general_2(self):
        #Test 2: General case - subset of data
        subset_data = self.sample_data[:3]  # First 3 items
        result = calculate_average_coffees_sold_per_day(subset_data)
        self.assertGreaterEqual(result['average_per_day'], 0)

    def test_calculate_average_coffees_sold_per_day_edge_1(self):
        #Test 3: Edge case - single date
        single_date_data = [item for item in self.sample_data if item['Date'] == '2024-03-01']
        result = calculate_average_coffees_sold_per_day(single_date_data)
        if result['total_days'] > 0:
            self.assertEqual(result['average_per_day'], len(single_date_data))

    def test_calculate_average_coffees_sold_per_day_edge_2(self):
        #Test 4: Edge case - empty data
        result = calculate_average_coffees_sold_per_day([])
        self.assertEqual(result['average_per_day'], 0)


    def test_calculate_coffees_sold_per_time_of_day_general_1(self):
        #Test 1: General case - using sample data
        result = calculate_coffees_sold_per_time_of_day(self.sample_data)
        # Sample data has Morning, Afternoon, and Night times
        self.assertIn('Morning', result)
        self.assertIn('Afternoon', result)
        self.assertIn('Night', result)
        self.assertGreater(result['Morning'], 0)

    def test_calculate_coffees_sold_per_time_of_day_general_2(self):
        #Test 2: General case - subset of data
        morning_data = [item for item in self.sample_data if item['Time_of_Day'] == 'Morning']
        result = calculate_coffees_sold_per_time_of_day(morning_data)
        expected = {'Morning': len(morning_data)}
        self.assertEqual(result, expected)

    def test_calculate_coffees_sold_per_time_of_day_edge_1(self):
        #Test 3: Edge case - data with empty Time_of_Day
        data_with_empty = [item for item in self.sample_data if item['Time_of_Day'] == '']
        result = calculate_coffees_sold_per_time_of_day(data_with_empty)
        if len(data_with_empty) > 0:
            self.assertIn('', result)

    def test_calculate_coffees_sold_per_time_of_day_edge_2(self):
        #Test 4: Edge case - empty data
        result = calculate_coffees_sold_per_time_of_day([])
        self.assertEqual(result, {})

    def test_calculate_total_revenue_general_1(self):
        #Test 1: General case - using sample data
        result = calculate_total_revenue(self.sample_data)
        # Sample data has various money values
        self.assertGreater(result, 0)
        # Sum should be reasonable based on sample data values
        self.assertIsInstance(result, (int, float))

    def test_calculate_total_revenue_general_2(self):
        #Test 2: General case - subset of data
        subset_data = self.sample_data[:3]  # First 3 items
        result = calculate_total_revenue(subset_data)
        expected_sum = sum(float(item['money']) for item in subset_data)
        self.assertAlmostEqual(result, expected_sum, places=2)

    def test_calculate_total_revenue_edge_1(self):
        #Test 3: Edge case - data with zero money
        zero_money_data = [item for item in self.sample_data if float(item['money']) == 0.0]
        result = calculate_total_revenue(zero_money_data)
        self.assertEqual(result, 0.0)

    def test_calculate_total_revenue_edge_2(self):
        #Test 4: Edge case - empty data
        result = calculate_total_revenue([])
        self.assertEqual(result, 0)

    def test_calculate_total_revenue_edge_2(self):
        #Test 4: Edge case - empty data
        result = calculate_total_revenue([])
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()