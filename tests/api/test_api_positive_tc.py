import pytest
from utilities.api_client import APIHelper
from utilities.logger import get_logger

logger = get_logger("API POSITIVE TESTS")

@pytest.mark.api
def test_get_users():
    logger.info("Starting API positive test: Create User")
    res = APIHelper.get_users()
    assert res.status_code == 200
    assert "data" in res.json()
    logger.info("Test passed successfully")



@pytest.mark.api
def test_update_user():
    res = APIHelper.update_user(2, "Balaji", "QA Engineer")
    assert res.status_code == 401
    body = res.json()
    assert "updatedAt" in body
