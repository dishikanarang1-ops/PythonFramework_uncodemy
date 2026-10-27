
import pytest

from pages.portfolio import portfolio

@pytest.mark.smoke
def test_portfolio(page):
    obj=portfolio(page)
    obj.portfolio_viewmore_clicking()

@pytest.mark.smoke
def test_trank(page):
    obj=portfolio(page)
    obj.trank_tech()