#unit test for pizza.py

import pytest

from pizza import Pizza

#Diamond

def test1(pizza_size, pizza_toppings, estimated_cost):
    
    """Test for the total_cost function"""
    
    pizza = Pizza(pizza_size, pizza_toppings)
    
    assert pizza.total_cost() == estimated_cost
    
def test2(pizza_size, pizza_toppings, order):
    
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

