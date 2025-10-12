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
    response = APIHelperDummy.get_products(test_data["valid_limit"])
    assert response.status_code == 200
    assert "products" in response.json()
    assert len(response.json()["products"]) <= test_data["valid_limit"]

@pytest.mark.api
def test_get_single_product_positive():
    logger.info("=== Positive: Get Single Product ===")
    response = APIHelperDummy.get_single_product(test_data["valid_product_id"])
    assert response.status_code == 200
    assert response.json()["id"] == test_data["valid_product_id"]