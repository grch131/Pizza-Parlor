#unit test for pizza.py

import pytest
from io import StringIO
import sys

import unit_test

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

from pizza import Cost

def test_total_cost_w_toppings():
    
    """This is the test for the total_cost of one pizza function"""
    
    cost_instance = Cost(toppings_cost = 1.00)
    
    assert cost_instance.total_cost_w_toppings(3) == 12.99

def test_profit():
    
    """This is the test for the total profit of all pizzas together"""
    
    cost_instance = Cost(toppings_cost= 1.00)

    assert cost_instance.profit(num_sales=100, num_toppings= 3) == 799.0

#Jason

from pizza import display_order

def test_display_order():

    stdout = sys.stdout

    sys.stdout = StringIO()

    display_order("Pizza Size: Large with Toppings: Pepperoni, Olives", 16.99)

    output = sys.stdout.getvalue()

    sys.stdout = stdout

    assert "Order Details:" in output

    assert "Pizza Size: Large" in output

    assert "Toppings: Pepperoni, Olives" in output
    
    assert "Total Cost: 16.99" in output


#Daniel

import unittest

from unittest.mock import patch

from io import StringIO

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
