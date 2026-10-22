import pytest

from pages.verticals import verticals

@pytest.mark.smoke
def test_trading(page):
    obj=verticals(page)
    obj.trading_options_clicking()

@pytest.mark.smoke
def test_retail(page):
    obj=verticals(page)
    obj.retail_ecommerce_clicking()
    
@pytest.mark.smoke
def test_healthcare(page):
    obj=verticals(page)
    obj.healthcare_clicking()


@pytest.mark.smoke
def test_fintech(page):
    obj=verticals(page)
    obj.fintech_clicking()


@pytest.mark.smoke
def test_custom(page):
    obj=verticals(page)
    obj.custom_App_clicking()

