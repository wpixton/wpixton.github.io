from dessert import DessertItem, Candy, Cookie, IceCream, Sundae
#dessertitem tests

#def test_tax_percent():


def test_dessertitem_default_value():
    candy = Candy()
    assert candy._name == ""
    assert candy._tax_percent == 7.25

    cookie = Cookie()
    assert cookie._name == ""
    assert cookie._tax_percent == 7.25

    icecream = IceCream()
    assert icecream._name == ""
    assert icecream._tax_percent == 7.25

    sundae = Sundae()
    assert sundae._name == ""
    assert sundae._tax_percent == 7.25
    
def test_dessertitem_provided_value():

    candy = Candy("candy")
    assert candy._name == "candy"
    assert candy._tax_percent == 7.25

    cookie = Cookie("cookie")
    assert cookie._name == "cookie"
    assert cookie._tax_percent == 7.25

    icecream = IceCream("icecream")
    assert icecream._name == "icecream"
    assert icecream._tax_percent == 7.25

    sundae = Sundae("sundae")
    assert sundae._name == "sundae"
    assert sundae._tax_percent == 7.25

def test_dessertitem_updated_values():
    candy = Candy("candy")
    candy._name = "candy1"
    candy._tax_percent = 7.24
    assert candy._name == "candy1"
    assert candy._tax_percent == 7.24

    cookie = Cookie("cookie")
    cookie._name = "cookie1"
    cookie._tax_percent = 7.24
    assert cookie._name == "cookie1"
    assert cookie._tax_percent == 7.24

    icecream = IceCream("icecream")
    icecream._name = "icecream1"
    icecream._tax_percent = 7.24
    assert icecream._name == "icecream1"
    assert icecream._tax_percent == 7.24

    sundae = Sundae("sundae")
    sundae._name = "sundae1"
    sundae._tax_percent = 7.24
    assert sundae._name == "sundae1"
    assert sundae._tax_percent == 7.24

def test_eq_operator():
    c1 = Candy("Candy A", 1, 2)   
    c2 = Candy("Candy B", 1, 2)   
    c3 = Candy("Candy C", 2, 2)   

    c1.calculate_cost()
    c2.calculate_cost()
    c3.calculate_cost()

    
    assert c1 == c2           
    assert c1 != c3     

def test_le_and_lt_operator(): 
    c1 = Candy("Candy A", 1, 2)   
    c2 = Candy("Candy B", 1, 2)   
    c3 = Candy("Candy C", 2, 2)   


    c1.calculate_cost()
    c2.calculate_cost()
    c3.calculate_cost()

    assert c1 <= c2
    assert c2 < c3

def test_ge_and_lt_operator():

    c1 = Candy("Candy A", 1, 2)   
    c2 = Candy("Candy B", 1, 2)   
    c3 = Candy("Candy C", 2, 2)   


    c1.calculate_cost()
    c2.calculate_cost()
    c3.calculate_cost()

    assert c1 >= c2
    assert c3 > c2


















  