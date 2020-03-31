import MySQLdb
from pprint import pprint

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="admin")        # name of the database

cur = db.cursor()

cur.execute("SELECT branchName, branchCode, branchOPS, address1, address2, state, city, location, pincode, phone, fax, email, longitude, lattitude, website  FROM branchlocator WHERE isDeleted = '0'")


decodedBranchList = []

for row in cur.fetchall():
    tempDict = {}
    tempDict['name'] = row[0].decode('base64')
    tempDict['code'] = row[1].decode('base64')
    tempDict['ops'] = row[2].decode('base64')
    tempDict['address1'] = row[3].decode('base64').strip('\r\n').rstrip(" ")
    tempDict['address2'] = row[4].decode('base64').strip('\r\n').rstrip(" ")
    tempDict['state_id'] = int(row[5])
    tempDict['city_id'] = int(row[6])
    tempDict['location'] = row[7].decode('base64')
    tempDict['pincode'] = row[8].decode('base64')
    tempDict['phone'] = row[9].decode('base64')

    decodedBranchList.append(tempDict)




db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="cms")        # name of the database


cur = db.cursor()

for k in decodedBranchList:
	# print k['name']
	strng = "INSERT INTO `branch__branches` (`id`, `name`, `code`, `OPS`, `address`, `state_id`, `city_id`, `location`, `pincode`, `phone`,`created_by`,`updated_by`,`created_at`, `updated_at`) VALUES (NULL, '"+str(k['name'])+"', '"+str(k['code'])+"', '"+str(k['ops'])+"', '"+str(k['address1'])+"<br>"+str(k['address2'])+"', "+str(k['state_id'])+", "+str(k['city_id'])+", '"+str(k['location'])+"', '"+str(k['pincode'])+"', '"+str(k['phone'])+"', 1, 1, NOW(), NOW());"
	# cur.execute(strng)
	print strng

db.commit()


db.close()

# pprint(decodedBranchList)