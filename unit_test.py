#unit test for pizza.py

import pytest

from pizza import Pizza

def test1(pizza_size, pizza_toppings, estimated_cost):
    
    pizza = Pizza(pizza_size, pizza_toppings)
    
    assert pizza.total_cost() == estimated_cost
    
def test2(pizza_size, pizza_toppings, order):
    
    pizza = Pizza(pizza_size, pizza_toppings)
    
    assert pizza.order() == order

def test_total_cost_w_toppings(self):
    """This is the test for the total_cost of one pizza function"""
    
    cost_instance = Cost(toppings_cost = 1)
    
    assert cost_instance.total_cost_w_toppings(3) == 12.99

def test_profit(self):
    """This is the test for the total profit of all pizzas together"""
    cost_instance = Cost(toppings_cost= 1)

    assert cost_instance.profit(num_sales=100, num_toppings= 3) == 899.0

from pizza import take_order

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
