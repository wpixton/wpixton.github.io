from abc import ABC, abstractmethod
from payment import Payable, PayType
from combine import Combinable

from packaging import Packaging
class DessertItem(ABC, Packaging): 
   
    def __init__(self, name: str = "", tax_percent: float = 7.25):
        self.packaging = "None"
        self._name = name
        self._tax_percent = tax_percent
        self._price = 0.0

    #format the name of product string
    def __str__(self):
        return f"Name of product: {self._name}"
    
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = price

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tax_percent(self):
        return self._tax_percent
    @tax_percent.setter
    def tax_percent(self, tax_percent):
        self._tax_percent = tax_percent

    def calculate_tax(self):
        tax = self._tax_percent / 100
        return round(self.calculate_cost() * tax, 2)
        
    @abstractmethod
    def calculate_cost(self):
        pass

    



    def __eq__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.price == other.price

    def __ne__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.price != other.price

    def __lt__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.price <= other.price

    def __gt__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.price > other.price

    def __ge__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented
        return self.price >= other.price

    


    # def __eq__(self, other):
    #     return self.price == other.price
    
    # def __lt__(self, other):
    #     return self.price < other.price

    # def __gt__(self, other):
    #     return self.price > other.price

    # def __le__(self, other):
    #     return self.price <= other.price

    # def __ge__(self, other):
    #     return self.price >= other.price

    # def __ne__(self, other):
    #     return self.price != other.price
    
   


#DessertShop class. gets the user input, validates the input, convirts items to the proper types and creates objects for them 
class DessertShop:
    def get_float_input(self, prompt):
        while True:
            user_input = input(prompt)
            try:
                # Attempt to convert the input to an integer
                float_value = float(user_input)
                return float_value  # If successful, return the integer
            except ValueError:
                # If conversion fails, a ValueError is raised
                print("Please enter a number")

    def get_int_input(self, prompt):
        while True:
            user_input = input(prompt)
            try:
                # Attempt to convert the input to an integer
                int_value = int(user_input)
                return int_value  # If successful, return the integer
            except ValueError:
                # If conversion fails, a ValueError is raised
                print("Please enter a whole number")

     #code to get input about payment type

    def get_payment_type_from_user(self):
        print("1:CASH\n2:CARD\n3:PHONE")
        done: bool = False
        while not done:
            payment_type = self.get_int_input("Enter payment method: ")
            
            if payment_type == "":
                print("Please enter a number")
            else:
               
                if payment_type <=3 and payment_type >= 1:
                    done = True
                else: 
                    print("Please enter a number 1-3")
       
   
        return PayType(str(payment_type))
              




    #get candy name
    def user_prompt_candy(self):
        done: bool = False
        candy_name = ""
        while not done:
            candy_name = input("Enter name of candy: ")
            if candy_name == "":
                print("Please enter a product name")
            else:
                if isinstance(candy_name, str) :
                    done = True
                else:
                    print(f"{candy_name} must be a string")
        #get candy weight
        done = False
        candy_weight = 0.0
        while not done:
            candy_weight = self.get_float_input("Candy weight (lbs): ")
            if candy_weight == "":
                print("Please enter a weight")
            else:
                if candy_weight <= 0:
                    print("Please enter a number above zero")
                else:
                    done = True
        #candy price per pound
        done = False
        price_per_pound = 0.0
        while not done:
            price_per_pound = self.get_float_input("Enter price per pound: ")
            if price_per_pound == "":
                print("Please enter a price")
            else: 
                if price_per_pound <= 0:
                    print("Please enter a number above zero")
                else:
                    done = True
        
        return Candy(candy_name, candy_weight, price_per_pound)
        
    
    #get cookie name
    def user_prompt_cookie(self):
        done: bool = False
        while not done:
            cookie_name = input("Enter name of Cookie: ")
            if cookie_name == "":
                print("Please enter a name")
            else:
                if isinstance(cookie_name, str):
                    done = True
                else:
                    print("Please enter the name as a string")

        #get cookie quantity
        done = False
        while not done:
            cookie_quantity = self.get_int_input("Enter cookie quantity: ")
            if cookie_quantity == "":
                print("Please enter a quantity")
            else:
                if cookie_quantity <= 0:
                    print("Please enter a number above zero")
                else:
                    done = True

        #get price per dozen
        done = False
        while not done:
            price_per_dozen = self.get_float_input("Enter price per dozen: ")
            if price_per_dozen == "":
                print("Please enter a price")
            else: 
                if price_per_dozen <= 0:
                    print("Please enter a number above 0")
                else: 
                    done = True

        return Cookie(cookie_name, cookie_quantity, price_per_dozen)

    #get icecream type
    def user_prompt_icecream(self):
        done: bool = False
        while not done:
            icecream_type = input("Enter type of ice cream: ")
            if icecream_type == "":
                print("Please enter an ice cream type")
            else:
                if isinstance(icecream_type, str):
                    done = True
                else:
                    
                    print("Please enter ice cream type as a string")
        #get scoop count
        done = False
        while not done:
            scoop_count = self.get_int_input("Enter the number of scoops: ")
            if scoop_count == "":
                print("Please enter an amount of scoops")
            else:
                if scoop_count <= 0:
                    print("Please enter an amount greater than 0")
                else: 
                    done = True
        #get price per scoop
        done = False
        while not done:
            price_per_scoop = self.get_float_input("Enter the price per scoop: ")
            if price_per_scoop == "":
                print("Please enter a price per scoop")
            else:
                if price_per_scoop <= 0: 
                    print("Please enter a price Greater than 0")
                else: 
                    done = True

        return IceCream(icecream_type, scoop_count, price_per_scoop)
    #get sundae info
    def user_prompt_sundae(self):
        #make an icecream object to reuse the user_prompt_icecream method
        icecream_object = self.user_prompt_icecream()
        #topping name
        done = False
        while not done:
            topping_name = input("Enter the topping: ")
            if topping_name == "":
                print("Please enter a topping name")
            else:
                if isinstance(topping_name, str):
                    done = True
                else: 
                    print("Please enter topping name as a string")
            #topping price
        done = False
        while not done:
            topping_price = self.get_float_input("Enter the price for the topping: ")
            if topping_price == "":
                print("Please enter a price for the topping")
            else: 
                if topping_price <= 0:
                    print("Please enter a topping price greater than 0")
                else:
                    done = True

        return Sundae(icecream_object.name, icecream_object.scoop_count, icecream_object.price_per_scoop, topping_name, topping_price)
        



