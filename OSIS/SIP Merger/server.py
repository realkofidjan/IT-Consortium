from flask import Flask, request, jsonify
import datetime
import uuid

app = Flask(__name__)

def generate_response(event):
    return {
        "ResponseMetadata": {
            "HTTPHeaders": {
                'connection': 'keep-alive',
                'content-type': 'application/json',
                'date': datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'),
                'requestId': str(uuid.uuid4()),
            },
            "HTTPStatusCode": 200,
            "RequestId": str(uuid.uuid4()),
            "RetryAttempts": 0
        },
        "User": {
            "Attributes": [
                {
                    "Name": f"{event['first_name']} {event['last_name']}",
                    "Value": str(uuid.uuid4())  # Simulated user ID
                }
            ],
            "Enabled": True,
            "UserCreateDate": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "UserLastModifiedDate": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "UserStatus": "CONFIRMED",
            "Username": f"{event['first_name'].lower()}{event['last_name'].lower()}",
        },
    }

@app.route('/create', methods=['POST'])
def create():
    event = request.get_json()
    
    # Ensure 'action' field is set to 'create'
    if not event or event.get('action') != 'create':
        return jsonify({"error": "Invalid action for /create endpoint. Action should be 'create'."}), 400

    return jsonify(generate_response(event)), 201

@app.route('/update', methods=['PUT'])
def update():
    event = request.get_json()
    
    # Ensure 'action' field is set to 'update'
    if not event or event.get('action') != 'update':
        return jsonify({"error": "Invalid action for /update endpoint. Action should be 'update'."}), 400

    return jsonify(generate_response(event)), 200

if __name__ == '__main__':
    app.run(debug=True)
