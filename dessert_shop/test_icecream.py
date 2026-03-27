from dessert import IceCream

#icecream tests
def test_icecream_default_value():
    icecream = IceCream()
    assert icecream._name == ""
    assert icecream._scoop_count == 0 
    assert icecream._price_per_scoop == 0.0

def test_icecream_provided_value():
    icecream = IceCream("Pistachio", 2, .79)
    assert icecream._name == "Pistachio"
    assert icecream._scoop_count == 2
    assert icecream._price_per_scoop == .79

def test_icecream_updated_value():
    icecream = IceCream("Pistachio", 2, .79)
    icecream._name = "Small Scoop"
    icecream._scoop_count = 1
    icecream._price_per_scoop = .39
    assert icecream._name == "Small Scoop"
    assert icecream._scoop_count == 1
    assert icecream._price_per_scoop == .39

def test_icecream_cost_calculation():
    icecream = IceCream("Pistachio", 2, .79)
    assert icecream.calculate_cost() == 1.58

def test_icecream_tax_calculation():
    icecream = IceCream("Pistachio", 2, .79)
    assert icecream.calculate_tax() == 0.11