#The Candy class. calls the __init__ in the DesertItem class
class Candy(DessertItem):


    def __init__(self, name: str = "", candy_weight: float = 0.0, price_per_pound: float = 0.0):
        super().__init__(name)
        self.packaging = "Bag"
        self._candy_weight = candy_weight
        self._price_per_pound = price_per_pound

    def __str__(self):
        return (f"{self.name} ({self.packaging})\n-     {self.candy_weight} lbs. @ ${self.price_per_pound}:, ${self.calculate_cost()}, [Tax: ${self.calculate_tax()}]" )

    def can_combine(self, other:"Candy") -> bool:
        if isinstance(other, Candy):

            if self.name == other.name and self.price_per_pound == other.price_per_pound:
                return True
            
        return False
        
    def combine(self, other: "Candy") -> "Candy":
   
        if not isinstance(other, Candy):
            raise TypeError
        self._candy_weight += other.candy_weight
        
        return self
            
   
            

    
    #getters and setters for candy class
    @property
    def candy_weight(self):
        return self._candy_weight
    
    @candy_weight.setter
    def candy_weight(self, weight):
        self._candy_weight = weight

    @property
    def price_per_pound(self):
        return self._price_per_pound
    
    @price_per_pound.setter
    def price_per_pound(self, price):
        self._price_per_pound = price

    def calculate_cost(self):
       self.price = round(self.candy_weight * self.price_per_pound, 2)
       return self.price
    
    

# #The Cookie class. calls the __init__ in the DesertItem class
class Cookie(DessertItem):
    

    def __init__(self, name: str = "", cookie_quantity: int = 0, price_per_dozen: float = 0.0):
        super().__init__(name)
        self.packaging = "Box"
        self._cookie_quantity = cookie_quantity
        self._price_per_dozen = price_per_dozen

    def __str__(self):
        return (f"{self.name} ({self.packaging})\n-     {self.cookie_quantity} cookies. @ ${self.price_per_dozen}/dozen:, ${self.calculate_cost()}, [Tax: ${self.calculate_tax()}]" )
    #getters and setters for cookie class
    @property
    def cookie_quantity(self):
        return self._cookie_quantity
    
    @cookie_quantity.setter
    def cookie_quantity(self, quantity):
        self._candy_weight = quantity
    #gets the price
    @property
    def price_per_dozen(self):
        return self._price_per_dozen
    
    #sets the price
    @price_per_dozen.setter
    def price_per_dozen(self, price):
        self._price_per_dozen = price

    # calculates the cost and rounds to two decimals
    def calculate_cost(self):
        dozen = self.cookie_quantity / 12
        self.price = round(dozen * self.price_per_dozen, 2)
        return self.price
    
    #checks to see if able to combine
    def can_combine(self, other:"Cookie") -> bool:
        if isinstance(other, Cookie):

            if self.name == other.name and self.price_per_dozen == other.price_per_dozen:

                return True
           
        return False
    
    # combines two items into one if they are in the cookie class
    def combine(self, other: "Cookie") -> "Cookie":
        if not isinstance(other, Cookie):
            raise TypeError
        self._cookie_quantity += other._cookie_quantity
        
        return self

