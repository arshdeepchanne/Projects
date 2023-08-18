from project import set_limit, set_today_total, set_savings, days_remaining


def test_set_limit():
    assert set_limit(2, 3100, 100) == round(((3100 - 100) / days_remaining(2)), 2)
    assert set_limit(22, 2500, 1000) == round(((2500 - 1000) / days_remaining(22)), 2)

def test_set_today_total():
    assert set_today_total(50, 20) == 70.00
    assert set_today_total(85, 20) == 105.00

def test_set_saving():
    assert set_savings(3000, 1500) == 1500.00
    assert set_savings(2100, 500) == 1600.00
