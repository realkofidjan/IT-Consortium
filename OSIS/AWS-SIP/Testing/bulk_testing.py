import json
from unittest.mock import patch
from requests.models import Response
from App.main import lambda_handler
from Testing.templates import *

def populate_template(template, request_data):
    if "User" in template and "Attributes" in template["User"]:
        for attribute in template["User"]["Attributes"]:
            key = attribute["Name"]
            if key in request_data:
                attribute["Value"] = request_data[key]
        template["User"]["Username"] = request_data.get("user_id", "")
    elif "ChallengeParameters" in template:
        template["ChallengeParameters"]["USER_ID_FOR_SRP"] = request_data.get("user_id", "")
        user_attributes = {key: request_data[key] for key in ["email", "phone", "first_name", "last_name", "picture", "status"] if key in request_data}
        template["ChallengeParameters"]["userAttributes"] = json.dumps(user_attributes)
    elif "CodeDeliveryDetails" in template:
        template["CodeDeliveryDetails"]["Destination"] = request_data.get("email", "")
    return template

def dynamic_response(request_data):
    action = request_data.get("action")
    if action == "create":
        response_data = populate_template(get_create_response_template(), request_data)
        return create_mock_response(response_data, 200)
    elif action == "update":
        response_data = get_update_response_template()
        return create_mock_response(response_data, 200)
    elif action == "login":
        response_data = get_login_response_template()
        return create_mock_response(response_data, 200)
    return create_mock_response({"error": "Invalid action"}, 400)

def create_mock_response(data, status_code):
    response = Response()
    response._content = json.dumps(data).encode("utf-8")
    response.status_code = status_code
    return response

def load_event_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

@patch("requests.post")
@patch("requests.put")
def test_lambda_handler(mock_put, mock_post):
    mock_post.side_effect = lambda url, json: dynamic_response(json)
    mock_put.side_effect = lambda url, json: dynamic_response(json)
    
    test_event = load_event_data("Testing/events/sqs_bulk.json")

    response = lambda_handler(test_event, None)

    response_body = json.loads(response["body"])
    for item in response_body:
        print(item)

    for i, record in enumerate(test_event["Records"]):
        record_body = json.loads(record["body"])
        action = record_body.get("action")
        expected_status_code = 200 if action in ["create", "update", "login"] else 400
        assert response_body[i]["statusCode"] == expected_status_code
        
        response_details = json.loads(response_body[i]["body"])
        
        if "details" in response_details:
            details = json.loads(response_details["details"])
        else:
            details = response_details

        if action == "create":
            assert "User" in details, f"User not found in response details: {details}"
        elif action == "update":
            assert "ResponseMetadata" in details, f"ResponseMetadata not found in response details: {details}"
        elif action == "login":
            assert "ChallengeParameters" in details, f"ChallengeParameters not found in response details: {details}"