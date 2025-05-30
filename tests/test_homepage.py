import requests
from pages.home_page import HomePage


def test_navbar_options(setup):
    page = setup
    hp = HomePage(page)
    expected_options = ['Services', 'Platforms', 'Solutions', 'Industries', 'Insights', 'About InfoBeans']
    actual_options = hp.get_all_navbar_options()
    assert actual_options == expected_options, "Actual options are different from Expected options"
    
def test_contact_us_button(setup):
    page = setup
    hp = HomePage(page)
    expected_link = "https://infobeans.com/contact-us"
    actual_link = hp.get_embedded_link(button_name="CONTACT US")
    assert actual_link == expected_link, "Actual link is different form Expected link"

def test_get_infobeans():
    response = requests.get(url="https://infobeans.com/")
    assert response.status_code == 200
