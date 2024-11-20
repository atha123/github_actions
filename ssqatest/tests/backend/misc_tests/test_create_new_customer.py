import logging as logger
import pytest
from ssqatest.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper
from ssqatest.src.dao.customers_dao import CustomersDAO

@pytest.mark.be006
def test_create_new_customer():
    """
    This is a test to verify if a new user can be registered through a REST API call.
    We also verify to make sure that the id of the user in the API call response matches the id in the DB.
    """

    # Create an object for the API call then create a customer and get the email id.
    api_obj = CustomersAPIHelper()
    new_cust = api_obj.call_create_customer()
    new_cust_email = new_cust["email"]
    new_cust_id = new_cust["id"]
    # Print the email id of he customer.
    print(f"Email id in API response is : {new_cust_id}")
    # breakpoint()

    # Create an object to get the data from the database for the newly created customer based on the email.
    db_helper = CustomersDAO()
    data_from_db = db_helper.get_customer_by_email(new_cust_email)
    db_id = data_from_db[0]['ID']


    logger.info(f"ID from API response is {db_id} ")
    logger.info(f"ID from DB is {new_cust_id}")

    assert new_cust_id == db_id, "Ids do not match"



    logger.info("Test completed: Customer correctly created!")

