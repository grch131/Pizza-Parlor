#unit test for pizza.py

import pytest

from pizza import Pizza

#Diamond

def test_total_cost(pizza_size, pizza_toppings, estimated_cost):
    
    """Test for the total_cost function"""
    
    pizza = Pizza(pizza_size, pizza_toppings)
    
    assert pizza.total_cost() == estimated_cost
    
def test_order(pizza_size, pizza_toppings, order):
    
    """Test for the order function"""
    
    pizza = Pizza(pizza_size, pizza_toppings)
    
    assert pizza.order() == order
    
#Grace

def test_total_cost_w_toppings(self):
    """This is the test for the total_cost of one pizza function"""
    
    cost_instance = Cost(toppings_cost = 1)
    
    assert cost_instance.total_cost_w_toppings(3) == 12.99

def test_profit(self):
    """This is the test for the total profit of all pizzas together"""
    cost_instance = Cost(toppings_cost= 1)

    assert cost_instance.profit(num_sales=100, num_toppings= 3) == 899.0

from pizza import take_order

#Jason

def test_take_order():
    """Unit test for the take_order function in pizza.py"""
    order_details, total_cost = take_order()

    assert isinstance(order_details, str)

    assert isinstance(total_cost, float)

    assert 'small' in order_details or 'medium' in order_details or 'large' in order_details
    assert 'pepperoni' in order_details or 'mushrooms' in order_details or 'onions' in order_details or 'sausage' in order_details or 'bacon' in order_details or 'olives' in order_details

#display_order test
"""Open the Python script containing the display_order function.
Call the display_order function with a set of parameters, such as display_order('medium pizza with mushrooms, onions', 6.00).
Check the console output."""

#Daniel
import unittest

from unittest.mock import patch

from io import StringIO

from your_module_name import main

from pizza import main

class TestPizzaParlor(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', 'small', 'pepperoni', '2', '3', '4'])
    def test_main_function(self, mock_input):
        """Test the main function of the Pizza Parlor simulation."""

        with patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            output = fake_output.getvalue()
        
        expected_output = "Welcome to Pizza Parlor!\nOrder placed!\n\nCurrent Orders:\n1. You want a small pizza with pepperoni toppings! - Total Cost: $10.99\nTotal Profit: $7.00\nThank you for visiting our Pizza Parlor!\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
