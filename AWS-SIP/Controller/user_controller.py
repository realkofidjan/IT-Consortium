import logging
import json
from Modules.user_actions import user_handler

def controller(event):
    """
    AWS Lambda handler for processing SQS messages and invoking user actions.
    """
    # Initialize the responses list to collect all responses for each record
    responses = []
    
    # Process each record from the SQS event
    for record in event.get("Records", []):
        try:
            # Parse the message body
            message_body = json.loads(record["body"])
            action = message_body.get("action")

            if not action:
                logging.error("Action not found in message body")
                responses.append({
                    "statusCode": 400,
                    "body": json.dumps({"error": "Action not provided in message"})
                })
                continue

            # Call the user_controller's function to handle the action
            response, status_code = user_handler(message_body)  # This invokes the action handler

            # Add the response to the list
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

    # Return the final response containing all processed records
    return {
        "body": json.dumps(responses)
    }
    

