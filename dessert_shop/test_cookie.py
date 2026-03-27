from dessert import Cookie, Candy
import pytest

#cookie tests
def test_cookie_defualt_value():
    cookie = Cookie()
    assert cookie._name == ""
    assert cookie._cookie_quantity == 0
    assert cookie._price_per_dozen == 0.0

def test_cookie_provided_value():
    cookie = Cookie("Chocolate Chip", 6, 3.99)
    assert cookie._name == "Chocolate Chip"
    assert cookie._cookie_quantity == 6
    assert cookie._price_per_dozen == 3.99
    

def test_cookie_updated_value():
    cookie = Cookie("Chocolate Chip", 6, 3.99)
    cookie._name = "Small Cookie"
    cookie._cookie_quantity = 3
    cookie._price_per_dozen = 2.99
    assert cookie._name == "Small Cookie"
    assert cookie._cookie_quantity == 3
    assert cookie._price_per_dozen == 2.99

def test_cookie_cost_calculation():
    cookie = Cookie("Chocolate Chip", 6, 3.99)
    assert cookie.calculate_cost() == 2.0

def test_cookie_tax_calculation():
    cookie = Cookie("Chocolate Chip", 6, 3.99)
    assert cookie.calculate_tax() == 0.14 




#test the combine and can combine methods
#test if can combine returns True when price is same and name is same 
def test_cookie_can_combine_true():
    cookie1 = Cookie("gummy bears", 200, 1.5)
    cookie2 = Cookie("gummy bears", 50, 1.5)
    assert cookie1.can_combine(cookie2) == True


#test if can combine returns false when price is different
def test_cookie_can_combine_false_price():
    cookie1 = Cookie("gummy bears", 200, 1.5)
    cookie2 = Cookie("gummy bears", 50, 1.6)
    assert cookie1.can_combine(cookie2) == False

#test if can combine returns false when name is different
def test_cookie_can_combine_false_name():
    cookie1 = Cookie("gummy bear", 200, 1.5)
    cookie2 = Cookie("gummy bears", 50, 1.6)
    assert cookie1.can_combine(cookie2) == False

#test if can combine returns false when other item is not a cookie

def test_cookie_can_combine_false_class():
    candy = Candy("gummy bear", 200, 1.5)
    cookie2 = Cookie("gummy bears", 50, 1.6)
    assert candy.can_combine(cookie2) == False

#test for combine() to verify it correctly combines two cookie items when they can be combined.
def test_cookie_combine_true():
    cookie1 = Cookie("gummy bears", 200, 1.5)
    cookie2 = Cookie("gummy bears", 50, 1.5)
    assert cookie1.combine(cookie2) == Cookie("gummy bears", 250, 1.5)

#test for combine() to verify it correctly raises TypeError when the other item is not a cookie.
def test_cookie_combine_TypeError():
    candy = Candy("gummy bears", 200, 1.5)
    cookie = Cookie("gummy bears", 50, 1.5)
    with pytest.raises(TypeError):
        cookie.combine(candy)
