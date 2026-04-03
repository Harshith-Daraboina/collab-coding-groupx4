import pytest
from cafe_management.billing import Billing


def test_subtotal():
    billing = Billing()
    items = [
        {"name": "Coffee", "price": 100, "quantity": 2},
        {"name": "Sandwich", "price": 150, "quantity": 1},
    ]
    assert billing.calculate_subtotal(items) == 350


def test_empty_items():
    billing = Billing()
    assert billing.calculate_subtotal([]) == 0.0


def test_negative_values():
    billing = Billing()
    items = [{"name": "Coffee", "price": -10, "quantity": 1}]
    
    with pytest.raises(ValueError):
        billing.calculate_subtotal(items)


def test_discount():
    billing = Billing()
    assert billing.apply_discount(200, 10) == 180


def test_invalid_discount():
    billing = Billing()
    with pytest.raises(ValueError):
        billing.apply_discount(200, 150)


def test_tax():
    billing = Billing(tax_rate=0.05)
    assert pytest.approx(billing.apply_tax(100), 0.01) == 105


def test_generate_bill():
    billing = Billing(tax_rate=0.1)
    items = [
        {"name": "Tea", "price": 50, "quantity": 2},
    ]

    result = billing.generate_bill(items, discount=10)

    assert result["subtotal"] == 100
    assert pytest.approx(result["total"], 0.01) == 99
