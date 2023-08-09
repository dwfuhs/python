import pytest
from account import *


def test_init():
    t_name = Account('David')
    assert t_name.get_name() == 'David'
    assert t_name.get_balance() == pytest.approx(0)


def test_deposit():
    t_name = Account('David')
    assert t_name.deposit(-2) is False
    assert t_name.get_balance() == pytest.approx(0)
    assert t_name.deposit(0) is False
    assert t_name.get_balance() == pytest.approx(0)
    assert t_name.deposit(2) is True
    assert t_name.get_balance() == pytest.approx(2)


def test_withdraw():
    t_name = Account('David')
    t_name.set_balance(5)
    assert t_name.withdraw(-2) is False
    assert t_name.get_balance() == pytest.approx(5)
    assert t_name.withdraw(0) is False
    assert t_name.get_balance() == pytest.approx(5)
    assert t_name.withdraw(10) is False
    assert t_name.get_balance() == pytest.approx(5)
    assert t_name.withdraw(3) is True
    assert t_name.get_balance() == pytest.approx(2)
