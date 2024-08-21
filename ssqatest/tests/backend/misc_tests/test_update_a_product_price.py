import pytest
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
import logging as logger
pytestmark= [pytest.mark.products, pytest.mark.regression]
import random

@pytest.mark.be005
def test_update_price_of_product():
    """
    This is a test to find a product that is not on sale and update the pricing.
    If all products are on sale then pick a random product, make the sale price= $0.00 and then update the pricing.
    """
    # Create objects that will run API call and also an object for the DAO
    api_helper = ProductsAPIHelper()

    # Create a filter to pick items that are not on sale
    filters = {'on_sale':False, 'per_page': 100, 'type':'simple'}

    # Use the filter to select the products not on sale.
    not_on_sale = api_helper.call_list_products(filters)
    any_product = api_helper.call_list_products()

    if not_on_sale: # Select random products from products that are not on sale
        selected_item = random.choice(not_on_sale)
        item_id = selected_item['id']
        price_selected_item = selected_item["sale_price"]
        name_selected_item = selected_item["name"]
        print(f" The sale price of selected item that is NOT on sale'{name_selected_item}'  before update is:  is: '{price_selected_item}' and ID is {item_id}")
    else: # Select random products if  all products are on sale.
        selected_item = random.choice(any_product)
        item_id = selected_item["id"]
        price_selected_item = selected_item["sale_price"]
        print(f"product id for a random item on sale : '{item_id}'")
        selected_item["sale_price"] =""
        print(f"price of selected item is: '{price_selected_item}'")

    # For the selected item, update the price. Create a payload first
    payload = dict()
    payload['regular_price'] = "15.00"
    update_price = api_helper.call_update_product(item_id,payload=payload)  # Update the price to $15.00


    # Verify the price is updated correctly
    assert update_price['regular_price'] == "15.00", f"Regular Price was not updated. Expected was $'15.00' and Actual price is $'{update_price['regular_price']}' "

    # Verify from the API response
    rs_data = api_helper.call_retrieve_product(item_id)
    updated_rp = rs_data['regular_price']
    print(updated_rp)
    assert updated_rp == "15.00", "Price is not yet updated"

    logger.info("Passed test!")



