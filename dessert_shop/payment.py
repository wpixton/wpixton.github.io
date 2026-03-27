from typing import Protocol
from enum import Enum


class PayType(str, Enum):
    """Only CASH, CARD or PHONE are allowed."""
    CASH  = 1
    CARD  = 2
    PHONE = 3


# ----------------------------------------------------------------------
# 2. Payable protocol – two abstract methods, no implementation
# ----------------------------------------------------------------------
class Payable(Protocol):
    def get_pay_type(self) -> PayType:
        """Return the current payment method."""
        ...

    def set_pay_type(self, payment_method: PayType) -> None:
        """Change the payment method."""

     