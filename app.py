#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
import pandas as pd

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def handle_share_availability(zone, prod):
    pass

def makeWebhookResult(req):
    action = req.get("result").get("action")
    if action == "Share_Availability":
        parameters = result.get("parameters")
        handle_share_availability(parameters.get("Country"), parameters.get("Product"))
    elif action == "":
        pass
    else:
        return {}
       
    if  != "Share_Availability":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("Country")
    prod = parameters.get("Product")

    
    # Voorbeeld met alle mogelijkheden met prijs inbegrepen
    df = pd.read_csv(fname)
    with open(fname, "r") as file:
        cost = eval(" ".join(line.strip() for line in file))
    
    {
        'Algeria': {
        "available": True,
        "price": 100
        },
        'Andorra': {
        "available": False,
        "price": 100
        },
        'Belgium': {
        "available": True,
        "price": 500
        }   
    }
    
    if cost[zone]["available"]:
        speech = "The %s is available in %s for the price of %s euros." % (prod, zone, cost[zone]["price"]
    else:
        speech = "Sorry, The %s is not available in %s" % (prod, zone)
    
    speech = ("The %s is available in %s for the price of %s euros." % (prod, zone, cost[zone]["price"]) if cost[zone]["available"]
              else "Sorry, The %s is not available in %s" % (prod, zone))
    
    #if cost[zone]["available"]:
    # speech = ("You are lucky, the $product is available in %s." (zone)) 
    #else: 
    #  speech = ("Sorry, the $product is not available in %s." (zone))            

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-availability"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
