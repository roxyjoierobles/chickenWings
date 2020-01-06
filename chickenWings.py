# File: chickenWings.py

# print("testing python")

import requests
import json

CLIENT_ID = "-cfWQyBjJ2Uoq184P-iiNg"
API_KEY = "E6m6f9Kakj0u6GMX2xWCESxXhbkPaDG9qI4LkV30VPSREZXADOk6c4RJGMyfGHg4BVCZBItLo1RYX5tGDg6QuLuMVcKJpIo_BMYOdycvSdX9j4w91GpTlGocOmAGXnYx"

HEADERS = {"Authorization": "Bearer %s" % API_KEY}

URL = "https://api.yelp.com/v3/businesses/search"

# TODO:
# missing restaurants such as flying beaver --> category: pubs, american (traditional)
# OR TRY WINGS NIGHT: https://www.yelp.com/search?find_desc=wings+night&find_loc=Vancouver%2C+BC

# WINGS_PARAMS = {"locale": "en_CA","location":"Vancouver", "term":"wings","categories":"chicken_wings", "limit": "50", "sort_by":"rating"}
WINGS_PARAMS = {"locale": "en_CA","location":"Vancouver", "term":"wings", "limit": "50", "sort_by":"rating"}
# params above give business near Vancouver, including Richmond & Burnaby
# if business does not have any reviews, it will not be included

RESTAURANTS = []

def get_results(wings_params):
    # make request
    request = requests.get(URL, params=wings_params, headers=HEADERS)
    # proceeds only if status code = 200
    print("The status code is {}".format(request.status_code))
    parsed = json.loads(request.text)
    # print(parsed)
    restaurants = parsed['businesses']
    for rest in restaurants:
        restInfo = []
        # all necessary restaurant info
        restInfo.append(rest["id"])
        restInfo.append(rest["name"])
        restInfo.append(rest["image_url"])
        restInfo.append(rest["is_closed"])
        restInfo.append(rest["url"])
        restInfo.append(rest["rating"])
        restInfo.append(rest["location"]["city"])
        restInfo.append(" ".join(rest["location"]["display_address"]))
        restInfo.append(rest["phone"])
        print("Restaurant Info: ", restInfo)
        RESTAURANTS.append(restInfo)
    # print(json.dumps(parsed, indent=4))
    print("Restaurants printed: ", len(RESTAURANTS))
    if len(RESTAURANTS) == 50:
        total_results = parsed["total"]
        print("Total restaurants found: ", total_results)
        return total_results
    return


def main():
    total_results = get_results(WINGS_PARAMS)
    # iterates through remaining results
    # first iteration is i = 0: results 51 - (100 - total_results)
    remaining_results = total_results - 50
    print("remaining ", remaining_results)
    i = 0
    while remaining_results >= 0:
        offset = 51 + i*50
        print("iteration ", i)
        i += 1
        wings_offset = {"offset":offset}
        WINGS_PARAMS.update(wings_offset)
        get_results(WINGS_PARAMS)
        remaining_results -= 50
    print("Array of businesses: ", RESTAURANTS)
main()


# expanded search - TO NOTE: restaurants w/ no reviews are not included in count
# NOW USE: https://www.yelp.com/search?find_desc=wings&find_loc=Vancouver%2C%20BC
# before used https://www.yelp.com/search?find_desc=food&find_loc=Vancouver%2C%20BC&cflt=chicken_wings&sortby=recommended which limited results
# only 58 because some of the results do not have any reviews -> 64 - 6 = 58!! THESE PLACES HAS NO REVIEWS SO NOT INCLUDED
# 27. https://www.yelp.com/biz/texas-barbecue-chicken-and-ribs-burnaby?osq=food
# 34. https://www.yelp.com/biz/panago-pizza-vancouver-17?osq=food -- no reviews!
# 52. https://www.yelp.com/biz/panago-pizza-north-vancouver-2?osq=food -- no reviews!
# 53. https://www.yelp.com/biz/panago-pizza-burnaby-2?osq=food -- no reviews!
# 56. https://www.yelp.com/biz/chicken-delight-burnaby?osq=food -- no reviews!
# 60. https://www.yelp.com/biz/lees-chicken-burnaby?osq=food -- no reviews!