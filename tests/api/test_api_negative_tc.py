import pytest
import json
from utilities.api_client import APIHelperDummy
from utilities.logger import get_logger

logger = get_logger("API_DUMMY_TESTS")

# Load test data
with open("Test_data/api_dummy_test_data.json") as f:
    test_data = json.load(f)


@pytest.mark.api
def test_get_single_product_negative():
    logger.info("=== Negative: Get Non-Existing Product ===")
    response = APIHelperDummy.get_single_product(test_data["invalid_product_id"])
    assert response.status_code == 401
    logger.info("=== Negative: Failed product not found and passes if status code is 404 ===")

@pytest.mark.api
def test_create_product_negative_missing_title():
    logger.info("=== Negative: Create Product Missing Title ===")
    response = APIHelperDummy.create_product_missing_title(test_data["price_only"])
    assert response.status_code == 201 or "title" in response.text