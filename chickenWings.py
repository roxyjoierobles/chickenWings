# File: chickenWings.py

# print("testing python")

import requests
import json

CLIENT_ID = "-cfWQyBjJ2Uoq184P-iiNg"
API_KEY = "E6m6f9Kakj0u6GMX2xWCESxXhbkPaDG9qI4LkV30VPSREZXADOk6c4RJGMyfGHg4BVCZBItLo1RYX5tGDg6QuLuMVcKJpIo_BMYOdycvSdX9j4w91GpTlGocOmAGXnYx"

HEADERS = {"Authorization": "Bearer %s" % API_KEY}

URL = "https://api.yelp.com/v3/businesses/search"
WINGS_PARAMS = {"locale": "en_CA", "term":"food", "location":"Vancouver", "categories":"chicken_wings", "sort_by":"rating"}
# TODO:
# missing restaurants such as cactus, and joey, etc.
# need to get more than 20 results --> max number of returns, need to use offset
# PARAMS = {"locale": "en_CA", "term":"food", "location":"Vancouver", "categories":"newcanadian", "sort_by":"rating"}


# make request
request = requests.get(URL, params=WINGS_PARAMS, headers=HEADERS)

# proceeds only if status code = 200
print("The status code is {}".format(request.status_code))

parsed = json.loads(request.text)
# restaurants = parsed["businesses"]
# count = 0
# for rest in restaurants:
#     count += 1
#     print(rest, " \n")
#
# print("Count of restaurants ", count)

print(json.dumps(parsed, indent=4))