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
    logger.debug(f"Response body: {response.text}")  # More detailed info
    if response.status_code == 404:
        logger.warning(f"Expected failure - Product not found (status {response.status_code})")
    else:
        logger.error(f"Unexpected response: {response.status_code}")

    assert response.status_code == 404


@pytest.mark.api
def test_create_product_negative_missing_title():
    logger.info("=== Negative: Create Product Missing Title ===")
    response = APIHelperDummy.create_product_missing_title(test_data["price_only"])
    logger.debug(f"Response body: {response.text}")

    if response.status_code == 201:
        logger.warning("Expected failure - Missing title validation error")
    else:
        logger.error(f"Unexpected status code: {response.status_code}")

    assert response.status_code == 201
    assert "title" in response.text
