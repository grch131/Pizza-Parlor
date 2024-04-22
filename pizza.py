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



class Cost:
    def __init__(self, toppings_cost):
        self.base_cost = 9.99 
        self.toppings_cost = toppings_cost
        
    def total_cost_w_toppings(self, num_toppings):
        """This function will be used to calculate the total cost of the specific pizza 
        selected with all the toppings calculated in it

        Args:
            num_toppings (_type_): _description_

        Returns:
            total_cost: _description_
        """
        total_cost = self.base_cost + (num_toppings * self.toppings_cost)
        return total_cost
        
    def profit(self, num_sales, num_toppings):
        """This function will calculate the total profit from all the pizzas sold

        Args:
            num_sales (_type_): _description_
            num_toppings (_type_): _description_

        Returns:
            _type_: _description_
        """
        total_sales = num_sales * self.total_cost_w_toppings(num_toppings)
        total_cost = num_sales * self.base_cost
        profit = total_sales - total_cost
        return profit 

"""unit test"""
    def test_total_cost_w_toppings(self):
        """This is the unit test for the total_cost of one pizza function"""
        cost_instance = Cost(toppings_cost = 1)
        assert cost_instance.total_cost_w_toppings(3) == 13
        
    def test_profit(self):
        """This would be the unit test for the total profit of all pizzas together"""
        cost_instance = Cost(toppings_cost= 1)
        assert cost_instance.profit(num_sales=100, num_toppings= 3) == 1100.0
        
if __name__ == '__main__':
   pytest.main()


#def main():
'''The main function of the pizza parlor simulation. This function provides options for taking orders, 
viewing orders, and exiting the pizza parlor simulation.'''


#if __name__ == '__main__':
    #pytest.main()
