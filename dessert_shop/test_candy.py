from dessert import Candy, Cookie
import pytest

#candy tests
def test_candy_default_value():
    candy = Candy()
    assert candy._name == ""
    assert candy._candy_weight == 0.0
    assert candy._price_per_pound == 0.0

def test_candy_provided_value():
    candy = Candy("Candy Corn", 1.5, .25)
    assert candy._name == "Candy Corn"
    assert candy._candy_weight == 1.5
    assert candy._price_per_pound == .25

def test_candy_updated_value():
    candy = Candy("Candy Corn", 1.5, .25)
    candy._name = "Gummy Bears"
    candy._candy_weight = .26
    candy._price_per_pound = .35
    assert candy._name == "Gummy Bears"
    assert candy._candy_weight == .26
    assert candy._price_per_pound == .35

def test_candy_cost_calculation():
    candy = Candy("Candy Corn", 1.5, .25)
    assert candy.calculate_cost() == .38

def test_candy_tax_calculation():
    candy = Candy("Candy Corn", 1.5, .25)
    assert candy.calculate_tax() == .03




#test the combine and can combine methods
#test if can combine returns True when price is same and name is same 
def test_candy_can_combine_true():
    candy1 = Candy("gummy bears", 200, 1.5)
    candy2 = Candy("gummy bears", 50, 1.5)
    assert candy1.can_combine(candy2) == True


#test if can combine returns false when price is different
def test_candy_can_combine_false_price():
    candy1 = Candy("gummy bears", 200, 1.5)
    candy2 = Candy("gummy bears", 50, 1.6)
    assert candy1.can_combine(candy2) == False

#test if can combine returns false when name is different
def test_candy_can_combine_false_name():
    candy1 = Candy("gummy bear", 200, 1.5)
    candy2 = Candy("gummy bears", 50, 1.6)
    assert candy1.can_combine(candy2) == False

#test if can combine returns false when other item is not a candy

def test_candy_can_combine_false_class():
    candy1 = Cookie("gummy bear", 200, 1.5)
    candy2 = Candy("gummy bears", 50, 1.6)
    assert candy1.can_combine(candy2) == False

#test for combine() to verify it correctly combines two Candy items when they can be combined.
def test_candy_combine_true():
    candy1 = Candy("gummy bears", 200, 1.5)
    candy2 = Candy("gummy bears", 50, 1.5)
    assert candy1.combine(candy2) == Candy("gummy bears", 250, 1.5)

#test for combine() to verify it correctly raises TypeError when the other item is not a Candy.
def test_candy_combine_TypeError():
    cookie1 = Cookie("gummy bears", 200, 1.5)
    candy = Candy("gummy bears", 50, 1.5)
    with pytest.raises(TypeError):
        cookie1.combine(candy)


'''









Add a '''



