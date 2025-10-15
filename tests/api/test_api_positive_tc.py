import pytest
import json
from utilities.api_client import APIHelperDummy
from utilities.logger import get_logger

logger = get_logger("API_DUMMY_TESTS")

# Load test data
with open("Test_data/api_dummy_test_data.json") as f:
    test_data = json.load(f)

@pytest.mark.api
def test_get_products_positive():
    logger.info("=== Positive: Get Products ===")
    response = APIHelperDummy.get_products()
    logger.debug(f"Response status: {response.status_code}")
    logger.debug(f"Response body: {response.text}")

    if response.status_code == 200:
        logger.info("API returned status 200")
    else:
        logger.error(f"Unexpected status code: {response.status_code}")

    assert response.status_code == 200


@pytest.mark.api
def test_get_single_product_positive():
    product_id = test_data["valid_product_id"]
    logger.info(f"=== Positive: Get Single Product (ID: {product_id}) ===")
    response = APIHelperDummy.get_single_product(product_id)
    logger.debug(f"Response status: {response.status_code}")
    logger.debug(f"Response body: {response.text}")

    if response.status_code == 200:
        logger.info(f"Product {product_id} fetched successfully")
    else:
        logger.error(f"Failed to fetch product {product_id}, status {response.status_code}")

    assert response.status_code == 200

