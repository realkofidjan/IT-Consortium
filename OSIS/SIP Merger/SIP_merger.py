import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path=".env")

baseURL = os.getenv('BASE_URL')
print("Base URL:", baseURL)  # Debugging print to confirm baseURL is loaded

def create_user():
    url = f"{baseURL}/create"
    payload = {
        "email": "bensmith@gmail.com",
        "first_name": "Ben",
        "last_name": "Smith",
        "phone": "+1234567890",
        "status": "active",
        "group": "OSIS",
        "picture": "https://example.com/picture.jpg",
        "action": "create",
    }

    try:
        response = requests.post(url, json=payload)
        
        # Check the status code
        print("Response Code:", response.status_code)
        
        # Attempt to parse JSON response
        try:
            response_data = response.json()
        except ValueError:
            # If JSON decoding fails, fallback to text response
            response_data = response.text  

        # Print the response from the API
        print("Response Body:", response_data)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    create_user()
