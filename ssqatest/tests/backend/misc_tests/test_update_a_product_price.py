import pytest
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ssqatest.src.dao.products_dao import ProductsDAO
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
    dao_helper = ProductsDAO()

    # Create a filter to pick items that are not on sale
    filters = {'on_sale':False, 'per_page': 100}

    # Use the filter to select the products not on sale.
    not_on_sale = api_helper.call_list_products(filters)
    any_product = api_helper.call_list_products()
    print(not_on_sale)

    if not_on_sale: # Select random products from products that are not on sale
        selected_item = random.choice(not_on_sale)
        print(f"selected item is: '{selected_item}'")
        item_id = selected_item['id']
        print(f"product id is : '{item_id}")
        price_selected_item = selected_item["sale_price"]
        name_selected_item = selected_item["name"]
        print(f"price of selected item: '{name_selected_item}' on sale is: '{price_selected_item}'")
    else: # Select random products if  all products are on sale.
        selected_item = random.choice(any_product)
        item_id = selected_item["id"]
        print(f"product id for a random item on sale : '{item_id}")
        selected_item["sale_price"] =""
        print(f"price of selected item is: '{price_selected_item}'")

    # For the selected item, update the price
    selected_item["sale_price"] = "10.00"
    updated_item = api_helper.call_update_product(item_id,selected_item["sale_price"])
    # print(f"details of the selected item is : '{selected_item}'")
    print(f"price of the selected item is : '{updated_item['sale_price']}'")

    # Verify that the new price is $10.00
    # product_rs = api_helper.call_get_product_by_id(item_id)
    # print(f"price from api is : '{product_rs['sale_price']}'")





    # For the product selected (both cases), update the price.

