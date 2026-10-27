
import pytest

from pages.contactus import contact

@pytest.mark.smoke
def test_contact(page):
    obj=contact(page)
    obj.contact_information()
    
@pytest.mark.smoke
def test_trank(page):
    obj=contact(page)
    obj.trank_tech()