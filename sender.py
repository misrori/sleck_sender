from dotenv import load_dotenv
import os
load_dotenv()

import requests

headers = {
    'Content-type': 'application/json',
}

json_data = {
    'text': 'Hello, slack!a',
}

response = requests.post(
    f'https://hooks.slack.com/services/T083CQWQS7N/B083CSAP5TN/{os.environ.get("SLACK_ID")}',
    headers=headers,
    json=json_data,
)

print(response)
