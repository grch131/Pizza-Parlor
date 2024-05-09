'''Pizza Parlor Simulator!   By Diamond Andy, Grace Choe, Jason Liu, and Daniel Amare '''

import random

class Pizza:
     
    def __init__(self, pizza_size, pizza_toppings):
        
        """This function initializes the size anbd toppings of the customers pizza.
        """
        
        self.pizza_size = pizza_size
        
        self.pizza_toppings = pizza_toppings
        
    def total_cost(self):
        
        """This function will give the estimated cost of the customer's pizza

        Returns:
            float: The estimated total cost of the customers pizza.
        """
        
        base_cost = 9.99
        
        toppings_cost = len(self.pizza_toppings) * 1.00
        
        total = base_cost + toppings_cost
        
        if self.pizza_size.lower() == 'medium':
            
            total += 2
            
        elif self.pizza_size.lower() == 'large':
            
            total += 4
            
        else:
            
            total += 1
            
        return total
    
    def order(self):
        
        """This function contains the order of the customer.

        Returns:
            str: A string of the customers order: the size of the pizza and the toppings they have chosen.
        """
        
        return f'You want a {self.pizza_size} pizza with {",".join(self.pizza_toppings)} toppings!'
        


def display_order(order_details, total_cost):
    
    """This function takes the details of a pizza order and the total cost as input and prints them out.

    Args:
        order_details (str): A string containing the details of the pizza order.
        total_cost (float): The total cost of the pizza order.
    """
    pizza_details = order_details.split(' with ')
    
    pizza_size = pizza_details[0].split(' ')[-1]
    
    pizza_toppings = pizza_details[1].split(' ')[0]
    
    print(f'Order Details:')
    
    print(f'Pizza Size: {pizza_size}')
    
    print(f'Toppings: {pizza_toppings}')
    
    print(f'Total Cost: {round(total_cost, 2)}')


class Cost:
    def __init__(self, toppings_cost):
        
        """This function will be used to initialize the base_cost of the pizza, which is 9.99
        and it will also initialize the toppings_cost 

        Args:
            toppings_cost (float): How much each of the toppings cost 
        """
        
        self.base_cost = 9.99 
        
        self.toppings_cost = toppings_cost
        
    def total_cost_w_toppings(self, num_toppings):
        
        """This function will be used to calculate the total cost of the specific pizza 
        selected with all the toppings calculated in it

        Args:
            num_toppings (int): This is the number of toppings that will be on the pizza

        Returns:
            total_cost: How much the total pizza will cost with all the toppings added to the base price 
        """
        total_cost = self.base_cost + (num_toppings * self.toppings_cost)
        
        return total_cost
        
    def profit(self, num_sales, num_toppings):
        """This function will calculate the total profit from all the pizzas sold

        Args:
            num_sales (int): How many pizzas we have sold
            num_toppings (int): How many toppings there are

        Returns:
            float: The total profit earned from all the pizza sold 
        """
        ingredient_cost = 5.00
        
        total_sales = num_sales * self.total_cost_w_toppings(num_toppings)
        
        total_cost = num_sales * 5.00
        
        profit = total_sales - total_cost
        
        return profit 

def main():
    
    '''The main function of the pizza parlor simulation. This function provides options for taking orders,
    viewing orders, viewing profit, and exiting the pizza parlor simulation.'''
    
    orders = []
    
    num_sales = 0
    
    total_toppings_sold = 0

    while True:
        
        print("Welcome to Pizza Parlor!")
        
        print("1. Take Order")
        
        print("2. View Orders")
        
        print("3. View Profit")
        
        print("4. Exit")

        choice = input("Please select a choice from the provided options: ")

        if choice == '1':
            size = input("Enter pizza size (small, medium, large): ")
            
            toppings = input("Enter toppings (comma-separated): ").split(',')
            
            new_order = Pizza(size.strip(), [topping.strip() for topping in toppings])
            
            orders.append(new_order)
            
            num_sales += 1
            
            total_toppings_sold += len(toppings)
            
            print("Order placed!")

            display_order(new_order.order(), new_order.total_cost())

        elif choice == '2':
            
            if orders:
                
                print("\nCurrent Orders:")
                
                for i, order in enumerate(orders, 1):
                    
                    print(f"{i}. {order.order()} - Total Cost: ${order.total_cost():.2f}")
            else:
                print("No orders yet.")

        elif choice == '3':
            
            if num_sales > 0:
                
                topping_cost = Cost(1.00)
                
                total_profit = topping_cost.profit(num_sales, total_toppings_sold)
                
                print(f"Total Profit: ${total_profit:.2f}")
                
            else:
                
                print("No sales yet.")

        elif choice == '4':
            
            print("Thank you for visiting our Pizza Parlor!")
            
            break

        else:
            
            print("Please try again. This time, select a provided option")


if __name__ == '__main__':
    main()


