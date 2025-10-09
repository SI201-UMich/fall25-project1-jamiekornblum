
import unittest
from code import *

class TestCoffeeSalesCalculations(unittest.TestCase):
    
    def test_calculate_coffees_sold_per_type_general_1(self):
        #Test 1: General case 
        data = [{'coffee_name': 'Latte'}, {'coffee_name': 'Latte'}, {'coffee_name': 'Espresso'}]
        result = calculate_coffees_sold_per_type(data)
        expected = {'Latte': 2, 'Espresso': 1}
        self.assertEqual(result, expected)

    def test_calculate_coffees_sold_per_type_general_2(self):
        #Test 2: General case 
        data = [{'coffee_name': 'Mocha'}, {'coffee_name': 'Mocha'}, {'coffee_name': 'Cappuccino'}]
        result = calculate_coffees_sold_per_type(data)
        expected = {'Mocha': 2, 'Cappuccino': 1}
        self.assertEqual(result, expected)

    def test_calculate_coffees_sold_per_type_edge_1(self):
        #Test 3: Edge case with empty data
        result = calculate_coffees_sold_per_type([])
        expected = {}
        self.assertEqual(result, expected)

    def test_calculate_coffees_sold_per_type_edge_2(self):
        #Test 4: Edge case with whitespace 
        data = [{'coffee_name': ' Latte '}, {'coffee_name': 'Latte'}]
        cleaned_data = [{'coffee_name': row['coffee_name'].strip()} for row in data]
        result = calculate_coffees_sold_per_type(cleaned_data)
        expected = {'Latte': 2}
        self.assertEqual(result, expected)


    def test_add_season_column_general_1(self):
        #Test 1: General case 
        data = [{'Month_name': 'Jan'}, {'Month_name': 'Apr'}, {'Month_name': 'Aug'}, {'Month_name': 'Oct'}]
        result = add_season_column(data)
        expected = ['Winter', 'Spring', 'Summer', 'Fall']
        actual = [r['Season'] for r in result]
        self.assertEqual(actual, expected)

    def test_add_season_column_general_2(self):
        #Test 2: General case 
        data = [{'Month_name': 'Feb'}, {'Month_name': 'May'}]
        result = add_season_column(data)
        self.assertEqual(result[0]['Season'], 'Winter')
        self.assertEqual(result[1]['Season'], 'Spring')

    def test_add_season_column_edge_1(self):
        #Test 3: Edge case with unknown month
        data = [{'Month_name': 'XYZ'}]
        result = add_season_column(data)
        self.assertEqual(result[0]['Season'], 'Unknown')

    def test_add_season_column_edge_2(self):
        #Test 4: Edge case with empty data
        data = []
        result = add_season_column(data)
        self.assertEqual(result, [])

    def test_calculate_orders_per_season_general_1(self):
        #Test 1: General case with multiple seasons
        data = [{'Season': 'Winter'}, {'Season': 'Winter'}, {'Season': 'Summer'}]
        result = calculate_orders_per_season(data)
        expected = {'Winter': 2, 'Summer': 1}
        self.assertEqual(result, expected)

    def test_calculate_orders_per_season_general_2(self):
        #Test 2: General case with single season``
        data = [{'Season': 'Fall'}, {'Season': 'Fall'}, {'Season': 'Fall'}]
        result = calculate_orders_per_season(data)
        expected = {'Fall': 3}
        self.assertEqual(result, expected)

    def test_calculate_orders_per_season_edge_1(self):
        #Test 3: Edge case with missing Season key
        data = [{}]
        result = calculate_orders_per_season(data)
        expected = {}
        self.assertEqual(result, expected)

    def test_calculate_orders_per_season_edge_2(self):
        #Test 4: Edge case with empty data
        data = []
        result = calculate_orders_per_season(data)
        expected = {}
        self.assertEqual(result, expected)


def test_get_most_popular_coffee_per_season():
    # General tests
    data = [
        {'Season': 'Winter', 'coffee_name': 'Latte'},
        {'Season': 'Winter', 'coffee_name': 'Espresso'},
        {'Season': 'Winter', 'coffee_name': 'Latte'},
    ]
    result = get_most_popular_coffee_per_season(data)
    assert result['Winter']['coffee'] == 'Latte'
    assert result['Winter']['count'] == 2

    data = [
        {'Season': 'Summer', 'coffee_name': 'Mocha'},
        {'Season': 'Summer', 'coffee_name': 'Mocha'},
        {'Season': 'Summer', 'coffee_name': 'Latte'},
    ]
    assert get_most_popular_coffee_per_season(data)['Summer']['coffee'] == 'Mocha'

    # Edge cases
    data = []  
    assert get_most_popular_coffee_per_season(data) == {}

    data = [{'Season': 'Winter', 'coffee_name': ''}]  
    result = get_most_popular_coffee_per_season(data)
    assert 'Winter' in result


def test_calculate_average_coffees_sold_per_day():
    # General tests
    data = [{'Date': '2024-01-01'}, {'Date': '2024-01-01'}, {'Date': '2024-01-02'}]
    result = calculate_average_coffees_sold_per_day(data)
    assert result['average_per_day'] == 1.5  
    assert result['total_days'] == 2

    data = [{'Date': '2024-01-01'}, {'Date': '2024-01-02'}, {'Date': '2024-01-03'}]
    result = calculate_average_coffees_sold_per_day(data)
    assert result['average_per_day'] == 1.0

    # Edge cases
    data = [{'Date': '2024-01-01'}]
    assert calculate_average_coffees_sold_per_day(data)['average_per_day'] == 1

    assert calculate_average_coffees_sold_per_day([])['average_per_day'] == 0


def test_calculate_coffees_sold_per_time_of_day():
    # General tests
    data = [{'Time_of_Day': 'Morning'}, {'Time_of_Day': 'Evening'}, {'Time_of_Day': 'Morning'}]
    assert calculate_coffees_sold_per_time_of_day(data) == {'Morning': 2, 'Evening': 1}

    data = [{'Time_of_Day': 'Afternoon'}, {'Time_of_Day': 'Afternoon'}]
    assert calculate_coffees_sold_per_time_of_day(data) == {'Afternoon': 2}

    # Edge cases
    data = [{'Time_of_Day': ''}]
    assert calculate_coffees_sold_per_time_of_day(data) == {'': 1}

    assert calculate_coffees_sold_per_time_of_day([]) == {}


def test_calculate_total_revenue():
    # General tests
    data = [{'money': 2.5}, {'money': 3.5}]
    assert calculate_total_revenue(data) == 6.0

    data = [{'money': 0}, {'money': 10}]
    assert calculate_total_revenue(data) == 10

    def test_calculate_total_revenue_edge_1(self):
        #Test 3: Edge case with empty data
        data = []
        result = calculate_total_revenue(data)
        expected = 0
        self.assertEqual(result, expected)

    def test_calculate_total_revenue_edge_2(self):
        #Test 4: Edge case with negative value
        data = [{'money': -5}]
        result = calculate_total_revenue(data)
        expected = -5
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()