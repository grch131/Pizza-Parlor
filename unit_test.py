#unit test for pizza.py

import pytest

from pizza import Pizza

def test1(pizza_size, pizza_toppings, estimated_cost):
    
    pizza = Pizza(pizza_size, pizza_toppings)
    
    assert pizza.total_cost() == estimated_cost
    
def test2(pizza_size, pizza_toppings, order):
    
    pizza = Pizza(pizza_size, pizza_toppings)
    
    assert pizza.order() == order

