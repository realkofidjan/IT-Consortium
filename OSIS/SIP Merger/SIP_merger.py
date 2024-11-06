import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path=".env")

baseURL = os.getenv("BASE_URL")
print("Base URL:", baseURL)  # Debugging print to confirm baseURL is loaded

# Action types mapped to HTTP methods
action_map = {
    "create": "post",
    "update": "put",
    "delete": "delete",
    "forgot": "post",
    "resend-verification": "post",
    "login": "post",
}

def user_actions(queue):
    """
    Processes a queue of payloads, determining action type from each payload's 'action' field.
    """
    for payload in queue:
        action_type = payload.get("action")
        
        # Validate action type and method
        method = action_map.get(action_type)
        if not method:
            print(f"Invalid action type provided in payload: {action_type}")
            continue

        # Construct the URL
        url = f"{baseURL}/{action_type}"
        print(f"Performing {action_type.upper()} request to {url} with payload: {payload}")

        # Perform the request
        try:
            response = getattr(requests, method)(url, json=payload)

            # Display response code
            print(f"Action: {action_type} | Response Code:", response.status_code)

            # Attempt to parse JSON response or fallback to text response
            try:
                response_data = response.json()
            except ValueError:
                response_data = response.text

            # Print the response from the API
            print("Response Body:", response_data)

        except requests.exceptions.RequestException as e:
            print("An error occurred with action:", action_type, "| Error:", e)

# Define a queue with multiple actions
action_queue = [
    {
        "action": "create",
        "email": "bensmith@gmail.com",
        "first_name": "Ben",
        "last_name": "Smith",
        "phone": "+1234567890",
        "status": "active",
        "group": "OSIS",
        "picture": "https://example.com/picture.jpg"
    },
    {
        "action": "update",
        "email": "bensmith@gmail.com",
        "phone": "+0987654321",
        "status": "inactive"
    }
]

# Execute actions from the queue
if __name__ == "__main__":
    print("Processing action queue...")
    user_actions(action_queue)
