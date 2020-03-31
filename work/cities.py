import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="admin")        # name of the database

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT stateId, cityName FROM cities")

allCities = []
stateIds = []
stateIdsIN = ""

# print all the first cell of all the rows
for row in cur.fetchall():
    allCities.append(row)
    if not row[0] in stateIds:
    	stateIds.append(row[0])

for k in range(len(stateIds)):
	stateIdsIN = stateIdsIN + str(stateIds[k]) + ","	

stateIdsIN = stateIdsIN.rstrip(",")
# print allCities
# print stateIds
# print stateIdsIN

# now that we have all cities


#let's get the state names
cur.execute("SELECT stateId, stateName FROM states WHERE stateId IN("+stateIdsIN+")")

statesNamekDict = {}

for row in cur.fetchall():
	statesNamekDict[int(row[0])] = row[1]

print statesNamekDict
db.close()



# let's close the db connection 


db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="cms")  


# and open a new one


cur = db.cursor()
sql = ""

# Use all the SQL you like
# cur.execute("SELECT stateId, cityName FROM cities")

# for k in (range(allCities)):
# 	sql = "INSERT into cities (`name`,`state_id) VALUES (" + str(allCities[k][1]) + "," + str(allCities[k][1]) +")"


# Use all the SQL you like
# cur.execute("INSERT ")
