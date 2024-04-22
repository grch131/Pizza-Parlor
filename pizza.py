import random

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

def take_order():
    sizes = ['small', 'medium', 'large']
    toppings = ['pepperoni', 'mushrooms', 'onions', 'sausage', 'bacon', 'olives']
    
    pizza_size = random.choice(sizes)
    pizza_toppings = random.sample(toppings, random.randint(1, len(toppings)))
    
    pizza = Pizza(pizza_size, pizza_toppings)
    
    topping_cost = Cost(1.50)
    total_cost = topping_cost.total_cost_w_toppings(len(pizza_toppings))
    
    return pizza.order(), total_cost

def display_order(order_details, total_cost):
    pizza_details = order_details.split(' with ')
    pizza_size = pizza_details[0].split(' ')[-1]
    pizza_toppings = pizza_details[1].split(' ')[0]
    
    print(f'Order Details:')
    print(f'Pizza Size: {pizza_size}')
    print(f'Toppings: {pizza_toppings}')
    print(f'Total Cost: {total_cost}')


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

#def main():
'''The main function of the pizza parlor simulation. This function provides options for taking orders, 
viewing orders, and exiting the pizza parlor simulation.'''
def main():
    orders = []

    while True:
        print("Welcome to Pizza Parlor!")
        print("1. Take Order")
        print("2. View Orders")
        print("3. Exit")

        choice = input("Please select a choice from the provided options: ")
 
        if choice == '1':
            size = input("Enter pizza size (small, medium, large): ")
            toppings = input("Enter toppings (comma-separated): ").split(',')
            new_order = Pizza(size.strip(), [topping.strip() for topping in toppings])
            orders.append(new_order)
            print("Order placed!")
        elif choice == '2':
            if orders:
                print("\nCurrent Orders:")
                for i, order in enumerate(orders, 1):
                    print(f"{i}. {order.order()} - Total Cost: ${order.total_cost():.2f}")
            else:
                print("No orders yet.")
        elif choice == '3':
            print("Thank you for visiting Pizza Parlor!")
            break
        else:
            print("Please try again. This time, select a provided option")

if __name__ == '__main__':
    main()


