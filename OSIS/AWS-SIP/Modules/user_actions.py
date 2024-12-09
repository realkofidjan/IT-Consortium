import json
import logging
import requests
from Config.config import Config

logging.basicConfig(level=logging.INFO)

url = Config.BASE_URL


def user_handler(payload):
    """
    Processes the payload based on the 'action' field.
    """

    action_type = payload.get("action")

    logging.debug(f"Received payload: {payload}")
    logging.debug(f"Determined action: {action_type}")

    if action_type == "create":
        return handle_create(payload)
    elif action_type == "update":
        return handle_update(payload)
    elif action_type == "login":
        return handle_login(payload)
    elif action_type == "forgot":
        return handle_forgot_password(payload)
    elif action_type == "delete":
        return handle_delete(payload)
    elif action_type == "resend-verfication":
        return handle_resend_verification(payload)
    else:
        return {"error": "Invalid action"}, 400


def handle_create(payload):
    """
    Handle the 'create' action by making an HTTP POST request.
    """
    logging.info(f"Sending data to {url}: {payload}")

    try:
        response = requests.post(url, json=payload)

        if response.status_code == 201:
            logging.info("User created successfully")
            return {
                "message": "User create action processed successfully.",
                "ResponseData": payload,
                "ResponseMetadata": {
                    "HTTPStatusCode": response.status_code,
                    "RequestId": response.headers.get("x-amzn-requestid", "N/A")
                },
            }, 201
        else:
            logging.error(f"Error creating user: {response.text}")
            return {
                "error": "Failed to create user",
                "details": response.text,
            }, response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {"error": "Failed to connect to the external API"}, 500


def handle_update(payload):
    """
    Handle the 'update' action.
    """
    logging.info(f"Sending data to {url}: {payload}")

    try:
        response = requests.put(url, json=payload)

        if response.status_code == 200:
            logging.info("User updated successfully")
            return {
                "message": "User update action processed successfully.",
                "ResponseData": payload,
                "ResponseMetadata": {
                    "HTTPStatusCode": response.status_code,
                    "RequestId": response.headers.get("x-amzn-requestid", "N/A")
                },
            }, 200
        else:
            logging.error(f"Error updating user: {response.text}")
            return {
                "error": "Failed to update user",
                "details": response.text,
            }, response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {"error": "Failed to connect to the external API"}, 500

def handle_login(payload):
    """
    Handle the 'login' action.
    """
    logging.info(f"Sending data to {url}: {payload}")

    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            logging.info("User logged in successfully")
            return response.json(), 200
        else:
            logging.error(f"Error logging in user: {response.text}")
            return {
                "error": "Failed to login user",
                "details": response.text,
            }, response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {"error": "Failed to connect to the external API"}, 500
    
def handle_forgot_password(payload):
    """
    Handle the 'forgot_password' action.
    """
    logging.info(f"Sending data to {url}: {payload}")

    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            logging.info("User password reset initiated successfully")
            return response.json(), 200
        else:
            logging.error(f"Error initiating password reset: {response.text}")
            return {
                "error": "Failed to reset password",
                "details": response.text,
            }, response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {"error": "Failed to connect to the external API"}, 500
    
def handle_delete(payload):
    """
    Handle the 'delete' action.
    """
    logging.info(f"Sending data to {url}: {payload}")

    try:
        response = requests.delete(url, json=payload)

        if response.status_code == 200:
            logging.info("User deleted successfully")
            return response.json(), 200
        else:
            logging.error(f"Error deleting user: {response.text}")
            return {
                "error": "Failed to delete user",
                "details": response.text,
            }, response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {"error": "Failed to connect to the external API"}, 500
    
    
def handle_resend_verification(payload):
    """
    Handle the 'resend_verification' action.
    """
    logging.info(f"Sending data to {url}: {payload}")

    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            logging.info("Verification email resent successfully")
            return response.json(), 200
        else:
            logging.error(f"Error resending verification email: {response.text}")
            return {
                "error": "Failed to resend verification email",
                "details": response.text,
            }, response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {"error": "Failed to connect to the external API"}, 500