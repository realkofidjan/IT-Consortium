import json
import logging
from Controller.user_controller import controller

logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    
    return controller(event)