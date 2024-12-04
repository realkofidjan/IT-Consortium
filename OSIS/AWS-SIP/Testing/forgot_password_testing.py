from Testing.test_payload import forgot_password_payload
from App.main import lambda_handler
from unittest.mock import patch
import json

def test_forgot_password():
    # Mock the `requests.post` method
    with patch("Modules.user_actions.requests.post") as mock_post:
        # Configure the mock to return a successful response
        mock_post.return_value.status_code = 200
        mock_post.return_value.headers = {"x-amzn-requestid": "mock-request-id"}

        # Call the lambda handler with the payload
        response = lambda_handler(forgot_password_payload, None)

        # Parse the response body
        response_body = json.loads(response["body"])

        # Check if the response status code is 200 (OK)
        assert response_body[0]["statusCode"] == 200, f"Expected statusCode 200, got {response_body[0]['statusCode']}"

        # Check if the response contains the expected message
        expected_message = "Password reset email sent successfully."
        assert expected_message in response_body[0]["body"], f"Expected message '{expected_message}' not found in response"

        # Optionally, check if there are no errors in the response
        assert "error" not in response_body[0]["body"], f"Unexpected error found in response: {response_body[0]['body']}"
