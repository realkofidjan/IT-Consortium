import logging
import json
from Modules.user_actions import user_handler

def controller(event):
    """
    AWS Lambda handler for processing SQS messages and invoking user actions.
    """
    responses = []

    for record in event.get("Records", []):
        try:
            message_body = json.loads(record["body"])
            action = message_body.get("action")
            if not action:
                logging.error("Action not found in message body")
                responses.append({
                    "statusCode": 400,
                    "body": json.dumps({"error": "Action not provided in message"})
                })
                continue

            response, status_code = user_handler(message_body)

            responses.append({
                "statusCode": status_code,
                "body": json.dumps(response)
            })

        except Exception as e:
            logging.error(f"Error processing record: {e}", exc_info=True)
            responses.append({
                "statusCode": 500,
                "body": json.dumps({"error": "Internal server error"})
            })

    return {
        "body": json.dumps(responses)
    }