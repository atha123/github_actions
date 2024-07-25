import pytest
import logging as logger
from ssqatest.src.utilities.genericUtilities import generate_random_string
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ssqatest.src.dao.products_dao import ProductsDAO

pytestmark = [pytest.mark.backend]
"""
This is a test to check the get call 
"""
@pytest.mark.be003
def test_get_products_call():
    # Create a product first
    payload = dict()
    payload["name"] = generate_random_string(5, "get_")
    payload["weight"] = "2"
    payload["regular_price"] = "10.00"
    product_create = ProductsAPIHelper().call_create_product(payload)
    productid = product_create['id']
    assert productid, "Product no created"

    #Validate to check that the response of the get call is not empty
    get_the_product=ProductsAPIHelper().call_get_product_by_id(productid)
    assert get_the_product, "Did not get anything"

    # Get values from the database
    data_db = ProductsDAO()
    db_data=data_db.get_product_by_id(productid)

    # Validate that the values from the get call match the database values
    assert db_data[0]['post_title'] == get_the_product['slug'], "Expected name does not match actual"
    assert db_data[0]['post_status'] == get_the_product['status'], "Expected status does not match actual status"

    logger.info("Test Passed!")









