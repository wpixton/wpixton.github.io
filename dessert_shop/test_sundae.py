from dessert import Sundae

#sundae tests
def test_sundae_default_value():
    sundae = Sundae()
    assert sundae._name == ""
    assert sundae._scoop_count == 0
    assert sundae._price_per_scoop == 0.0
    assert sundae._topping_name == ""
    assert sundae._topping_price == 0.0

def test_sundae_provided_value():
    sundae = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    assert sundae._name == "Vanilla"
    assert sundae._scoop_count == 3
    assert sundae._price_per_scoop == .69
    assert sundae._topping_name == "Hot Fudge"
    assert sundae._topping_price == 1.29

def test_sundae_updated_value():
    sundae = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    sundae._name = "Chocolate"
    sundae._scoop_count = 2
    sundae._price_per_scoop = .50
    sundae._topping_name = "Sprinkles"
    sundae._topping_price = 2.50
    assert sundae._name == "Chocolate"
    assert sundae._scoop_count == 2
    assert sundae._price_per_scoop == .50
    assert sundae._topping_name == "Sprinkles"
    assert sundae._topping_price == 2.50

def test_sundae_cost_calculation():
    sundae = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    assert sundae.calculate_cost() == 3.36

def test_sundae_tax_calculation():
    sundae = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    assert sundae.calculate_tax() == .24

