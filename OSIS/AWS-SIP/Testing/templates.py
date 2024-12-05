def get_create_response_template():
    return {
        "ResponseMetadata": {
            "HTTPHeaders": {
                "connection": "keep-alive",
                "content-length": "940",
                "content-type": "application/x-amz-json-1.1",
                "date": "Fri, 18 Oct 2024 11:34:54 GMT",
                "x-amzn-requestid": "4dce9074-50a1-4a5d-8b09-0273ecb10fe2"
            },
            "HTTPStatusCode": 200,
            "RequestId": "4dce9074-50a1-4a5d-8b09-0273ecb10fe2",
            "RetryAttempts": 0
        },
        "User": {
            "Attributes": [
                {"Name": "email", "Value": ""},
                {"Name": "phone_number", "Value": ""},
                {"Name": "family_name", "Value": ""},
                {"Name": "given_name", "Value": ""},
                {"Name": "picture", "Value": ""},
                {"Name": "custom:status", "Value": ""},
                {"Name": "custom:institution", "Value": ""},
                {"Name": "sub", "Value": ""}
            ],
            "Enabled": "true",
            "UserCreateDate": "Fri, 18 Oct 2024 11:34:54 GMT",
            "UserLastModifiedDate": "Fri, 18 Oct 2024 11:34:54 GMT",
            "UserStatus": "FORCE_CHANGE_PASSWORD",
            "Username": ""
        }
    }

def get_update_response_template():
    return {
        "ResponseMetadata": {
            "HTTPHeaders": {
                "connection": "keep-alive",
                "content-length": "2",
                "content-type": "application/x-amz-json-1.1",
                "date": "Fri, 18 Oct 2024 11:37:09 GMT",
                "x-amzn-requestid": "dd2f39cb-3d8c-4573-83a6-8a0858267393"
            },
            "HTTPStatusCode": 200,
            "RequestId": "dd2f39cb-3d8c-4573-83a6-8a0858267393",
            "RetryAttempts": 0
        }
    }
    
def get_login_response_template():
    return {
        "ChallengeName": "NEW_PASSWORD_REQUIRED",
        "ChallengeParameters": {
            "USER_ID_FOR_SRP": "72059404-c0b1-7058-fd93-19fa6c9cad66",
            "requiredAttributes": "[]",
            "userAttributes": "{\"custom:status\":\"active\",\"phone_number\":\"+233208283735\",\"given_name\":\"Joshua\",\"family_name\":\"Jason\",\"email\":\"josei@itconsortiumgh.com\",\"picture\":\"https://transflow-auth-test-bucket.s3.amazonaws.com/pngtree-user-profile-avatar-png-image_13369988.png\"}"
        },
        "ResponseMetadata": {
            "HTTPHeaders": {
                "connection": "keep-alive",
                "content-length": "1315",
                "content-type": "application/x-amz-json-1.1",
                "date": "Thu, 17 Oct 2024 13:42:43 GMT",
                "x-amzn-requestid": "d89dfc60-71b9-469a-a171-06332d91386f"
            },
            "HTTPStatusCode": 200,
            "RequestId": "d89dfc60-71b9-469a-a171-06332d91386f",
            "RetryAttempts": 0
        },
        "Session": "AYABeOcW6u5XlhwPMD-0ZKP_TukAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOmV1LXdlc3QtMTo0NTU0NTg0OTMwODE6a2V5L2FiN2U3M2UzLWU2NDEtNDk5Zi1iNzc0LWZkZmM1MWM3NzFhYQC4AQIBAHg2MqczZDLcfrmByK-jqwTPNbH_6yjwU8M-1Yu0RrEmiQHmwKgMX45UHOKIDdHaxdGHAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM1prXyj_UCcGWsNaJAgEQgDuUlMV64rbDetLfYjm4tXWRGkzdyFOM3j7QpCZ4_Ugu8uULqssKB8pyUfDob7puaCoPS994d_FBtMTJHwIAAAAADAAAEAAAAAAAAAAAAAAAAADkSNMh-l6j5CV8lS9kBCaD_____wAAAAEAAAAAAAAAAAAAAAEAAADxpC9c2ZKh-IO7ojkkvpXDSqDswEXKs-dgsTvTzRMBNgdQCUc9_30VOqZOw6ehcEYP9bbhZ-y_kGMlOuGB0mzls9m9tvtsI83b7yopIQ2K9s2WPm7sVEocv05dI28rfdHEYqak_4wwWdX2CO54GJ09GBPBJYpMY4ZueaDFAvNWU4-bpUf8ustztBNcZom5OwFr2vSLj62mObyvqBwNrWT57W20EaKkABVOioq8LPQ_n5CUjHoWnisPzLNr0n58ipjKHMwpbtH-EqSg6xM_i2cdf5j23AgE3oSJSPOT8A8DxGfhihJc9xF2_W5t93fHxU2PXcCk_-dJD6X01qTsguw7xUY"
    }
    
def get_forgot_password_response_template():
    {
  "CodeDeliveryDetails": {
    "AttributeName": "email",
    "DeliveryMedium": "EMAIL",
    "Destination": "j***@g***"
  },
  "ResponseMetadata": {
    "HTTPHeaders": {
      "connection": "keep-alive",
      "content-length": "100",
      "content-type": "application/x-amz-json-1.1",
      "date": "Thu, 17 Oct 2024 13:44:32 GMT",
      "x-amzn-requestid": "c32fda87-2e74-45fb-a54f-1fa39f33885e"
    },
    "HTTPStatusCode": 200,
    "RequestId": "c32fda87-2e74-45fb-a54f-1fa39f33885e",
    "RetryAttempts": 0
  }
}
