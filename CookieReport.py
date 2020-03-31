import requests
from datetime import datetime, timedelta

def createandwritefile(filename, content):
    try:
        f = open('reports/'+filename,"w")
        f.write(content +"\n")
        f.close()
    except Exception:
        print("Error in file write")

def CallFormat0A(payload, filename):
    print(payload)
    print(filename)

def CallFormat1(payload, filename):
    print(payload)
    print(filename)

def CallFormat0(payload, filename):
    print(payload)
    print(filename)

def APICallFormat0(payload, filename):
    print(payload)
    print(filename)
    url = 'http://35.154.142.119:1337/export/format0'
    response = requests.post(url, data=payload)
    createandwritefile(filename, response.text)
    
def APICallFormat0A(payload, filename):
    print(payload)
    print(filename)
    url = 'http://35.154.142.119:1337/export/format0a'
    response = requests.post(url, data=payload)
    createandwritefile(filename, response.text)

def APICallFormat1(payload, filename):
    print(payload)
    print(filename)
    url = 'http://35.154.142.119:1337/export/format1'
    response = requests.post(url, data=payload)
    createandwritefile(filename, response.text)

#APICallFormat0({ "startDate": "2017-04-13T18:30:00.000Z", "endDate": "2017-04-14T18:30:00.000Z" }, "2017-04-14_format0.csv")

for index in range(34, 33, -1):
    d1 = datetime.today() - timedelta(days=index)
    startdate = d1.strftime("%Y-%m-%d")
    d2 = datetime.today() - timedelta(days=index-1)
    enddate = d2.strftime("%Y-%m-%d")
    APICallFormat0({ "startDate": startdate+"T18:30:00.000Z", "endDate": enddate+"T18:30:00.000Z" }, enddate+"_format0.csv")
    APICallFormat0A({ "startDate": startdate+"T18:30:00.000Z", "endDate": enddate+"T18:30:00.000Z" }, enddate+"_format0a.csv")
    APICallFormat1({ "startDate": startdate+"T18:30:00.000Z", "endDate": enddate+"T18:30:00.000Z" }, enddate+"_format1.csv")

#APICallFormat0({ "startDate": "2017-04-13T18:30:00.000Z", "endDate": "2017-04-14T18:30:00.000Z" }, "2017-04-14_format0.csv")
#url = 'http://35.154.142.119:1337/export/format0a'
#payload = { "startDate": "2017-04-13T18:30:00.000Z", "endDate": "2017-04-14T18:30:00.000Z" }

#response = requests.post(url, data=payload)
#print(response.text)

