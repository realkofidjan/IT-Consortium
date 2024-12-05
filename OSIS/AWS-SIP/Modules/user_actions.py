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
            
            # Assuming that the ChallengeParameters are dynamic and depend on the payload or other logic
            challenge_parameters = {
                "USER_ID_FOR_SRP": "72059404-c0b1-7058-fd93-19fa6c9cad66",  # Example static value
                "requiredAttributes": "[]",  # Empty list as a string (example)
                "userAttributes": json.dumps({
                    "custom:status": "active",
                    "phone_number": "+233208283735",
                    "given_name": "Joshua",
                    "family_name": "Jason",
                    "email": payload.get("username"),
                    "picture": "https://transflow-auth-test-bucket.s3.amazonaws.com/pngtree-user-profile-avatar-png-image_13369988.png"
                })
            }

            return {
                "ChallengeName": "NEW_PASSWORD_REQUIRED",
                "ChallengeParameters": challenge_parameters,
                "ResponseMetadata": {
                    "HTTPStatusCode": response.status_code,
                    "RequestId": response.headers.get("x-amzn-requestid", "N/A")
                },
                "Session": "SESSION_ID"  # Use appropriate session id or dynamic value
            }, 200
        else:
            logging.error(f"Error logging in user: {response.text}")
            return {
                "error": "Failed to login user",
                "details": response.text,
            }, response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {"error": "Failed to connect to the external API"}, 500
