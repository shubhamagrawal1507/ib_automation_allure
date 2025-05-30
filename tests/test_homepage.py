import requests
import pytest
import logging
from pages.home_page import HomePage

logger = logging.getLogger()

def test_navbar_options(setup):

    logger.info("On InfoBeans Homepage")

    page = setup
    hp = HomePage(page)
    expected_options = ['Services', 'IB Platforms', 'Solutions', 'Industries', 'Insights', 'About InfoBeans']
    actual_options = hp.get_all_navbar_options()

    logger.info("Verifying options")

    assert actual_options == expected_options, "Actual options are different from Expected options"

    logger.info("Test Completed")

def test_contact_us_button(setup):

    logger.info("On InfoBeans Homepage")

    page = setup
    hp = HomePage(page)
    expected_link = "https://infobeans.com/contact-us"
    actual_link = hp.get_embedded_link(button_name="CONTACT US")

    logger.info("Verifying embedded link")

    assert actual_link == expected_link, "Actual link is different form Expected link"

    logger.info("Test Completed")

    
def test_get_infobeans():

    logger.info("Calling IB's API")

    response = requests.get(url="https://infobeans.com/")
    assert response.status_code == 200

    logger.info("Status Code Validated")

@pytest.mark.parametrize("input, output",[(18, "Valid"),(155, "Valid")])
def test_age(input, output):

    logger.info("Starting Test for validating age")
    ans = "Invalid"
    if input < 150:
        ans = "Valid"
    assert ans == output, "Input age is Invalid"
    logger.info("Test for validating age completed")

@pytest.mark.skip(reason= "This functionality is under development")
def test_sso_login():
    pass

@pytest.mark.xfail(reason="This test is expected to fail")
def test_outh2_login():

    logger.info("This test will fail")

    is_user_logged_in = False
    assert is_user_logged_in == True, "Login is failed"


