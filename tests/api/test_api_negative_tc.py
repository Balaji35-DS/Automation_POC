import pytest
from utilities.api_client import APIHelper
from utilities.logger import get_logger

logger = get_logger("API NEGATIVE TESTS")


@pytest.mark.api
def test_invalid_user():
    logger.info("Starting API Negative test: Invalid User")
    res = APIHelper.get_user(9999)
    assert res.status_code == 200  # Should be 404
    logger.info("Invalid user and Test failed ")

@pytest.mark.api
def test_wrong_field():
    logger.info("Intentionally fail - wrong expected value")
    res = APIHelper.create_user("John", "Tester")
    assert res.status_code == 201
    assert res.json()["name"] == "Johnny"  # Wrong name
    logger.info("wrong user name and Test failed ")