#The IceCream class. calls the __init__ in the DesertItem class
class IceCream(DessertItem):
    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0):
 
        super().__init__(name)
        self.packaging = "Bowl"
        self._scoop_count = scoop_count
        self._price_per_scoop = price_per_scoop

    def __str__(self):
        return (f"{self.name} ({self.packaging})\n-     {self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop:, ${self.calculate_cost()}, [Tax: {self.calculate_tax()}]")

    #getters and setters for IceCream class
    @property
    def scoop_count(self):
        return self._scoop_count
    
    @scoop_count.setter
    def scoop_count(self, count):
        self._scoop_count = count

    @property
    def price_per_scoop(self):
        return self._price_per_scoop
    
    @price_per_scoop.setter
    def price_per_scoop(self, price):
        self._price_per_scoop = price

    def calculate_cost(self):
        self.price = round(self.scoop_count * self.price_per_scoop, 2)
        return self.price


#The Sundae class. calls the __init__ in the IceCream class
class Sundae(IceCream):
    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0, topping_name: str = "", topping_price: float = 0.0):

        super().__init__(name, scoop_count, price_per_scoop)
        self.packaging = "Boat"
        self._topping_name = topping_name
        self._topping_price = topping_price
 
    def __str__(self):
        return (f"{self.name} ({self.packaging})\n-     {self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop\n-     {self.topping_name} topping @ {self.topping_price}:, ${self.calculate_cost()}, [Tax: {self.calculate_tax()}]")
    #getters and setters for the sundae class
    @property
    def topping_name(self):
        return self._topping_name
    
    @topping_name.setter
    def topping_name(self, name):
        self._topping_name = name

    @property
    def topping_price(self):
        return self._topping_price
    
    @topping_price.setter
    def topping_price(self, price):
        self._topping_price = price

    def calculate_cost(self):
        self.price = round(self.scoop_count * self.price_per_scoop + self.topping_price, 2)
        return self.price


    #the order class. it combines all the items into a list, puts them on new lines, and counts the number of items
class Order(Payable): 
    def __init__(self):
        self._list_of_items = []
        self._payment_type = PayType.CASH
    
    def __str__(self):
        return_value = ""
        for item in self._list_of_items:
            return_value += f"{item.__str__()}\n"
        return_value += f"Paid with {self._payment_type}"
        return return_value
        
    def get_pay_type(self):
        if self._payment_type not in (PayType.CASH, PayType.CARD, PayType.PHONE):
            raise ValueError(f"Invalid pay type: {self._payment_type}")
        return self._payment_type
    
    def set_pay_type(self, payment_method: PayType):
        if payment_method not in (PayType.CASH, PayType.CARD, PayType.PHONE):
            raise ValueError(f"Invalid pay type: {payment_method}")
        self._payment_type = payment_method



    def __iter__(self):
        self._a = 0
        return self
    
    def __next__(self):
        if self._a < len(self._list_of_items):
            item = self._list_of_items[self._a]
            self._a += 1
            return item
        else:
            raise StopIteration

    def to_list(self):
        data_list = []

          

        data_list.append(["Name", "Cost", "Tax"])
        data_list.append(["-------------------------------", "----------", "------------"])


        for item in self._list_of_items:
            item_string = item.__str__()
            new_line_split = item_string.split("\n")
            for i in new_line_split:
                comma_split = i.split(",")
                data_list.append(comma_split)
        data_list.append(["----------", "----------", "----------"])
        data_list.append(["Total Items in the order:", f"{len(self._list_of_items)}"])
        data_list.append(["Order Subtotals:", f"${self.order_cost()}", f"[Tax: ${self.order_tax()}]"])
        data_list.append(["Order Total:", "", f"{self.order_total()}"])
        data_list.append(["--------------------"])
        data_list.append([f"Paid with {self._payment_type.name}"])

        

        return data_list  
            #data_list.append([item.name, f"{item.calculate_cost()}", f"{item.calculate_tax()}"])

    def add(self, dessertitem):
        combined = False
        for item in self:
            #checks if both items are combinable 
            if isinstance(item, Combinable) and isinstance(dessertitem, Combinable):
                
                
                if item.can_combine(dessertitem):
                    item.combine(dessertitem)
                    combined = True
                    break
        if not combined:
            self._list_of_items.append(dessertitem)
        #if dessertitem is not combinable then add to list. 
   
            #check to see if item is combinable 
  
        
            
       
   
    def __len__(self):
        return len(self._list_of_items)
    
    def order_cost(self):
        cost = 0
        for item in self._list_of_items:
            cost += item.calculate_cost()
        return round(cost, 2)

    def order_tax(self):
        tax = 0
        for item in self._list_of_items:
            tax += item.calculate_tax()
        return round(tax, 2)
    
    def order_total(self):
        return round(self.order_cost() + self.order_tax(), 2)
    
    
    def sort(self):
        sorted_list = []
        self.order_cost()
        smallest_item = Candy("sort_test")
    
        first_time: bool = True
        
        while len(self._list_of_items) > 0:
            first_time = True
            for item in self._list_of_items:
                if item < smallest_item or first_time == True:
                    smallest_item = item 
                first_time = False
            sorted_list.append(smallest_item) 
            self._list_of_items.remove(smallest_item)
        self._list_of_items = sorted_list
        print(self._list_of_items)

    
