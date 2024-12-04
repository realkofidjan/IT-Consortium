forgot_password_payload = {
    "Records": [
        {
            "body": {
                "action": "forgot",
                "email": "jason@gmail.com"
            }
        }
    ]
}

login_payload = {
    "Records": [
        {
            "body": {
                "action": "login",
                "email": "jason@gmail.com",
                "password": "password123"
            }
        }
    ]
}

resend_verification_payload = {
    "Records": [
        {
            "body": {
                "action": "resend-verification",
                "email": "jason@gmail.com",
            }
        }
    ]
}

delete_payload = {
    "Records": [
        {
            "body": {
                "action": "delete",
                "email": "jason@gmail.com",
            }
        }
    ]
}

update_payload = {
    "Records": [
        {
            "body": {
                "action": "update",
                "email": "jason@gmail.com",
                "given_name": "Jason",
                "family_name": "Smith",
                "phone_number": "+233200929118",
                "status": "active",
                "institution": "University of Ghana",
                "picture": "https://example.com/picture.jpg"
            }
        }
    ]
}

create_payload = {
    "Records": [
        {
            "body": {
                "action": "create",
                "email": "jason@gmail.com",
                "given_name": "Jason",
                "family_name": "Smith",
                "phone_number": "+233200929118",
                "status": "active",
                "institution": "University of Ghana",
                "picture": "https://example.com/picture.jpg"
            }
        }
    ]
}

bulk_payload = {
    "Records": [
        {
            "body": {
                "action": "create",
                "email": "jason@gmail.com",
                "given_name": "Jason",
                "family_name": "Smith",
                "phone_number": "+233200929118",
                "status": "active",
                "institution": "University of Ghana",
                "picture": "https://example.com/picture.jpg"
            },
            "body": {
                "action": "create",
                "email": "john.doe@gmail.com",
                "given_name": "John",
                "family_name": "Doe",
                "phone_number": "+233200929119",
                "status": "inactive",
                "institution": "Harvard University",
                "picture": "https://example.com/john.jpg"
            },
            "body": {
                "action": "update",
                "email": "jasmine@gmail.com",
                "given_name": "Jasmine",
                "family_name": "Smith",
                "phone_number": "+233200929118",
                "status": "active",
                "institution": "University of Ghana",
                "picture": "https://example.com/jasmine.jpg"
            },
            "body": {
                "action": "delete",
                "email": "jason@gmail.com",
            },
            "body": {
                "action": "forgot",
                "email": "jason@gmail.com"
            },
            "body": {
                "action": "login",
                "email": "jason@gmail.com",
                "password": "password123",
            },
            "body": {
                "action": "resend-verification",
                "email": "jason@gmail.com"
            }
        }
    ]
}