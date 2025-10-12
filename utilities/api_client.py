import requests
from utilities.logger import get_logger
from config.config import Config

logger = get_logger("API_HELPER_DUMMY")

class APIHelperDummy:

    @staticmethod
    def get_products(limit):
        logger.info(f"Fetching products with limit: {limit}")
        return requests.get(f"{Config.API_BASE_URL}/products", params={"limit": limit})

    @staticmethod
    def get_single_product(product_id):
        logger.info(f"Fetching product with ID: {product_id}")
        return requests.get(f"{Config.API_BASE_URL}/products/{product_id}")

    @staticmethod
    def create_product(title, price):
        logger.info(f"Creating product: {title}, price: {price}")
        payload = {"title": title, "price": price}
        return requests.post(f"{Config.API_BASE_URL}/products/add", json=payload)

    @staticmethod
    def create_product_missing_title(price):
        logger.info(f"Creating product without title, price: {price}")
        payload = {"price": price}
        return requests.post(f"{Config.API_BASE_URL}/products/add", json=payload)
