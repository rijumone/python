# get_advertiser_ids.py

import json

with open("all_advertiser_data.json") as get_advertiser_ids_json_file:
	response_dict = json.loads(get_advertiser_ids_json_file.read())
ad_id_lst = []
for ad in response_dict["response"]:
	if ad["status"] == "ACTIVE":
		ad_id_lst.append({"id":ad["id"], "timezone": ad["timezone"]})

print(json.dumps(ad_id_lst, sort_keys=True, indent=2))	