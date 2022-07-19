from flask import Flask
import requests
app = Flask (__name__)

api_key = "USE_YOUR_KEY_HERE"

@app.route('/')
def check():
    return {"Flask": "Up and running. Check the /status/order_id/email endpoint to get valid response"}


#if non existing endpoint would be used this will return the 404 error
@app.errorhandler(404)
def page_not_found(e):
    return {'errorCode': 404, 'message': 'Route not found'}

#Search for order number and validate user input with email address to provide status and tracking information if present.
@app.route('/status/<order>/<email>')
def get_status(order, email):
    headers = {"X-API-KEY": api_key}
    response = requests.get('https://customizations.chatbotize.com/ecommerce/orders', headers=headers)
    if response.ok:
        response = response.json()
    else:
        raise Exception('Originating API not responding')
    for item in response['items']:
        if item['orderNumber'] == order:
            if item['email'] == email:       
                # tracking informations are not shared for orders that are refunded as tracking informations are incorrect for this status
                if "tracking" in item.keys() and item['status'] != "refunded":               
                    return {"status": item['status'], "tracking_url": item['tracking']['url']}
                return{"status": item['status']}
    raise ValueError("Order doesn't exist.")
