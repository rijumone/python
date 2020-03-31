import sys
import requests

# 20670,12521

api_key = "LUh0Zc1qqOWkEgwrbSM4lfUTi8kYnKcZD8vh7zUS6UaylpLaUXskDnVKH4mRIW2d"

# https://www.zipcodeapi.com/rest/ujtZhtxIZku2ny8Cn3gXZGaumtnAvy3nWRyayiem83PTp1vcATGHwBnDhY1kCDpF/multi-distance.json/74018/20670,96860/mile

# print 500
r = requests.get("https://www.zipcodeapi.com/rest/" + api_key + "/distance.json/" + sys.argv[1] + "/" + sys.argv[2] + "/mile")
# r.status_code
# 200
# r.headers['content-type']
# 'application/json; charset=utf8'
# r.encoding
# 'utf-8'
# print r.text
# u'{"type":"User"...'
# print r.json()
if not "error_code" in r.json():
	print r.json()["distance"]
else:
	print r.json()["error_msg"]
# {u'private_gists': 419, u'total_private_repos': 77, ...}

