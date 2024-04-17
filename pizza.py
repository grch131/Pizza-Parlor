#class Pizza

'''This class will have the pizza size, toppings, and the cost of them'''

#def init
    #self.size of the pizza
    #self.toppings for the pizza
class Pizza:
     
    def __init__(self, pizza_size, pizza_toppings ):
        
        self.pizza_size = pizza_size
        
        self.pizza_toppings = pizza_toppings
    
    #def total_cost
        #there will be a base cost for the pizza (around 9.99)
        #toppings_cost (about 1.00 or 1.50 for each topping)
        
    def total_cost(self):
        
        base_cost = 9.99
        
        toppings_cost = len(self.pizza_toppings) * 1.00
        
        total = base_cost + toppings_cost
        
        if self.pizza_size.lower == 'medium':
            
            total += 2
            
        elif self.pizza_size.lower == 'large':
            
            total += 4
            
        return total
            
        
    #def order
        #a string that will return the order of the customer
    
    def order(self):
        
        return f'You want a {self.pizza_size} pizza with {",".join(self.pizza_toppings)} toppings!'
        
        
    
#unit test

#def topping_price():
    
    #pizza_topping = 1.50
    
    #assert pizza_topping(4) == 6
    
#class Order:
'''Represents an order of a pizza with the size and toppings'''

#def take_order(self):
'''This function will generate a random pizza order with size and toppings

Returns:
    order(str): A string containing the randomly generated pizza order
'''



#class Cost:
''' This class will calculate the total cost of the pizza with the toppings calculated
into it. This class will also calculate the total profit created, from adding all the
pizzas sold together. '''

#def total_cost_w_toppings():
'''Function used to calculate the total cost of the specific pizza selected with all the 
toppings calculated in it'''

#def profit():
''' This function will calculate the total profit from all the pizzas sold '''

# def test_total_cost_w_toppings(self):
'''This is the unit test for the total_cost of one pizza function'''
    # self.assertEqual(total_cost([This would contain the prices of the pizzas]))

#def test_profit(self):
'''This would be the unit test for the total profit of all pizzas together'''
    #self.assertEqual(profit([This would calculate the total price of all the pizzas together]))

#def main():
'''The main function of the pizza parlor simulation. This function provides options for taking orders, 
viewing orders, and exiting the pizza parlor simulation.'''


#if __name__ == '__main__':
    #pytest.main()
