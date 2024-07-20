import requests
import json

def Checker(address_in, address_out, amount):
    url = "https://backend.swap.coffee/v1/route"
    payload = {
        "input_token": {
            "blockchain": "ton",
            "address": address_in
        },
        "output_token": {
            "blockchain": "ton",
            "address": address_out
        },
        "input_amount": amount,
        "max_splits": 4,
        "max_length": 3
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    # Parse the JSON response
    response_json = json.loads(response.text)

    # Extract the output_amount value from the data field
    return(response_json['output_amount'])
