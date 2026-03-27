from dessert import Order, Candy, Cookie
from payment import PayType
import pytest
def test_get_and_set_cash():
    order = Order()
    order.set_pay_type(PayType.CASH)
    assert order.get_pay_type() == PayType.CASH

def test_get_and_set_card():
    order = Order()
    order.set_pay_type(PayType.CARD)
    assert order.get_pay_type() == PayType.CARD

def test_get_and_set_phone():
    order = Order()
    order.set_pay_type(PayType.PHONE)
    assert order.get_pay_type() == PayType.PHONE

def test_get_invalid_value():
    order = Order()
    with pytest.raises(ValueError, match=r"Invalid pay type:"):
        order.set_pay_type("BITCOIN")  # type: ignore

def test_set_invalid_value():
    order = Order()
    order.__dict__["_payment_type"] = "BITCOIN"
    with pytest.raises(ValueError, match=r"Invalid pay type:"):
        order.get_pay_type()

def test_order_sort():
    order = Order()
    
    
    cookie = Cookie("Expensive cookie", 1, 20)
    candy1 = Candy("Lots of Candy", 20, 2)
    candy = Candy("Candy", 1, 1)

    cookie.calculate_cost()
    candy.calculate_cost()
    candy1.calculate_cost()


    order.add(cookie)
    order.add(candy)
    order.add(candy1)
    order.sort()

     

    # Extract the prices to check ascending order
    prices = [item.price for item in order._list_of_items]

    # Assert that prices are in ascending order
    assert prices == sorted(prices)
    

def test_order_iteration():
    
    o = Order()
    c1 = Candy("Gummy Bears", 0.25, 1.0)
    c2 = Cookie("Chocolate Chip", 1.99, 6)
    
    o.add(c1)
    o.add(c2)

    items = []
    for item in o:  # Uses __iter__ and __next__ under the hood
        items.append(item)
    
    assert items == [c1, c2]








    