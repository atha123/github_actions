import pytest
import logging as logger
from ssqatest.src.utilities.genericUtilities import generate_random_string
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ssqatest.src.dao.products_dao import ProductsDAO

pytestmark = [pytest.mark.backend]
"""
This is a test for the 'update' call 
"""
@pytest.mark.be004
def test_get_products_call():
    # Create a product first
    payload = dict()
    payload["name"] = generate_random_string(2, "update_")
    payload["weight"] = "2"
    payload["regular_price"] = "10.00"
    payload["short_description"] = "Stainless Steel Coffee Cup"
    product_create = ProductsAPIHelper().call_create_product(payload)
    productid = product_create['id']
    assert productid, "Test Product not created"
    logger.info(f"Product created is :'{payload['name']}'")

    # Create an updated payload and run the update API call. Then assert to make sure the UI shows the expected description.
    payload["short_description"] = "Wide-Slot Toaster - Stainless Steel"
    update_product=ProductsAPIHelper().call_update_product(productid,payload)
    assert update_product['short_description'] == "Wide-Slot Toaster - Stainless Steel", "Update did not happen in the UI"

    # Check the database to ensure the description is updated.
    data_db=ProductsDAO().get_product_by_id(productid)
    print(f"update description is : '{data_db[0]['post_excerpt']}'")
    assert data_db[0]['post_excerpt'] == "Wide-Slot Toaster - Stainless Steel", f"Description did not update to 'Wide-Slot Toaster - Stainless Steel'"
    logger.info("Test Passed!")