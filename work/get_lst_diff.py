"""
take in two lists
print their diff
"""

lst1 = ["Advertiser_ID","Day","Hour","Advertiser_Name","Advertiser_Timezone","Advertiser_Currency","Campaign_ID","Campaign_Name","Campaign_Objective","Campaign_Start_Date","Campaign_End_Date","Campaign_Status","Budget","Budget_Type","Ad_Group_ID","Ad_Group_Name","Ad_Group_Status","Ad_ID","Ad_Title","Ad_Description","Ad_Status","Ad_Format","Ad_SponsoredBy","Ad_Image_URL","Ad_Landing_URL","Ad_Display_URL","Impressions","Clicks","CTR","Conversions","Spend","Average_CPC","Average_Cost_Per_Install","Average_CPM","Average_Position","Pricing_Type","Source","Max_Bid","ts_created","ts_updated",]

lst2 = ["Advertiser_ID","Day","Campaign_ID","Impressions","Clicks","CTR","Conversions","Spend","Average_CPC","Average_Cost_Per_Install","Average_CPM","Average_Position","Click_Outs","Click_Outs_Rate","Forward_Rate","Forwards","Opens","Save_Rate","Saves","Cost_Per_Video_View","Video_100_Percent_Complete","Video_25_Percent_Complete","Video_50_Percent_Complete","Video_75_Percent_Complete","Video_Closed","Video_Skipped","Video_Starts","Video_Views","Ad_Extn_Conversions","Post_Click_Conversions","Post_Impression_Conversions","Post_Impression_CPA","Total_Conversions","Ad_Group_Tracking_URL","Device_Type","Ad_Extn_Clicks","Ad_Extn_Impressions","Ad_Extn_Spend","Advertiser_Name","Campaign_Name","Campaign_Objective","Native_Average_CPC","Native_CTR","Native_Clicks","Native_Conversions","Native_Impressions","Native_Spend","Search_Average_CPC","Search_CTR","Search_Clicks","Search_Conversions","Search_Impressions","Search_Spend","Engagement_Rate","Engagements","Follow_Rate","Follows","Like_Rate","Likes","Paid_Engagement_Rate","Paid_Engagements","Reblog_Rate","Reblogs","Video_Completes_With_Audio","Video_Expands","Video_Replays","Video_Unmutes","Landing_Page_Type","Delivery_Status","Native_Recommended_Bid","Post_Click_CPA","Post_Click_Conversion_Rate","Post_View_Conversion_Rate","Spend_USD","Ad_ID","Ad_Name","Ad_Title","In_App_Post_Click_Conversions","In_App_Post_Install_Conversions","In_App_Post_View_Conversions","ts_created","ts_updated",]

for item in lst1:
	if item not in lst2:
		print(item)