import requests
from config.config import Config
from utilities.logger import get_logger

logger = get_logger("API_HELPER")

class APIHelper:

    @staticmethod
    def get_users(page=2):
        url = f"{Config.API_BASE_URL}/users?page={page}"
        logger.info(f"GET Request: {url}")
        response = requests.get(url)
        logger.info(f"Response Status: {response.status_code}, Body: {response.text}")
        return response

    @staticmethod
    def create_user(name, job):
        url = f"{Config.API_BASE_URL}/users"
        payload = {"name": name, "job": job}
        logger.info(f"POST Request: {url}, Payload: {payload}")
        response = requests.post(url, json=payload)
        logger.info(f"Response Status: {response.status_code}, Body: {response.text}")
        return response

    @staticmethod
    def get_user(user_id):
        url = f"{Config.API_BASE_URL}/users/{user_id}"
        logger.info(f"GET Request: {url}")
        response = requests.get(url)
        logger.info(f"Response Status: {response.status_code}, Body: {response.text}")
        return response

    @staticmethod
    def update_user(user_id, name, job):
        url = f"{Config.API_BASE_URL}/users/{user_id}"
        headers = {"Content-Type": "application/json"}
        payload = {"name": name, "job": job}
        logger.info(f"PUT Request: {url}, Payload: {payload}, Headers: {headers}")
        response = requests.put(url, json=payload, headers=headers)
        logger.info(f"Response Status: {response.status_code}, Body: {response.text}")
        return response
